import tkinter as tk
from tkinter import ttk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tabbed Interface Example")
    root.geometry("400x300")

    # Create a notebook (tabbed interface)
    notebook = ttk.Notebook(root)

    # Create frames for each tab
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)

    # Add tabs to the notebook
    notebook.add(tab1, text="Tab 1")
    notebook.add(tab2, text="Tab 2")

    # Add widgets to Tab 1
    label1 = ttk.Label(tab1, text="This is Tab 1")
    label1.pack(padx=20, pady=20)

    button1 = ttk.Button(tab1, text="Press Me")
    button1.pack(pady=10)

    # Add widgets to Tab 2
    label2 = ttk.Label(tab2, text="This is Tab 2")
    label2.pack(padx=20, pady=20)

    entry2 = ttk.Entry(tab2)
    entry2.pack(pady=10)

    # Pack the notebook into the main window
    notebook.pack(expand=True, fill='both')

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
