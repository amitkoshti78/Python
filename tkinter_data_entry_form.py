
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry
import os

def enter_data():
    pass

root = tk.Tk()
root.title("Data Entry Form")
root.geometry("800x600+500+200")

frame = tk.Frame(root)
frame.pack()

## >Personal info frame
personal_info_frame = ttk.LabelFrame(frame, text="Personal Information")
personal_info_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)


first_name_label = tk.Label(personal_info_frame, text="First Name")
first_name_label.grid(row=0, column=0) 


last_name_lable = tk.Label(personal_info_frame, text="Last Name")
last_name_lable.grid(row=0, column=1) 

title_label = tk.Label(personal_info_frame, text="Title")
title_label.grid(row=0, column=2)

first_name_entry = tk.Entry(personal_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = tk.Entry(personal_info_frame) 
last_name_entry.grid(row=1, column=1)

title_combobox = ttk.Combobox(personal_info_frame, values=["Mr.", "Mrs.", "Ms."])
title_combobox.grid(row=1, column=2)

dob_label = tk.Label(personal_info_frame, text="DOB")
dob_label.grid(row=0, column=3)

cal = DateEntry(personal_info_frame, selectmode = 'day', year = 2025, month = 2, day = 19)
cal.grid(row=1, column=3)

for widget in personal_info_frame.winfo_children():
    widget.grid(padx=5, pady=5) 

## Contact info frame
contact_info_frame = ttk.LabelFrame(frame, text="Contact Information")
contact_info_frame.grid(row=1, column=0, sticky="nesw", padx=20, pady=10)  

email_label = tk.Label(contact_info_frame, text="Email")
email_label.grid(row=0, column=0)

email_entry = tk.Entry(contact_info_frame)
email_entry.grid(row=1, column=0)

phone_label = tk.Label(contact_info_frame, text="Phone")
phone_label.grid(row=0, column=1)

phone_entry = tk.Entry(contact_info_frame)
phone_entry.grid(row=1, column=1)

### Address info frame
address_frame = ttk.LabelFrame(contact_info_frame, text="Address")
address_frame.grid(row=2, column=0, rowspan=1, columnspan=2, sticky="nesw", padx=20, pady=10)  

address_label = tk.Label(address_frame, text="Enter Address")
address_label.grid(row=0,column=0)

address_text = tk.Text(address_frame, width=40, height=3)
address_text.grid(row=0, column=1, padx=20, pady=5)

for widget in contact_info_frame.winfo_children():
    widget.grid(padx=5, pady=5)


## Course info frame
course_frame = ttk.LabelFrame(frame, text="Course Details")
course_frame.grid(row=2, column=0, sticky="nesw", padx=20, pady=10)  

course_label = tk.Label(course_frame, text="Select Course")
course_label.grid(row=0, column=0)

course_combobox = ttk.Combobox(course_frame, values=["FE", "SE", "TE", "BE"])
course_combobox.grid(row=1, column=0)

sub1_label = tk.Label(course_frame, text="Subject 1")
sub1_label.grid(row=0, column=1)

sub1_entry = tk.Entry(course_frame)
sub1_entry.grid(row=1, column=1)

sub2_label = tk.Label(course_frame, text="Subject 2")
sub2_label.grid(row=0, column=2)

sub2_entry = tk.Entry(course_frame)
sub2_entry.grid(row=1, column=2)

sub3_label = tk.Label(course_frame, text="Subject 3")
sub3_label.grid(row=0, column=3)

sub3_entry = tk.Entry(course_frame)
sub3_entry.grid(row=1, column=3)

for widget in course_frame.winfo_children():
    widget.grid(padx=5, pady=5)

terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

registered_var = tk.StringVar(value="Not Rigistered")
registered_check = tk.Checkbutton(terms_frame, text= "I would like to register for above course.",
                                  variable=registered_var, onvalue="Registered", offvalue="Not Registered")
registered_check.grid(row=0, column=0)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=1, column=0)

for widget in terms_frame.winfo_children():
    widget.grid(padx=5, pady=5)

# Button
button = tk.Button(frame, text="Enter data", command= enter_data)
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

root.mainloop()