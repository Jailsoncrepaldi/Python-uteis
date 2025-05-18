import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import threading

def open_file():
    """Open a file dialog to select the TXT file and read URLs."""
    file_path = filedialog.askopenfilename(
        title="Select a TXT file",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                global urls
                urls = [line.strip() for line in file if line.strip()]
            if urls:
                btn_open_urls["state"] = "normal"
                btn_start_timer["state"] = "normal"
                messagebox.showinfo("Success", "URLs loaded successfully!")
            else:
                messagebox.showwarning("Warning", "The file is empty or invalid.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")

def open_next_url():
    """Open the next URL in the list."""
    global current_index
    if current_index < len(urls):
        webbrowser.open(urls[current_index])
        current_index += 1
    if current_index == len(urls):
        messagebox.showinfo("Done", "All URLs have been opened!")
        btn_open_urls["state"] = "disabled"
        btn_start_timer["state"] = "disabled"

def start_timer():
    """Start the timer to open URLs at intervals."""
    try:
        interval = int(entry_timer.get())
        if interval <= 0:
            raise ValueError("Interval must be a positive number.")
        btn_open_urls["state"] = "disabled"
        btn_start_timer["state"] = "disabled"
        threading.Thread(target=timer_loop, args=(interval,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for the timer interval.")

def timer_loop(interval):
    """Loop through the URLs and open them at specified intervals."""
    global current_index
    while current_index < len(urls):
        webbrowser.open(urls[current_index])
        current_index += 1
        root.after(interval * 1000)
    messagebox.showinfo("Done", "All URLs have been opened!")
    reset_buttons()

def reset_buttons():
    """Reset the buttons to allow loading a new file or manual opening."""
    btn_open_urls["state"] = "normal"
    btn_start_timer["state"] = "normal"

def reset():
    """Reset the application to load a new file."""
    global urls, current_index
    urls = []
    current_index = 0
    btn_open_urls["state"] = "disabled"
    btn_start_timer["state"] = "disabled"

# Initialize variables
urls = []
current_index = 0

# Create main window
root = tk.Tk()
root.title("Open URLs from TXT with Timer")
root.geometry("400x300")

# Create and place widgets
btn_load_file = tk.Button(root, text="Load TXT File", command=open_file, width=20)
btn_load_file.pack(pady=10)

btn_open_urls = tk.Button(root, text="Open Next URL", command=open_next_url, width=20, state="disabled")
btn_open_urls.pack(pady=10)

frame_timer = tk.Frame(root)
frame_timer.pack(pady=10)

lbl_timer = tk.Label(frame_timer, text="Timer Interval (seconds):")
lbl_timer.pack(side=tk.LEFT, padx=5)

entry_timer = tk.Entry(frame_timer, width=5)
entry_timer.pack(side=tk.LEFT, padx=5)

btn_start_timer = tk.Button(root, text="Start Timer", command=start_timer, width=20, state="disabled")
btn_start_timer.pack(pady=10)

btn_reset = tk.Button(root, text="Reset", command=reset, width=20)
btn_reset.pack(pady=10)

# Run the application
root.mainloop()