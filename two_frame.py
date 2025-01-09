import tkinter as tk
from tkinter import filedialog, Text

def load_file(text_area):
    """Load a file and display its content in the specified text area."""
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  # Clear previous content
            text_area.insert(tk.END, content)  # Insert new content

def create_frame(master, frame_label):
    """Create a frame with a label, load button, and text area."""
    frame = tk.Frame(master)
    
    label = tk.Label(frame, text=frame_label)
    label.grid(row=0, column=0, pady=10)

    text_area = Text(frame)
    text_area.grid(row=2, column=0, pady=10, sticky="nsew")

    load_button = tk.Button(frame, text="Load File", command=lambda: load_file(text_area))
    load_button.grid(row=1, column=0, pady=10)

    # Configure grid weights for proper resizing
    frame.grid_rowconfigure(2, weight=1)
    
    return frame

def main():
    """Main function to set up the Tkinter window and frames."""
    root = tk.Tk()
    root.title("Two Frames Example")
    root.geometry("800x400")

    # Create two frames using grid
    frame1 = create_frame(root, "Frame 1")
    frame2 = create_frame(root, "Frame 2")

    # Place frames in the grid
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2.grid(row=0, column=1, sticky="nsew")

    # Configure grid weights for proper resizing
    root.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand
    root.grid_columnconfigure(1, weight=1)  # Allow column 1 to expand

    # Ensure that rows can also expand if necessary
    root.grid_rowconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
