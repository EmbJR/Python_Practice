import tkinter as tk

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
        
        # MOCK DATA: Fill specific areas to test layout accuracy
        # Fill Page 5, Bytes 10-20
        for b in range(10, 21):
            self.memory_buffer[5][b] = 0xAA
        # Fill Page 10 to 15, Bytes 0-5
        for p in range(100, 160):
            for b in range(263):
                self.memory_buffer[p][b] = 0xBB
        
        self.setup_ui()

    def setup_ui(self):
        # Control Panel
        control_frame = tk.Frame(self.root, bg="#333")
        control_frame.pack(side=tk.TOP, fill=tk.X)
        
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

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    app = MemoryVisualizer(root)
    root.mainloop()
