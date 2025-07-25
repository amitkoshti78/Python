import tkinter as tk

def on_click(lable, entry, text_list, event=None):
    print("Button Clicked!")
    lable.config(text="Text Added!")
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)
    else:
        lable.config(text="Please Enter Text!")

def on_clear(lable, text_list):
    lable.config(text="List Cleared!")
    text_list.delete(0, tk.END)

#tk._test()

def main():
    root = tk.Tk()  
    root.title("My APP!")
    root.geometry("600x600")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = tk.Frame(root, bd=2, relief=tk.SOLID, width=400, height=150)
    frame.grid(row=0, column=0,  padx=10, pady=10)
    #frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    lable = tk.Label(frame, text="Hello World!")
    lable.grid(row=0, column=0)

    lable_list = tk.Label(frame, text="My List!")
    lable_list.grid(row=6, column=0)

    text_list = tk.Listbox(frame)
    text_list.grid(row=6, column=1)

    entry = tk.Entry(frame, width=40)
    entry.grid(row=0, column=1)
    entry.bind("<Return>", lambda event: on_click(lable, entry, text_list, event))

    add_button = tk.Button(frame, text="Add To List", fg="blue", command=lambda: on_click(lable, entry, text_list)) #, padx=50, pady=50, fg="blue", bg="red")
    add_button.grid(row=2, column=1)

    clear_button = tk.Button(frame, text="Clear List", fg="red", command=lambda: on_clear(lable, text_list))
    #, padx=50, pady=50, fg="blue", bg="red")
    clear_button.grid(row=8, column=1)

    close_button = tk.Button(frame, text="Close", fg="green", command=root.quit)
    close_button.grid(row=9, column=1)

    frame1 = tk.Frame(root, bd=2, relief=tk.SOLID, width=400, height=150)
    frame1.grid(row=1, column=0, padx=10, pady=10)
    #frame.rowconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=1)
    text_list = tk.Listbox(frame1)
    text_list.grid(row=6, column=1)

    root.mainloop()

if __name__ == "__main__":
    main()
