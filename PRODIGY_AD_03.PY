import tkinter as tk
from tkinter import ttk
import time

class ColorfulStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Stopwatch")
        self.root.geometry("650x300")
        self.root.resizable(False, False)
        self.root.configure(bg='#2E3440')  # Dark background
        
        # Variables
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.last_update = 0
        
        # Color scheme
        self.colors = {
            'background': '#2E3440',
            'display_bg': '#3B4252',
            'display_fg': '#ECEFF4',
            'button_bg': '#81A1C1',
            'button_fg': '#2E3440',
            'button_active': '#5E81AC',
            'start_button': '#A3BE8C',
            'pause_button': '#EBCB8B',
            'reset_button': '#BF616A'
        }
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Time display
        self.time_label = tk.Label(
            main_frame, 
            text="00:00:000", 
            font=('Helvetica', 64, 'bold'),
            fg=self.colors['display_fg'],
            bg=self.colors['display_bg'],
            padx=20,
            pady=10,
            relief='ridge',
            bd=4
        )
        self.time_label.pack(pady=(0, 20), fill='x')
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg=self.colors['background'])
        button_frame.pack(fill='x')
        
        # Start button
        self.start_button = tk.Button(
            button_frame, 
            text="START", 
            command=self.start_timer,
            bg=self.colors['start_button'],
            fg=self.colors['button_fg'],
            activebackground=self.colors['button_active'],
            font=('Helvetica', 12, 'bold'),
            padx=20,
            pady=10,
            bd=0,
            relief='raised',
            highlightthickness=0
        )
        self.start_button.grid(row=0, column=0, padx=5, sticky='ew')
        
        # Pause button
        self.pause_button = tk.Button(
            button_frame, 
            text="PAUSE", 
            command=self.pause_timer,
            bg=self.colors['pause_button'],
            fg=self.colors['button_fg'],
            activebackground=self.colors['button_active'],
            font=('Helvetica', 12, 'bold'),
            padx=20,
            pady=10,
            bd=0,
            state=tk.DISABLED,
            relief='raised',
            highlightthickness=0
        )
        self.pause_button.grid(row=0, column=1, padx=5, sticky='ew')
        
        # Reset button
        self.reset_button = tk.Button(
            button_frame, 
            text="RESET", 
            command=self.reset_timer,
            bg=self.colors['reset_button'],
            fg=self.colors['button_fg'],
            activebackground=self.colors['button_active'],
            font=('Helvetica', 12, 'bold'),
            padx=20,
            pady=10,
            bd=0,
            relief='raised',
            highlightthickness=0
        )
        self.reset_button.grid(row=0, column=2, padx=5, sticky='ew')
        
        # Configure column weights
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        
        # Add some decorative elements
        tk.Label(
            main_frame, 
            text="⏱️ STOPWATCH", 
            font=('Helvetica', 10),
            fg='#D8DEE9',
            bg=self.colors['background']
        ).pack(side='bottom', pady=(10, 0))
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
    
    def pause_timer(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
    
    def reset_timer(self):
        self.running = False
        self.elapsed_time = 0
        self.start_time = None        # Reset start time
        self.last_update = 0          # Reset update time to avoid delay
        self.time_label.config(text="00:00:000")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    
    def update_time(self):
        if self.running:
            current_time = time.time() - self.start_time
            if current_time - self.last_update >= 0.01:
                self.elapsed_time = current_time
                self.display_time()
                self.last_update = current_time
            self.root.after(10, self.update_time)
    
    def display_time(self):
        minutes, remainder = divmod(self.elapsed_time, 60)
        seconds, milliseconds = divmod(remainder, 1)
        milliseconds = int(milliseconds * 1000)
        
        time_str = f"{int(minutes):02d}:{int(seconds):02d}:{milliseconds:03d}"
        self.time_label.config(text=time_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorfulStopwatchApp(root)
    root.mainloop()