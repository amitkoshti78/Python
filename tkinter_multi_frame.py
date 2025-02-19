import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Frames Example")
root.geometry("400x300")

# Frame 1 with border
frame1 = tk.Frame(root, bd=2, relief=tk.SOLID, width=400, height=150)
frame1.pack_propagate(False)  # Prevent frame from resizing to its children
frame1.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

# Labels, entries, and buttons in Frame 1
label1 = tk.Label(frame1, text="Enter your name:")
label1.pack(pady=5)

entry1 = tk.Entry(frame1)
entry1.pack(pady=5)

button1 = tk.Button(frame1, text="Submit", command=lambda: print(f"Hello, {entry1.get()}"))
button1.pack(pady=5)

# Frame 2 with border
frame2 = tk.Frame(root, bd=2, relief=tk.SOLID, width=400, height=150)
frame2.pack_propagate(False)  # Prevent frame from resizing to its children
frame2.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

# Labels, entries, and buttons in Frame 2
label2 = tk.Label(frame2, text="Enter your age:")
label2.pack(pady=5)

entry2 = tk.Entry(frame2)
entry2.pack(pady=5)

button2 = tk.Button(frame2, text="Submit", command=lambda: print(f"Age: {entry2.get()}"))
button2.pack(pady=5)

# Run the application
root.mainloop()
