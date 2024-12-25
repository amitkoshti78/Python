import tkinter as tk


def button_click(event, text_var, entry):
    text_var.set(f"Hello, World! {entry.get()}")

def main():
    root = tk.Tk()
    root.title("Sample Tkinter Window")
    root.geometry("1000x1000")
    root.resizable(True, True)

    # Create a Text widget
    text_widget = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 16))
    text_widget.grid(row=0, column=0, sticky="nsew")

    # Create a vertical scrollbar
    v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
    v_scrollbar.grid(row=0, column=1, sticky="ns")

    # Create a horizontal scrollbar
    h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=text_widget.xview)
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    # Configure the Text widget to use the scrollbars
    text_widget.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Make sure the grid cells expand with the window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    text_var = tk.StringVar()
    label = tk.Label(root, textvariable=text_var)
    label.grid(row=2, column=0, pady=20)

    entry = tk.Entry(root)
    entry.grid(row=3, column=0, pady=10)

    button = tk.Button(root, text="Press me!")
    button.grid(row=4, column=0, pady=10)
    button.bind("<Button-1>", lambda event: button_click(event, text_var, entry))

    button_close = tk.Button(root, text="Close", command=root.quit)
    button_close.grid(row=5, column=0, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()