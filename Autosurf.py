import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser

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

def reset():
    """Reset the application to load a new file."""
    global urls, current_index
    urls = []
    current_index = 0
    btn_open_urls["state"] = "disabled"

# Initialize variables
urls = []
current_index = 0

# Create main window
root = tk.Tk()
root.title("Open URLs from TXT")
root.geometry("400x200")

# Create and place widgets
btn_load_file = tk.Button(root, text="Load TXT File", command=open_file, width=20)
btn_load_file.pack(pady=10)

btn_open_urls = tk.Button(root, text="Open Next URL", command=open_next_url, width=20, state="disabled")
btn_open_urls.pack(pady=10)

btn_reset = tk.Button(root, text="Reset", command=reset, width=20)
btn_reset.pack(pady=10)

# Run the application
root.mainloop()
