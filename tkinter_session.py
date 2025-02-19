import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def save_contact(name_entry, phone_entry):
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])

        try:
            with open(file_path, "w") as file_handle:
                file_handle.write(f"Name: {name}\nPhone: {phone}")
                messagebox.showinfo("Success", "Contact Saved Successfully!")
        except Exception as err:
            messagebox.showerror("Error", f"Error Saving File: {err}")
    else:
        messagebox.showwarning("Warning", "Please Enter Name and Phone Number!")

def main_window():

    window = tk.Tk()
    window.geometry('700x600+400+100')
    window.title('My Contact App')

    app_label = tk.Label(window, text='Welcome to My Contact App!', font=('Verdana', 24), fg='grey')
    app_label.pack(padx=20, pady=20)

    name_label = tk.Label(window, text='Enter Name:', font=('Verdana', 16), fg='grey')
    name_label.pack()
    name_entry = tk.Entry(window,font=('Verdana', 16), border=3, bg='grey', fg='white')
    name_entry.pack(padx=10,pady=10)


    phone_label=tk.Label(window,text='Enter Phone', font=('Verdana', 16), fg='grey')
    phone_label.pack()
    phone_entry = tk.Entry(window,font=('Verdana', 16), border=3, bg='grey', fg='white')
    phone_entry.pack()

    save_button = tk.Button(window,text="Save", command=lambda: save_contact(name_entry, phone_entry))
    save_button.pack(pady=20)

    close_button = tk.Button(window,text="Close", command=window.quit)
    close_button.pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    main_window()
