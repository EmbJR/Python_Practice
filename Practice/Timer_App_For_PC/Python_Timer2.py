import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import time as time_module
import threading
import datetime
import math
import os
import pygame
import json
from pathlib import Path
import winsound
from dataclasses import dataclass
from typing import Optional, List
import queue

# Initialize pygame mixer for audio
pygame.mixer.init()

@dataclass
class TimerData:
    """Data class for timer information"""
    timer_id: str
    name: str
    timer_type: str  # 'time' or 'countdown'
    target_time: Optional[datetime.datetime] = None
    duration_seconds: Optional[int] = None
    audio_file: Optional[str] = None
    audio_preset: Optional[str] = None
    switch_off_minutes: int = 1
    is_running: bool = False
    is_completed: bool = False
    remaining_seconds: Optional[int] = None
    is_stopped: bool = False

class BlinkingNotification(tk.Toplevel):
    """Blinking notification window for timer events"""
    
    def __init__(self, parent, timer_name, timer_type, on_stop_callback):
        super().__init__(parent)
        self.parent = parent
        self.timer_name = timer_name
        self.on_stop_callback = on_stop_callback
        self.blinking = True
        self.blink_state = False
        
        # Configure window
        self.title("Timer Alert!")
        self.geometry("400x200")
        self.resizable(False, False)
        
        # Make window stay on top
        self.attributes('-topmost', True)
        
        # Remove window decorations (optional - uncomment if you want borderless)
        # self.overrideredirect(True)
        
        # Center the window
        self.center_window()
        
        # Create GUI
        self.create_widgets()
        
        # Start blinking
        self.blink()
        
        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self.stop_notification)
        
    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        """Create notification widgets"""
        # Main frame
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Icon/Emoji (using text for simplicity)
        icon_label = ttk.Label(main_frame, text="⏰", font=('Arial', 48))
        icon_label.pack(pady=10)
        
        # Timer name
        name_label = ttk.Label(main_frame, text=f"Timer: {self.timer_name}", 
                               font=('Arial', 14, 'bold'))
        name_label.pack(pady=5)
        
        # Message
        message_label = ttk.Label(main_frame, text="Timer has completed!", 
                                  font=('Arial', 12))
        message_label.pack(pady=5)
        
        # Stop button
        stop_button = ttk.Button(main_frame, text="Stop Alert", 
                                 command=self.stop_notification, width=15)
        stop_button.pack(pady=20)
        
        # Store references for blinking
        self.main_frame = main_frame
        self.icon_label = icon_label
        self.name_label = name_label
        self.message_label = message_label
        self.stop_button = stop_button
        
    def blink(self):
        """Blink the notification window"""
        if self.blinking:
            # Toggle colors
            if self.blink_state:
                self.main_frame.configure(style='Notification.TFrame')
                self.icon_label.configure(foreground='black')
                self.name_label.configure(foreground='black')
                self.message_label.configure(foreground='black')
            else:
                self.main_frame.configure(style='Blink.TFrame')
                self.icon_label.configure(foreground='white')
                self.name_label.configure(foreground='white')
                self.message_label.configure(foreground='white')
            
            self.blink_state = not self.blink_state
            
            # Schedule next blink
            self.after(500, self.blink)
            
    def stop_notification(self):
        """Stop the blinking notification"""
        self.blinking = False
        if self.on_stop_callback:
            self.on_stop_callback()
        self.destroy()

