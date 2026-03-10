import tkinter as tk
import serial
import serial.tools.list_ports
import threading
import time
import struct
import queue

class MemoryVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Chip Memory Layout (Optimized)")
        
        # Configuration
        self.PAGES = 2048
        self.BYTES_PER_PAGE = 264
        self.cell_size = 6  # Default zoom level
        
        # Initialize buffer: 0xFF is empty
        # This simulates your UART buffer
        self.memory_buffer = [[0xFF for _ in range(self.BYTES_PER_PAGE)] for _ in range(self.PAGES)]
        
        # Serial port connection state
        self.serial_connection = None
        self.available_ports = []
        
        # Memory read state
        self.is_reading = False
        self.read_complete = False
        self.read_error = None
        self.chunks_received = 0
        self.read_thread = None
        self.stop_reading = threading.Event()
        
        # Queue for thread-safe GUI updates
        self.update_queue = queue.Queue()
        
        # MOCK DATA: Fill specific areas to test layout accuracy
        # Fill Page 5, Bytes 10-20
        for b in range(10, 21):
            self.memory_buffer[5][b] = 0xAA
        # Fill Page 10 to 15, Bytes 0-5
        for p in range(100, 160):
            for b in range(263):
                self.memory_buffer[p][b] = 0xBB
        
        self.setup_ui()
        
        # Start processing update queue
        self.root.after(100, self.process_update_queue)

    def setup_ui(self):
        # Control Panel
        control_frame = tk.Frame(self.root, bg="#333")
        control_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Serial Port Selection Frame
        serial_frame = tk.Frame(control_frame, bg="#333")
        serial_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(serial_frame, text="Serial Port:", fg="white", bg="#333").pack(anchor=tk.W)
        
        # Serial port listbox with scrollbar
        self.SerialPortList = tk.Listbox(serial_frame, height=4, width=20, bg="#1e1e1e", fg="white", selectbackground="#2ECC71")
        self.SerialPortList.pack(side=tk.LEFT, fill=tk.X, padx=(0, 2))
        serial_scroll = tk.Scrollbar(serial_frame, orient=tk.VERTICAL, command=self.SerialPortList.yview)
        serial_scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.SerialPortList.config(yscrollcommand=serial_scroll.set)
        
        # Refresh and Connect buttons frame
        serial_btn_frame = tk.Frame(control_frame, bg="#333")
        serial_btn_frame.pack(side=tk.LEFT, padx=5)
        
        tk.Button(serial_btn_frame, text="Refresh Ports", command=self.refresh_serial_ports, bg="#555", fg="white").pack(pady=2)
        self.connect_btn = tk.Button(serial_btn_frame, text="Connect", command=self.toggle_connection, bg="#555", fg="white", width=12)
        self.connect_btn.pack(pady=2)
        
        # Get Memory button - placed below Connect button
        self.get_memory_btn = tk.Button(serial_btn_frame, text="Get_Memory", command=self.start_get_memory, bg="#3498db", fg="white", width=12, state=tk.DISABLED)
        self.get_memory_btn.pack(pady=2)
        
        # Progress bar for memory read operation
        progress_frame = tk.Frame(control_frame, bg="#333")
        progress_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(progress_frame, text="Memory Progress:", fg="white", bg="#333").pack(anchor=tk.W)
        self.progress_bar = tk.Canvas(progress_frame, width=150, height=20, bg="#1e1e1e", highlightthickness=0)
        self.progress_bar.pack(pady=2)
        self.progress_fill = None
        self.progress_label = tk.Label(progress_frame, text="0/2048 chunks", fg="#00FF00", bg="#333", font=("Arial", 8))
        self.progress_label.pack()
        
        # Zoom controls
        tk.Label(control_frame, text="Zoom:", fg="white", bg="#333").pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="+", width=4, command=self.zoom_in).pack(side=tk.LEFT, padx=2, pady=5)
        tk.Button(control_frame, text="-", width=4, command=self.zoom_out).pack(side=tk.LEFT, padx=2, pady=5)

        ReadButton = tk.Button(control_frame, text="Read_Memmory", command=self.Read_Memmory, bg="Red")
        ReadButton.pack(side=tk.RIGHT, padx=2)
        
        tk.Button(control_frame, text="Refresh View", command=self.draw_memory).pack(side=tk.LEFT, padx=20)
        
        self.status_label = tk.Label(control_frame, text="Hover over memory to see address", fg="#00FF00", bg="#333")
        self.status_label.pack(side=tk.RIGHT, padx=10)

        # Canvas Setup
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Darker background helps the "empty" bytes feel more like a grid
        self.canvas = tk.Canvas(self.canvas_frame, bg="#1e1e1e", highlightthickness=0)
        self.v_scroll = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.h_scroll = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)
        
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Mouse tracking
        self.canvas.bind("<Motion>", self.update_status)
        
        # Bind scroll events for automatic refresh on scroll
        self.v_scroll.bind("<ButtonRelease-1>", lambda e: self.draw_memory())
        self.h_scroll.bind("<ButtonRelease-1>", lambda e: self.draw_memory())
        
        # Bind keyboard arrow keys for scrolling with auto-refresh
        self.canvas.focus_set()
        self.canvas.bind("<Up>", self.scroll_up)
        self.canvas.bind("<Down>", self.scroll_down)
        self.canvas.bind("<Left>", self.scroll_left)
        self.canvas.bind("<Right>", self.scroll_right)
        
        # Bind mouse wheel scrolling
        self.canvas.bind("<MouseWheel>", self.mouse_wheel_vertical)
        
        self.draw_memory()

    def scroll_up(self, event):
        """Scroll up and refresh view"""
        self.canvas.yview_scroll(-1, "units")
        self.draw_memory()
        return "break"

    def scroll_down(self, event):
        """Scroll down and refresh view"""
        self.canvas.yview_scroll(1, "units")
        self.draw_memory()
        return "break"

    def scroll_left(self, event):
        """Scroll left and refresh view"""
        self.canvas.xview_scroll(-1, "units")
        self.draw_memory()
        return "break"

    def scroll_right(self, event):
        """Scroll right and refresh view"""
        self.canvas.xview_scroll(1, "units")
        self.draw_memory()
        return "break"

    def mouse_wheel_vertical(self, event):
        """Mouse wheel vertical scrolling with refresh"""
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        else:
            self.canvas.yview_scroll(1, "units")
        self.draw_memory()
        return "break"

    def get_visible_viewport(self):
        """Calculate visible page and byte range based on scroll position"""
        try:
            vscroll_info = self.v_scroll.get()
            hscroll_info = self.h_scroll.get()
            
            # Calculate visible range
            start_page = int(vscroll_info[0] * self.PAGES)
            end_page = int(vscroll_info[1] * self.PAGES)
            start_byte = int(hscroll_info[0] * self.BYTES_PER_PAGE)
            end_byte = int(hscroll_info[1] * self.BYTES_PER_PAGE)
            
            # Add buffer for smooth scrolling
            buffer = 5
            start_page = max(0, start_page - buffer)
            end_page = min(self.PAGES, end_page + buffer)
            start_byte = max(0, start_byte - buffer)
            end_byte = min(self.BYTES_PER_PAGE, end_byte + buffer)
            
            return start_page, end_page, start_byte, end_byte
        except:
            return 0, min(100, self.PAGES), 0, min(50, self.BYTES_PER_PAGE)

    def draw_memory(self):
        """Optimized memory drawing using virtual scrolling and merged rectangles"""
        self.canvas.delete("all")
        s = self.cell_size
        gap = 1 if s > 3 else 0
        
        # Get visible viewport
        start_page, end_page, start_byte, end_byte = self.get_visible_viewport()
        
        fill_color = "#2ECC71"
        
        # OPTIMIZATION: Merge continuous non-0xFF bytes into single rectangles
        for p_idx in range(start_page, end_page):
            y1 = p_idx * s
            y2 = y1 + (s - gap)
            
            row = self.memory_buffer[p_idx]
            
            # Find contiguous runs of non-0xFF values within visible range
            start_byte_idx = None
            
            for b_idx in range(start_byte, end_byte):
                val = row[b_idx]
                
                if val != 0xFF:
                    # Start of a new run
                    if start_byte_idx is None:
                        start_byte_idx = b_idx
                else:
                    # End of a run - draw the rectangle
                    if start_byte_idx is not None:
                        x1 = start_byte_idx * s
                        x2 = b_idx * s  # End of continuous run
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
                        start_byte_idx = None
            
            # Handle case where run extends to end of visible range
            if start_byte_idx is not None:
                x1 = start_byte_idx * s
                x2 = end_byte * s
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="")
        
        # Set scroll region
        self.canvas.config(scrollregion=(0, 0, self.BYTES_PER_PAGE * s, self.PAGES * s))

    def update_status(self, event):
        # Convert mouse pixel position to Page and Byte
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        page = int(canvas_y // self.cell_size)
        byte = int(canvas_x // self.cell_size)
        
        if 0 <= page < self.PAGES and 0 <= byte < self.BYTES_PER_PAGE:
            val = self.memory_buffer[page][byte]
            status = "Empty" if val == 0xFF else f"Value: {hex(val)}"
            self.status_label.config(text=f"Page: {page} | Byte: {byte} | {status}")

    def zoom_in(self):
        if self.cell_size < 40:
            self.cell_size += 2
            self.draw_memory()

    def zoom_out(self):
        if self.cell_size > 2:
            self.cell_size -= 2
            self.draw_memory()

    def Read_Memmory(self):
        # Optimized: Use list comprehension
        self.memory_buffer = [[0x1E] * self.BYTES_PER_PAGE for _ in range(self.PAGES)]
        self.draw_memory()

    def refresh_serial_ports(self):
        """Refresh the list of available serial ports"""
        self.available_ports = []
        self.SerialPortList.delete(0, tk.END)
        
        ports = serial.tools.list_ports.comports()
        for port in ports:
            port_name = f"{port.device} - {port.description}"
            self.available_ports.append(port.device)
            self.SerialPortList.insert(tk.END, port_name)
        
        if not self.available_ports:
            self.SerialPortList.insert(tk.END, "No ports found")

    def toggle_connection(self):
        """Toggle between Connect and Disconnect states"""
        if self.serial_connection is None:
            # Try to connect
            self.connect_to_port()
        else:
            # Disconnect
            self.disconnect_from_port()

    def connect_to_port(self):
        """Connect to the selected serial port"""
        selection = self.SerialPortList.curselection()
        if not selection:
            self.status_label.config(text="Please select a serial port", fg="red")
            return
        
        port_index = selection[0]
        if port_index >= len(self.available_ports):
            self.status_label.config(text="No valid port selected", fg="red")
            return
        
        port = self.available_ports[port_index]
        
        try:
            self.serial_connection = serial.Serial(port, 115200, timeout=1)
            self.connect_btn.config(text="Disconnect", bg="#e74c3c")
            self.status_label.config(text=f"Connected to {port}", fg="#00FF00")
            # Enable Get_Memory button when connected
            self.get_memory_btn.config(state=tk.NORMAL)
        except Exception as e:
            self.status_label.config(text=f"Connection failed: {str(e)}", fg="red")
            self.serial_connection = None

    def disconnect_from_port(self):
        """Disconnect from the current serial port"""
        # Stop any ongoing read operation
        if self.is_reading:
            self.stop_reading.set()
            if self.read_thread and self.read_thread.is_alive():
                self.read_thread.join(timeout=2)
            self.is_reading = False
        
        if self.serial_connection:
            try:
                self.serial_connection.close()
            except:
                pass
            self.serial_connection = None
            self.connect_btn.config(text="Connect", bg="#555")
            self.get_memory_btn.config(state=tk.DISABLED, bg="#3498db", text="Get_Memory")
            self.status_label.config(text="Disconnected", fg="#00FF00")
            
            # Reset progress bar
            self.update_progress_bar(0, 2048)

    def process_update_queue(self):
        """Process updates from the reading thread"""
        try:
            while True:
                update_type, data = self.update_queue.get_nowait()
                
                if update_type == "progress":
                    print("^^^^ Progress")
                    chunks_received, total_chunks = data
                    self.update_progress_bar(chunks_received, total_chunks)
                elif update_type == "complete":
                    self.read_complete = True
                    self.is_reading = False
                    self.get_memory_btn.config(state=tk.NORMAL, bg="#3498db", text="Get_Memory")
                    self.status_label.config(text=f"Memory read complete! {data} chunks received", fg="#00FF00")
                    self.draw_memory()
                elif update_type == "error":
                    self.read_error = data
                    self.is_reading = False
                    self.get_memory_btn.config(state=tk.NORMAL, bg="#3498db", text="Get_Memory")
                    self.status_label.config(text=f"Error: {data}", fg="red")
                elif update_type == "memory_chunk":
                    page_num, chunk_data = data
                    # Update memory buffer with received chunk
                    if page_num < self.PAGES and len(chunk_data) == self.BYTES_PER_PAGE:
                        self.memory_buffer[page_num] = chunk_data
        except queue.Empty:
            pass
        
        # Continue checking for updates
        if self.is_reading:
            self.root.after(50, self.process_update_queue)

    def update_progress_bar(self, chunks_received, total_chunks):
        """Update the progress bar display"""
        self.progress_label.config(text=f"{chunks_received}/{total_chunks} chunks")
        
        # Calculate fill width
        max_width = 150
        fill_width = int((chunks_received / total_chunks) * max_width) if total_chunks > 0 else 0
        
        # Delete old fill rectangle
        if self.progress_fill:
            self.progress_bar.delete(self.progress_fill)
        
        # Draw new fill rectangle
        self.progress_fill = self.progress_bar.create_rectangle(
            0, 0, fill_width, 20, fill="#2ECC71", outline=""
        )

    def calculate_crc16(self, data):
        """Calculate CRC16 for the data (Modbus CRC16)"""
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc

    def build_read_memory_command(self):
        """Build the 'Read entire Memory' command according to protocol"""
        # Command: 0x01 (Read entire Memory)
        cmd = 0x01
        
        # Length is 1 byte (just the command)
        length = 0x0001
        
        # Build data without header for CRC calculation
        # Format: Length (2 bytes) + Cmd (1 byte)
        data_for_crc = struct.pack('<HB', length, cmd)

        print("-------------------------------------")
        print(len(data_for_crc))
        
        # Calculate CRC16
        crc = self.calculate_crc16(data_for_crc)
        
        # Build full packet: Header + CRC + Length + Cmd
        # Header: 0xA5 (1 byte)
        # CRC: 2 bytes
        # Length: 2 bytes
        # Cmd: 1 byte
        packet = struct.pack('<B', 0xA5)  # Header
        packet += struct.pack('<H', crc)   # CRC16
        packet += struct.pack('<HB', length, cmd)  # Length (2 bytes) + Cmd (1 byte)
        
        return packet

    def parse_memory_chunk(self, data):
        """Parse a memory chunk response from controller"""
        # Expected format: Header(1) + CRC(2) + Length(2) + Cmd(1) + Address(2) + Data(264)
        # Total: 272 bytes minimum
        if len(data) < 272:
            print("########## Len error")
            return None, None, None
        try:
            # Parse the packet
            header = data[0]
            if header != 0xA5:
                return None, None, None
            
            # Check for error response (Cmd = 0x70)
            cmd = data[5]
            if cmd == 0x70:
                return None, None, "Error response received from controller"
            
            # Extract address (bytes 6-7)
            address = struct.unpack('<H', data[6:8])[0]

            print(f"########## header = {header}, cmd = {cmd}, address = {address}")
            
            # Page number is the address (each page is 264 bytes)
            page_num = address
            
            # Extract data (bytes 8 to end)
            chunk_data = list(data[8:272])
            
            return page_num, chunk_data, None
        except Exception as e:
            return None, None, str(e)

    def receive_with_timeout(self, timeout_seconds=240):
        """Receive data from serial port with timeout"""
        start_time = time.time()
        received_data = bytearray()
        
        # Expected response length: 272 bytes (Header + CRC + Length + Cmd + Address + Data)
        expected_length = 272
        
        # Flush input buffer to discard any stale data before reading response
        self.serial_connection.reset_input_buffer()
        
        while (time.time() - start_time) < timeout_seconds:
            if self.stop_reading.is_set():
                return None, "Reading stopped by user"
            
            try:
                # Use read with timeout instead of in_waiting for more reliable reading
                # This prevents blocking issues with some USB-serial adapters
                bytes_read = self.serial_connection.read(272)  # Read up to expected bytes with timeout
                
                if bytes_read:
                    print("#####################################")
                    print(f"Received byte is {bytes_read} length is {len(bytes_read)}")
                    received_data.extend(bytes_read)
                    print("#####################################")
                    
                    # Check if we have enough data
                    if len(received_data) >= expected_length:
                        # Return the first complete packet
                        return received_data[:expected_length], None
                else:
                    # No data received within timeout, small delay to prevent CPU spinning
                    time.sleep(0.01)
            except serial.SerialException as e:
                return None, f"Serial error: {str(e)}"
        
        return None, "Timeout waiting for response"

    def read_memory_worker(self):
        """Worker thread for reading memory from controller"""
        try:
            # Send Read entire Memory command
            cmd_packet = self.build_read_memory_command()
            self.serial_connection.write(cmd_packet)
            self.serial_connection.flush()
            
            # Reset counters
            self.chunks_received = 0
            max_chunks = 2048
            timeout_seconds = 240  # 4 minutes
            
            # Wait for chunks
            while self.chunks_received < max_chunks:
                if self.stop_reading.is_set():
                    break
                
                # Receive a chunk
                chunk_data, error = self.receive_with_timeout(timeout_seconds)
                
                if error:
                    # Check if it's just a timeout (no more data)
                    if "Timeout" in error and self.chunks_received > 0:
                        # Timeout is okay if we received some data
                        break
                    self.update_queue.put(("error", error))
                    return
                
                if chunk_data is None:
                    break
                
                # Parse the chunk
                page_num, data, parse_error = self.parse_memory_chunk(chunk_data)
                
                if parse_error:
                    if "Error response" in parse_error:
                        self.update_queue.put(("error", parse_error))
                    else:
                        self.update_queue.put(("error", f"Parse error: {parse_error}"))
                    return
                
                if page_num is not None and data is not None:
                    # Update memory buffer
                    self.update_queue.put(("memory_chunk", (page_num, data)))
                    self.chunks_received += 1
                    
                    # Update progress
                    self.update_queue.put(("progress", (self.chunks_received, max_chunks)))
            
            # Reading complete
            self.update_queue.put(("complete", self.chunks_received))
            
        except Exception as e:
            self.update_queue.put(("error", str(e)))

    def start_get_memory(self):
        """Start the memory read operation"""
        if self.serial_connection is None or not self.serial_connection.is_open:
            self.status_label.config(text="Please connect to a serial port first", fg="red")
            return
        
        if self.is_reading:
            self.status_label.config(text="Memory read already in progress", fg="orange")
            return
        
        # Reset state
        self.is_reading = True
        self.read_complete = False
        self.read_error = None
        self.stop_reading.clear()
        
        # Disable button during reading
        self.get_memory_btn.config(state=tk.DISABLED, bg="#f39c12", text="Reading...")
        
        # Reset memory buffer
        self.memory_buffer = [[0xFF for _ in range(self.BYTES_PER_PAGE)] for _ in range(self.PAGES)]
        
        # Reset progress bar
        self.update_progress_bar(0, 2048)
        
        # Start reading in a separate thread
        self.read_thread = threading.Thread(target=self.read_memory_worker, daemon=True)
        self.read_thread.start()
        
        self.status_label.config(text="Reading memory from controller...", fg="#00FF00")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    app = MemoryVisualizer(root)
    root.mainloop()
