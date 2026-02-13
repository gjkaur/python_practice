"""
PCPP 3.1, 3.2, 3.3: GUI Programming with tkinter Demo

Demonstrates:
- Creating windows and widgets
- Layout managers
- Event handling
- Observable variables
"""

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable


# PCPP 3.2: Basic tkinter Window
def create_basic_window() -> None:
    """PCPP 3.2: Create a basic window with widgets."""
    root = tk.Tk()
    root.title("Basic Window")
    root.geometry("300x200")
    
    # Label widget
    label = tk.Label(root, text="Hello, tkinter!")
    label.pack(pady=10)
    
    # Button widget
    button = tk.Button(root, text="Click Me", command=lambda: print("Clicked!"))
    button.pack(pady=5)
    
    # Entry widget
    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)
    
    root.mainloop()


# PCPP 3.2: Grid Layout Manager
def create_grid_layout() -> None:
    """PCPP 3.2: Demonstrate grid layout manager."""
    root = tk.Tk()
    root.title("Grid Layout")
    
    # Create widgets
    tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    name_entry = tk.Entry(root, width=20)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    email_entry = tk.Entry(root, width=20)
    email_entry.grid(row=1, column=1, padx=5, pady=5)
    
    submit_btn = tk.Button(root, text="Submit", command=lambda: print("Submitted"))
    submit_btn.grid(row=2, column=0, columnspan=2, pady=10)
    
    root.mainloop()


# PCPP 3.3: Event Handling
def create_event_demo() -> None:
    """PCPP 3.3: Demonstrate event handling."""
    root = tk.Tk()
    root.title("Event Handling")
    
    def on_button_click() -> None:
        """Button click handler."""
        messagebox.showinfo("Info", "Button clicked!")
    
    def on_key_press(event: tk.Event) -> None:
        """Key press handler."""
        print(f"Key pressed: {event.char}")
    
    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=10)
    
    entry = tk.Entry(root)
    entry.pack(pady=10)
    entry.bind("<Key>", on_key_press)
    entry.bind("<Return>", lambda e: print("Enter pressed"))
    
    root.mainloop()


# PCPP 3.3: Observable Variables
def create_observable_variables() -> None:
    """PCPP 3.3: Demonstrate observable variables."""
    root = tk.Tk()
    root.title("Observable Variables")
    
    # Create observable variables
    text_var = tk.StringVar(value="Initial value")
    int_var = tk.IntVar(value=0)
    
    # Widgets linked to variables
    entry = tk.Entry(root, textvariable=text_var, width=20)
    entry.pack(pady=10)
    
    label = tk.Label(root, textvariable=text_var)
    label.pack(pady=5)
    
    # Variable tracer
    def on_change(*args: object) -> None:
        print(f"Variable changed to: {text_var.get()}")
    
    text_var.trace('w', on_change)
    
    # Radio buttons with IntVar
    tk.Radiobutton(root, text="Option 1", variable=int_var, value=1).pack()
    tk.Radiobutton(root, text="Option 2", variable=int_var, value=2).pack()
    
    def show_selection() -> None:
        print(f"Selected: {int_var.get()}")
    
    tk.Button(root, text="Show Selection", command=show_selection).pack(pady=10)
    
    root.mainloop()


# PCPP 3.2: Frame widget and destroy()
def create_frame_and_destroy_demo() -> None:
    """PCPP 3.2: Frame for grouping; destroy() to close window."""
    root = tk.Tk()
    root.title("Frame and Destroy Demo")
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()
    tk.Label(frame, text="Widgets inside a Frame").pack()
    tk.Button(frame, text="Close", command=root.destroy).pack(pady=5)  # destroy() closes window
    root.mainloop()


# PCPP 3.2/3.3: Dialog boxes (messagebox), RGB/HEX colors
def create_dialog_demo() -> None:
    """PCPP 3.2: Dialog boxes - messagebox for user interaction."""
    root = tk.Tk()
    root.title("Dialog Demo")
    tk.Button(root, text="Show Info", command=lambda: messagebox.showinfo("Title", "Info message")).pack(pady=5)
    tk.Button(root, text="Ask Yes/No", command=lambda: messagebox.askyesno("Title", "Yes or No?")).pack(pady=5)
    root.mainloop()


# PCPP 3.2: Canvas Widget (RGB/HEX colors)
def create_canvas_demo() -> None:
    """PCPP 3.2: Demonstrate Canvas widget; PCPP 3.3: color modes RGB, HEX."""
    root = tk.Tk()
    root.title("Canvas Demo")
    
    # bg: color by name or HEX (e.g. '#ffffff' = white)
    canvas = tk.Canvas(root, width=400, height=300, bg="#ffffff")
    canvas.pack(pady=10)
    
    # Draw shapes - fill with color names or HEX (RGB as hex: #RRGGBB)
    canvas.create_rectangle(50, 50, 150, 100, fill="blue")
    canvas.create_oval(200, 50, 300, 150, fill="#ff0000")  # HEX red
    canvas.create_oval(250, 100, 350, 200, fill="#00ff00")  # HEX green
    canvas.create_line(50, 200, 350, 200, width=3)
    canvas.create_text(200, 250, text="Canvas Drawing", font=("Arial", 16))
    
    root.mainloop()


if __name__ == "__main__":
    # Uncomment to run demos:
    # create_basic_window()
    # create_grid_layout()
    # create_event_demo()
    # create_observable_variables()
    # create_canvas_demo()
    print("GUI demos ready - uncomment to run!")