class AnalogClock(tk.Canvas):
    """Custom analog clock widget"""
    
    def __init__(self, parent, size=300, *args, **kwargs):
        super().__init__(parent, width=size, height=size, bg='white', highlightthickness=0, *args, **kwargs)
        self.size = size
        self.center = size // 2
        self.radius = size // 2 - 20
        self.update_clock()
        
    def draw_clock_face(self):
        """Draw the clock face with hour markers"""
        self.delete("all")
        
        # Draw clock border
        self.create_oval(5, 5, self.size-5, self.size-5, outline='black', width=2)
        
        # Draw hour markers and numbers
        for hour in range(1, 13):
            angle = math.pi/2 - (hour * math.pi/6)
            x = self.center + self.radius * 0.85 * math.cos(angle)
            y = self.center - self.radius * 0.85 * math.sin(angle)
            
            # Draw hour number
            self.create_text(x, y, text=str(hour), font=('Arial', 12, 'bold'), fill='black')
            
            # Draw minute markers
            for minute in range(0, 60, 5):
                angle_min = math.pi/2 - (minute * math.pi/30)
                x_min_start = self.center + self.radius * 0.95 * math.cos(angle_min)
                y_min_start = self.center - self.radius * 0.95 * math.sin(angle_min)
                x_min_end = self.center + self.radius * 0.85 * math.cos(angle_min)
                y_min_end = self.center - self.radius * 0.85 * math.sin(angle_min)
                self.create_line(x_min_start, y_min_start, x_min_end, y_min_end, fill='black', width=1)
    
    def update_clock(self):
        """Update clock hands based on current time"""
        self.draw_clock_face()
        
        current_time = datetime.datetime.now()
        hours = current_time.hour % 12
        minutes = current_time.minute
        seconds = current_time.second
        
        # Draw hour hand
        hour_angle = math.pi/2 - ((hours + minutes/60) * math.pi/6)
        hour_x = self.center + self.radius * 0.5 * math.cos(hour_angle)
        hour_y = self.center - self.radius * 0.5 * math.sin(hour_angle)
        self.create_line(self.center, self.center, hour_x, hour_y, width=6, fill='black', capstyle=tk.ROUND)
        
        # Draw minute hand
        min_angle = math.pi/2 - ((minutes + seconds/60) * math.pi/30)
        min_x = self.center + self.radius * 0.7 * math.cos(min_angle)
        min_y = self.center - self.radius * 0.7 * math.sin(min_angle)
        self.create_line(self.center, self.center, min_x, min_y, width=4, fill='black', capstyle=tk.ROUND)
        
        # Draw second hand
        sec_angle = math.pi/2 - (seconds * math.pi/30)
        sec_x = self.center + self.radius * 0.8 * math.cos(sec_angle)
        sec_y = self.center - self.radius * 0.8 * math.sin(sec_angle)
        self.create_line(self.center, self.center, sec_x, sec_y, width=2, fill='red', capstyle=tk.ROUND)
        
        # Draw center dot
        self.create_oval(self.center-5, self.center-5, self.center+5, self.center+5, fill='black')
        
        # Schedule next update
        self.after(1000, self.update_clock)

