import tkinter as tk

root_window = tk.Tk()
root_window.title("Data Entry Form")
root_window.geometry("600x600+500+100")

frame = tk.Frame(root_window, bd=20, bg="lightblue")
frame.pack(padx=10, pady=10)

personal_info_frame = tk.LabelFrame(frame,text="Personal Information", bg="lightgrey")
personal_info_frame.grid(row=0,column=0) #sticky="nsew",padx=20,pady=10)

first_name_lable = tk.Label(personal_info_frame, text="First Name")
first_name_lable.grid(row=0,column=0) 

first_name_entry = tk.Entry(personal_info_frame)
first_name_entry.grid(row=1,column=0)

last_name_lable = tk.Label(personal_info_frame, text="Last Name")
last_name_lable.grid(row=0,column=1) 

last_name_entry = tk.Entry(personal_info_frame)
last_name_entry.grid(row=1,column=1)

for widget in personal_info_frame.winfo_children():
    widget.grid(padx=10,pady=10)

contact_info_frame = tk.LabelFrame(frame,text="Contact Information", bg="lightgrey")
contact_info_frame.grid(row=1, column=0, padx=10, pady=10)

email_label = tk.Label(contact_info_frame, text="Email")
email_label.grid(row=0, column=0)

email_entry = tk.Entry(contact_info_frame)
email_entry.grid(row=1,column=0)

phone_label = tk.Label(contact_info_frame, text="Phone")
phone_label.grid(row=0,column=1)

phone_entry = tk.Entry(contact_info_frame)
phone_entry.grid(row=1,column=1)

for widget in contact_info_frame.winfo_children():
    widget.grid(padx=10,pady=10)

root_window.mainloop()