class TimerDialog(tk.Toplevel):
    """Dialog for adding/editing timers"""
    
    def __init__(self, parent, timer_data=None):
        super().__init__(parent)
        self.parent = parent
        self.timer_data = timer_data
        self.result = None
        self.is_playing = False
        
        self.title("Timer Settings" if not timer_data else "Edit Timer")
        self.geometry("550x550")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        # Make dialog modal
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        self.create_widgets()
        if timer_data:
            self.load_timer_data()
            
    def create_widgets(self):
        """Create dialog widgets"""
        # Main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Timer name
        ttk.Label(main_frame, text="Timer Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Timer type selection
        ttk.Label(main_frame, text="Timer Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.timer_type = tk.StringVar(value="countdown")
        ttk.Radiobutton(main_frame, text="Count-down based", variable=self.timer_type, 
                       value="countdown", command=self.toggle_timer_type).grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="Time based", variable=self.timer_type,
                       value="time", command=self.toggle_timer_type).grid(row=1, column=2, sticky=tk.W)
        
        # Countdown frame
        self.countdown_frame = ttk.LabelFrame(main_frame, text="Countdown Settings", padding="5")
        self.countdown_frame.grid(row=2, column=0, columnspan=3, sticky=tk.EW, pady=10)
        
        ttk.Label(self.countdown_frame, text="Duration (HH:MM:SS):").grid(row=0, column=0, sticky=tk.W)
        
        time_frame = ttk.Frame(self.countdown_frame)
        time_frame.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        self.hours_var = tk.StringVar(value="0")
        self.minutes_var = tk.StringVar(value="0")
        self.seconds_var = tk.StringVar(value="0")
        
        ttk.Entry(time_frame, textvariable=self.hours_var, width=3).pack(side=tk.LEFT)
        ttk.Label(time_frame, text=":").pack(side=tk.LEFT)
        ttk.Entry(time_frame, textvariable=self.minutes_var, width=3).pack(side=tk.LEFT)
        ttk.Label(time_frame, text=":").pack(side=tk.LEFT)
        ttk.Entry(time_frame, textvariable=self.seconds_var, width=3).pack(side=tk.LEFT)
        
        ttk.Label(self.countdown_frame, text="Max: 23:59:59", font=('Arial', 8)).grid(row=1, column=1, sticky=tk.W)
        
        # Time-based frame
        self.time_frame = ttk.LabelFrame(main_frame, text="Date & Time Settings", padding="5")
        self.time_frame.grid(row=3, column=0, columnspan=3, sticky=tk.EW, pady=10)
        
        ttk.Label(self.time_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W)
        self.date_var = tk.StringVar(value=datetime.datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(self.time_frame, textvariable=self.date_var, width=12).grid(row=0, column=1, sticky=tk.W, padx=5)
        
        ttk.Label(self.time_frame, text="Time (HH:MM):").grid(row=1, column=0, sticky=tk.W)
        self.time_var = tk.StringVar(value=datetime.datetime.now().strftime("%H:%M"))
        ttk.Entry(self.time_frame, textvariable=self.time_var, width=8).grid(row=1, column=1, sticky=tk.W, padx=5)
        
        self.time_frame.grid_remove()  # Hide initially
        
        # Switch off timer
        ttk.Label(main_frame, text="Switch off after (minutes):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.switch_off_var = tk.StringVar(value="1")
        ttk.Spinbox(main_frame, from_=1, to=60, textvariable=self.switch_off_var, width=10).grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Audio file selection
        ttk.Label(main_frame, text="Audio File:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        audio_frame = ttk.Frame(main_frame)
        audio_frame.grid(row=5, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        self.audio_var = tk.StringVar()
        ttk.Entry(audio_frame, textvariable=self.audio_var, width=25).pack(side=tk.LEFT)
        ttk.Button(audio_frame, text="Browse", command=self.browse_audio).pack(side=tk.LEFT, padx=5)
        
        # Test and Stop buttons for audio
        self.test_button = ttk.Button(audio_frame, text="Test", command=self.test_audio, width=6)
        self.test_button.pack(side=tk.LEFT)
        
        self.stop_button = ttk.Button(audio_frame, text="Stop", command=self.stop_audio, width=6, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Pre-tuned messages
        ttk.Label(main_frame, text="Or select preset:").grid(row=6, column=0, sticky=tk.W, pady=5)
        
        self.presets = ["None", "Beep", "Notification", "Alarm", "Ding"]
        self.preset_var = tk.StringVar(value="None")
        self.preset_combo = ttk.Combobox(main_frame, textvariable=self.preset_var, values=self.presets, width=20, state="readonly")
        self.preset_combo.grid(row=6, column=1, columnspan=2, sticky=tk.W, pady=5)
        self.preset_combo.bind('<<ComboboxSelected>>', self.on_preset_selected)
        
        # Note about presets
        ttk.Label(main_frame, text="Note: Select 'None' to use audio file", font=('Arial', 8), foreground='gray').grid(row=7, column=0, columnspan=3, sticky=tk.W, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=3, pady=20)
        
        ttk.Button(button_frame, text="OK", command=self.ok, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.cancel, width=10).pack(side=tk.LEFT, padx=5)
        
    def toggle_timer_type(self):
        """Toggle between countdown and time-based timer settings"""
        if self.timer_type.get() == "countdown":
            self.countdown_frame.grid()
            self.time_frame.grid_remove()
        else:
            self.countdown_frame.grid_remove()
            self.time_frame.grid()
            
    def browse_audio(self):
        """Browse for audio file"""
        filename = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg"), ("All Files", "*.*")]
        )
        if filename:
            self.audio_var.set(filename)
            # Clear preset selection when file is selected
            self.preset_var.set("None")
            
    def stop_audio(self):
        """Stop currently playing audio"""
        try:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.test_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
        except:
            pass
            
    def play_preset_sound(self, preset):
        """Play preset sound based on selection"""
        def play():
            if preset == "Beep":
                winsound.Beep(1000, 500)
            elif preset == "Notification":
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
            elif preset == "Alarm":
                for _ in range(3):
                    winsound.Beep(800, 200)
                    time_module.sleep(0.2)
            elif preset == "Ding":
                winsound.Beep(1500, 300)
                
        # Run in thread to avoid blocking GUI
        threading.Thread(target=play, daemon=True).start()
            
    def test_audio(self):
        """Test the selected audio or preset"""
        # Stop any currently playing audio first
        self.stop_audio()
        
        preset = self.preset_var.get()
        audio_file = self.audio_var.get()
        
        # Check if preset is selected and not "None"
        if preset and preset != "None":
            self.play_preset_sound(preset)
            messagebox.showinfo("Testing Preset", f"Playing preset: {preset}")
            
        # Check if audio file is selected
        elif audio_file and os.path.exists(audio_file):
            try:
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play()
                self.is_playing = True
                self.test_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                
                # Schedule automatic stop button re-enable after playback
                def check_playing():
                    if not pygame.mixer.music.get_busy() and self.is_playing:
                        self.stop_audio()
                    else:
                        self.after(100, check_playing)
                
                self.after(100, check_playing)
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not play audio file: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please select either a preset or audio file to test")
            
    def on_preset_selected(self, event):
        """Handle preset selection"""
        preset = self.preset_var.get()
        if preset != "None":
            # Clear audio file selection when preset is selected
            self.audio_var.set("")
            # Optionally, automatically test the preset
            if messagebox.askyesno("Test Preset", f"Would you like to test the '{preset}' preset?"):
                self.play_preset_sound(preset)
        
    def load_timer_data(self):
        """Load existing timer data for editing"""
        self.name_var.set(self.timer_data.name)
        self.timer_type.set(self.timer_data.timer_type)
        self.switch_off_var.set(str(self.timer_data.switch_off_minutes))
        
        if self.timer_data.audio_file:
            self.audio_var.set(self.timer_data.audio_file)
            self.preset_var.set("None")
        elif self.timer_data.audio_preset:
            self.preset_var.set(self.timer_data.audio_preset)
            
        if self.timer_data.timer_type == "countdown" and self.timer_data.duration_seconds:
            hours = self.timer_data.duration_seconds // 3600
            minutes = (self.timer_data.duration_seconds % 3600) // 60
            seconds = self.timer_data.duration_seconds % 60
            self.hours_var.set(str(hours))
            self.minutes_var.set(str(minutes))
            self.seconds_var.set(str(seconds))
        elif self.timer_data.target_time:
            self.date_var.set(self.timer_data.target_time.strftime("%Y-%m-%d"))
            self.time_var.set(self.timer_data.target_time.strftime("%H:%M"))
            
        self.toggle_timer_type()
        
    def validate_inputs(self):
        """Validate user inputs"""
        if not self.name_var.get().strip():
            messagebox.showerror("Error", "Please enter a timer name")
            return False
            
        if self.timer_type.get() == "countdown":
            try:
                hours = int(self.hours_var.get() or "0")
                minutes = int(self.minutes_var.get() or "0")
                seconds = int(self.seconds_var.get() or "0")
                
                total_seconds = hours * 3600 + minutes * 60 + seconds
                if total_seconds <= 0:
                    messagebox.showerror("Error", "Duration must be greater than 0")
                    return False
                if total_seconds > 24 * 3600 - 1:
                    messagebox.showerror("Error", "Maximum duration is 23:59:59")
                    return False
            except ValueError:
                messagebox.showerror("Error", "Invalid time format")
                return False
        else:
            try:
                date = datetime.datetime.strptime(self.date_var.get(), "%Y-%m-%d")
                time_val = datetime.datetime.strptime(self.time_var.get(), "%H:%M").time()
                target = datetime.datetime.combine(date.date(), time_val)
                
                if target <= datetime.datetime.now():
                    messagebox.showerror("Error", "Target time must be in the future")
                    return False
            except ValueError:
                messagebox.showerror("Error", "Invalid date/time format")
                return False
                
        try:
            int(self.switch_off_var.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid switch off time")
            return False
            
        # Validate audio selection
        preset = self.preset_var.get()
        audio_file = self.audio_var.get()
        
        if (preset == "None" or not preset) and not audio_file:
            if not messagebox.askyesno("No Audio", "No audio selected. Timer will use default beep. Continue?"):
                return False
                
        return True
        
    def get_timer_data(self):
        """Get timer data from dialog inputs"""
        preset = self.preset_var.get()
        audio_file = self.audio_var.get()
        
        if self.timer_type.get() == "countdown":
            hours = int(self.hours_var.get() or "0")
            minutes = int(self.minutes_var.get() or "0")
            seconds = int(self.seconds_var.get() or "0")
            duration = hours * 3600 + minutes * 60 + seconds
            
            return TimerData(
                timer_id=f"timer_{time_module.time()}",
                name=self.name_var.get().strip(),
                timer_type="countdown",
                duration_seconds=duration,
                audio_file=audio_file if audio_file else None,
                audio_preset=preset if preset != "None" else None,
                switch_off_minutes=int(self.switch_off_var.get()),
                remaining_seconds=duration,
                is_stopped=False
            )
        else:
            date = datetime.datetime.strptime(self.date_var.get(), "%Y-%m-%d")
            time_val = datetime.datetime.strptime(self.time_var.get(), "%H:%M").time()
            target = datetime.datetime.combine(date.date(), time_val)
            
            return TimerData(
                timer_id=f"timer_{time_module.time()}",
                name=self.name_var.get().strip(),
                timer_type="time",
                target_time=target,
                audio_file=audio_file if audio_file else None,
                audio_preset=preset if preset != "None" else None,
                switch_off_minutes=int(self.switch_off_var.get()),
                is_stopped=False
            )
            
    def ok(self):
        """OK button handler"""
        if self.validate_inputs():
            self.stop_audio()
            self.result = self.get_timer_data()
            self.destroy()
            
    def cancel(self):
        """Cancel button handler"""
        self.stop_audio()
        self.result = None
        self.destroy()

class TimerApp:
    """Main application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Timer & Countdown Application")
        self.root.geometry("200x200")
        self.root.minsize(800, 500)
        
        # Initialize timers storage
        self.timers = []
        self.timer_frames = {}
        self.completed_timers = set()
        self.notification_windows = {}  # Track notification windows
        
        # Load saved timers
        self.load_timers()
        
        # Create GUI
        self.create_gui()
        
        # Start timer checking thread
        self.running = True
        self.timer_thread = threading.Thread(target=self.check_timers, daemon=True)
        self.timer_thread.start()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_gui(self):
        """Create main GUI"""
        # Configure styles for notifications
        style = ttk.Style()
        style.configure('Notification.TFrame', background='white')
        style.configure('Blink.TFrame', background='red')
        style.configure('BlinkNotification.TFrame', background='#ff4444')  # Bright red for notifications
        
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Analog clock
        left_panel = ttk.Frame(main_container, width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Clock frame
        clock_frame = ttk.LabelFrame(left_panel, text="Current Time", padding=10)
        clock_frame.pack(fill=tk.BOTH, expand=True)
        
        self.clock = AnalogClock(clock_frame, size=350)
        self.clock.pack(expand=True)
        
        # Digital time display
        self.digital_time = ttk.Label(clock_frame, font=('Arial', 16, 'bold'))
        self.digital_time.pack(pady=10)
        self.update_digital_time()
        
        # Right panel - Timers
        right_panel = ttk.Frame(main_container, width=400)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Timer list header
        header_frame = ttk.Frame(right_panel)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(header_frame, text="Active Timers", font=('Arial', 14, 'bold')).pack(side=tk.LEFT)
        
        # Add timer button
        add_button = ttk.Button(header_frame, text="+", width=3, command=self.add_timer)
        add_button.pack(side=tk.RIGHT)
        
        # Timer list container
        self.timer_list_frame = ttk.Frame(right_panel)
        self.timer_list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create scrollable frame for timers
        self.create_timer_list()
        
        # Refresh timer list
        self.refresh_timer_list()
        
    def create_timer_list(self):
        """Create scrollable timer list"""
        # Canvas for scrolling
        self.timer_canvas = tk.Canvas(self.timer_list_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.timer_list_frame, orient="vertical", command=self.timer_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.timer_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.timer_canvas.configure(scrollregion=self.timer_canvas.bbox("all"))
        )
        
        self.timer_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.timer_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.timer_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.timer_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.timer_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def update_digital_time(self):
        """Update digital time display"""
        current = datetime.datetime.now().strftime("%H:%M:%S")
        self.digital_time.config(text=current)
        self.root.after(1000, self.update_digital_time)
        
    def add_timer(self):
        """Open dialog to add new timer"""
        dialog = TimerDialog(self.root)
        self.root.wait_window(dialog)
        
        if dialog.result:
            self.timers.append(dialog.result)
            self.save_timers()
            self.refresh_timer_list()
            
    def edit_timer(self, timer_data):
        """Edit existing timer"""
        dialog = TimerDialog(self.root, timer_data)
        self.root.wait_window(dialog)
        
        if dialog.result:
            # Update timer data
            timer_data.name = dialog.result.name
            timer_data.timer_type = dialog.result.timer_type
            timer_data.target_time = dialog.result.target_time
            timer_data.duration_seconds = dialog.result.duration_seconds
            timer_data.audio_file = dialog.result.audio_file
            timer_data.audio_preset = dialog.result.audio_preset
            timer_data.switch_off_minutes = dialog.result.switch_off_minutes
            
            if timer_data.timer_type == "countdown":
                timer_data.remaining_seconds = timer_data.duration_seconds
                
            # Reset completion state
            timer_data.is_completed = False
            timer_data.is_stopped = False
            
            # Close any existing notification for this timer
            if timer_data.timer_id in self.notification_windows:
                try:
                    self.notification_windows[timer_data.timer_id].destroy()
                except:
                    pass
                del self.notification_windows[timer_data.timer_id]
                
            self.save_timers()
            self.refresh_timer_list()
            
    def delete_timer(self, timer_data):
        """Delete timer"""
        if messagebox.askyesno("Confirm Delete", f"Delete timer '{timer_data.name}'?"):
            # Close any existing notification for this timer
            if timer_data.timer_id in self.notification_windows:
                try:
                    self.notification_windows[timer_data.timer_id].destroy()
                except:
                    pass
                del self.notification_windows[timer_data.timer_id]
                
            self.timers.remove(timer_data)
            if timer_data.timer_id in self.timer_frames:
                self.timer_frames[timer_data.timer_id].destroy()
                del self.timer_frames[timer_data.timer_id]
            self.save_timers()
            self.refresh_timer_list()
            
    def refresh_timer_list(self):
        """Refresh the timer list display"""
        # Clear existing timer frames
        for frame in self.timer_frames.values():
            frame.destroy()
        self.timer_frames.clear()
        
        # Create frames for each timer
        for timer in self.timers:
            self.create_timer_frame(timer)
            
    def create_timer_frame(self, timer):
        """Create a frame for a single timer"""
        frame = ttk.Frame(self.scrollable_frame, relief=tk.RAISED, borderwidth=1)
        frame.pack(fill=tk.X, pady=2, padx=2)
        
        # Timer info
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Name and type
        name_label = ttk.Label(info_frame, text=timer.name, font=('Arial', 10, 'bold'))
        name_label.pack(anchor=tk.W)
        
        # Audio info
        audio_info = ""
        if timer.audio_preset and timer.audio_preset != "None":
            audio_info = f" (Preset: {timer.audio_preset})"
        elif timer.audio_file:
            audio_info = " (Custom Audio)"
            
        type_label = ttk.Label(info_frame, text=f"Type: {timer.timer_type}{audio_info}", font=('Arial', 8))
        type_label.pack(anchor=tk.W)
        
        # Time display
        self.update_timer_display(timer, info_frame)
        
        # Control buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Edit", command=lambda: self.edit_timer(timer), width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Delete", command=lambda: self.delete_timer(timer), width=8).pack(side=tk.LEFT, padx=2)
        
        if timer.is_completed:
            ttk.Button(button_frame, text="Stop", command=lambda: self.stop_timer_alert(timer), width=8).pack(side=tk.LEFT, padx=2)
            
        self.timer_frames[timer.timer_id] = frame
        
    def update_timer_display(self, timer, parent_frame):
        """Update timer display with current time"""
        # Remove old time label if exists
        for widget in parent_frame.winfo_children():
            if isinstance(widget, ttk.Label) and widget.cget('font') == ('Arial', 9):
                widget.destroy()
                
        # Create new time label
        if timer.is_completed:
            time_text = "COMPLETED - Click Stop to dismiss"
            time_label = ttk.Label(parent_frame, text=time_text, font=('Arial', 9), foreground='red')
            time_label.pack(anchor=tk.W)
            
            # Make the frame blink
            self.blink_timer_frame(timer.timer_id)
        elif timer.is_stopped:
            time_text = "STOPPED - Click Edit to restart"
            time_label = ttk.Label(parent_frame, text=time_text, font=('Arial', 9), foreground='gray')
            time_label.pack(anchor=tk.W)
        else:
            if timer.timer_type == "countdown" and timer.remaining_seconds is not None:
                hours = timer.remaining_seconds // 3600
                minutes = (timer.remaining_seconds % 3600) // 60
                seconds = timer.remaining_seconds % 60
                time_text = f"Remaining: {hours:02d}:{minutes:02d}:{seconds:02d}"
            elif timer.target_time:
                remaining = timer.target_time - datetime.datetime.now()
                if remaining.total_seconds() > 0:
                    hours = int(remaining.total_seconds() // 3600)
                    minutes = int((remaining.total_seconds() % 3600) // 60)
                    seconds = int(remaining.total_seconds() % 60)
                    time_text = f"Time until: {hours:02d}:{minutes:02d}:{seconds:02d}"
                else:
                    time_text = "Due now"
            else:
                time_text = "Ready"
                
            time_label = ttk.Label(parent_frame, text=time_text, font=('Arial', 9))
            time_label.pack(anchor=tk.W)
            
    def blink_timer_frame(self, timer_id):
        """Make timer frame blink when completed"""
        if timer_id in self.timer_frames:
            frame = self.timer_frames[timer_id]
            
            if not hasattr(self, '_blink_state'):
                self._blink_state = {}
                
            if timer_id not in self._blink_state:
                self._blink_state[timer_id] = True
                
            # Toggle background color
            if self._blink_state[timer_id]:
                frame.configure(style='Blink.TFrame')
            else:
                frame.configure(style='TFrame')
                
            self._blink_state[timer_id] = not self._blink_state[timer_id]
            
            # Continue blinking if timer is still completed
            timer = self.get_timer_by_id(timer_id)
            if timer and timer.is_completed and not timer.is_stopped:
                self.root.after(500, lambda: self.blink_timer_frame(timer_id))
                
    def get_timer_by_id(self, timer_id):
        """Get timer by ID"""
        for timer in self.timers:
            if timer.timer_id == timer_id:
                return timer
        return None
        
    def check_timers(self):
        """Background thread to check timer conditions"""
        while self.running:
            try:
                current_time = datetime.datetime.now()
                
                for timer in self.timers:
                    # Skip if timer is stopped or already completed
                    if timer.is_stopped or timer.is_completed:
                        continue
                        
                    should_trigger = False
                    
                    if timer.timer_type == "countdown" and timer.remaining_seconds is not None:
                        if timer.remaining_seconds <= 0:
                            should_trigger = True
                        else:
                            timer.remaining_seconds -= 1
                            
                    elif timer.timer_type == "time" and timer.target_time:
                        if current_time >= timer.target_time:
                            should_trigger = True
                            
                    if should_trigger and not timer.is_completed and not timer.is_stopped:
                        timer.is_completed = True
                        self.root.after(0, lambda t=timer: self.timer_triggered(t))
                        
                # Update displays
                self.root.after(0, self.refresh_timer_list)
                
            except Exception as e:
                print(f"Error in timer check: {e}")
                
            time_module.sleep(1)
            
    def timer_triggered(self, timer):
        """Handle timer trigger event"""
        # Bring window to top
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.attributes('-topmost', False)
        
        # Play audio based on preset or file
        if timer.audio_preset and timer.audio_preset != "None":
            # Play preset sound
            if timer.audio_preset == "Beep":
                winsound.Beep(1000, 500)
            elif timer.audio_preset == "Notification":
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
            elif timer.audio_preset == "Alarm":
                for _ in range(3):
                    winsound.Beep(800, 200)
                    time_module.sleep(0.2)
            elif timer.audio_preset == "Ding":
                winsound.Beep(1500, 300)
        elif timer.audio_file and os.path.exists(timer.audio_file):
            try:
                pygame.mixer.music.load(timer.audio_file)
                pygame.mixer.music.play()
            except:
                winsound.Beep(1000, 1000)  # Fallback beep
        else:
            winsound.Beep(1000, 1000)  # Default beep
            
        # Show blinking notification window
        self.show_blinking_notification(timer)
        
        # Schedule auto stop
        self.root.after(timer.switch_off_minutes * 60 * 1000, 
                       lambda: self.auto_stop_timer(timer))
        
    def show_blinking_notification(self, timer):
        """Show a blinking notification window for the timer"""
        # Close any existing notification for this timer
        if timer.timer_id in self.notification_windows:
            try:
                self.notification_windows[timer.timer_id].destroy()
            except:
                pass
        
        # Create new notification window
        def on_notification_stop():
            self.stop_timer_alert(timer)
            if timer.timer_id in self.notification_windows:
                del self.notification_windows[timer.timer_id]
        
        notification = BlinkingNotification(
            self.root, 
            timer.name, 
            timer.timer_type,
            on_notification_stop
        )
        
        # Store reference
        self.notification_windows[timer.timer_id] = notification
        
    def auto_stop_timer(self, timer):
        """Automatically stop timer alert"""
        if timer.is_completed and not timer.is_stopped:
            self.stop_timer_alert(timer)
            
    def stop_timer_alert(self, timer):
        """Stop timer alert and prevent it from running again"""
        timer.is_completed = False
        timer.is_stopped = True
        
        # Close notification window if exists
        if timer.timer_id in self.notification_windows:
            try:
                self.notification_windows[timer.timer_id].destroy()
            except:
                pass
            del self.notification_windows[timer.timer_id]
        
        # Reset remaining seconds for countdown timers
        if timer.timer_type == "countdown":
            timer.remaining_seconds = timer.duration_seconds
            
        self.refresh_timer_list()
        
        # Stop any playing audio
        pygame.mixer.music.stop()
        
    def save_timers(self):
        """Save timers to file"""
        try:
            timers_data = []
            for timer in self.timers:
                timer_dict = {
                    'timer_id': timer.timer_id,
                    'name': timer.name,
                    'timer_type': timer.timer_type,
                    'switch_off_minutes': timer.switch_off_minutes,
                    'audio_file': timer.audio_file,
                    'audio_preset': timer.audio_preset,
                    'is_running': timer.is_running,
                    'is_completed': timer.is_completed,
                    'is_stopped': timer.is_stopped
                }
                
                if timer.target_time:
                    timer_dict['target_time'] = timer.target_time.isoformat()
                    
                if timer.duration_seconds:
                    timer_dict['duration_seconds'] = timer.duration_seconds
                    
                if timer.remaining_seconds:
                    timer_dict['remaining_seconds'] = timer.remaining_seconds
                    
                timers_data.append(timer_dict)
                
            with open('timers.json', 'w') as f:
                json.dump(timers_data, f, indent=2)
        except Exception as e:
            print(f"Error saving timers: {e}")
            
    def load_timers(self):
        """Load timers from file"""
        try:
            if os.path.exists('timers.json'):
                with open('timers.json', 'r') as f:
                    timers_data = json.load(f)
                    
                for timer_dict in timers_data:
                    target_time = None
                    if 'target_time' in timer_dict:
                        target_time = datetime.datetime.fromisoformat(timer_dict['target_time'])
                        
                    timer = TimerData(
                        timer_id=timer_dict['timer_id'],
                        name=timer_dict['name'],
                        timer_type=timer_dict['timer_type'],
                        target_time=target_time,
                        duration_seconds=timer_dict.get('duration_seconds'),
                        audio_file=timer_dict.get('audio_file'),
                        audio_preset=timer_dict.get('audio_preset'),
                        switch_off_minutes=timer_dict.get('switch_off_minutes', 1),
                        is_running=timer_dict.get('is_running', False),
                        is_completed=timer_dict.get('is_completed', False),
                        remaining_seconds=timer_dict.get('remaining_seconds'),
                        is_stopped=timer_dict.get('is_stopped', False)
                    )
                    self.timers.append(timer)
        except Exception as e:
            print(f"Error loading timers: {e}")
            
    def on_closing(self):
        """Handle window closing"""
        self.running = False
        
        # Close all notification windows
        for notification in self.notification_windows.values():
            try:
                notification.destroy()
            except:
                pass
        
        self.save_timers()
        pygame.mixer.quit()
        self.root.destroy()

def main():
    """Main function"""
    root = tk.Tk()
    
    # Configure styles
    style = ttk.Style()
    style.theme_use('clam')
    
    # Create blink styles
    style.configure('Blink.TFrame', background='red')
    style.configure('Notification.TFrame', background='white')
    style.configure('BlinkNotification.TFrame', background='#ff4444')
    
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()