import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def save_data():
    print(f"Title :  {title_combobox.get()}")
    print(f"First Name :  {first_name_entry.get()}")
    print(f"Last Name :  {last_name_entry.get()}")
    print(f"Gender :  {gender_combobox.get()}")
    print(f"Date of Birth :  {dob_date.get()}")


root_window = tk.Tk()
root_window.title("Data Entry Form")
root_window.geometry("400x400+100+100")

main_frame = tk.Frame(root_window)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

v_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

h_scrollbar = ttk.Scrollbar(root_window, orient=tk.HORIZONTAL, command=canvas.xview)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

scrollbar_frame = tk.Frame(canvas)
canvas.create_window((0,0), window=scrollbar_frame, anchor="nw")


frame1 = tk.Frame(scrollbar_frame, bd=6, relief=tk.RAISED, bg="lightcyan")  # relief : flat, groove, raised, ridge, solid, or sunken
frame1.pack(padx=10, pady=10)

personal_info_frame = tk.LabelFrame(frame1,text="Personal Information", bg="lightgrey")
personal_info_frame.grid(row=0,column=0) #sticky="nsew",padx=20,pady=10)

title_label = tk.Label(personal_info_frame, text="Title")
title_label.grid(row=0,column=0)

title_combobox = ttk.Combobox(personal_info_frame, values=["Mr","Mrs","Miss"])
title_combobox.grid(row=1,column=0)

first_name_lable = tk.Label(personal_info_frame, text="First Name")
first_name_lable.grid(row=0,column=1) 

first_name_entry = tk.Entry(personal_info_frame)
first_name_entry.grid(row=1,column=1)

last_name_lable = tk.Label(personal_info_frame, text="Last Name")
last_name_lable.grid(row=0,column=2) 

last_name_entry = tk.Entry(personal_info_frame)
last_name_entry.grid(row=1,column=2)

gender_label = tk.Label(personal_info_frame, text="Gender")
gender_label.grid(row=2,column=0)

gender_combobox = ttk.Combobox(personal_info_frame, values=["Male", "Female"])
gender_combobox.grid(row=3,column=0)

dob_label = tk.Label(personal_info_frame, text="Date of Birth")
dob_label.grid(row=2,column=1)

dob_date = DateEntry(personal_info_frame, selectmode="day", year=2025, month=2, day=20)
dob_date.grid(row=3,column=1)


for widget in personal_info_frame.winfo_children():
    widget.grid(padx=10,pady=10)

contact_info_frame = tk.LabelFrame(frame1,text="Contact Information", bg="lightgrey")
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

frame2 = tk.Frame(scrollbar_frame, bd=6, relief=tk.SUNKEN, bg="lightgreen")  # relief : flat, groove, raised, ridge, solid, or sunken
frame2.pack(padx=10, pady=10)

address_frame = tk.LabelFrame(frame2,text="Address", bg="lightgrey", padx=10, pady=10)
address_frame.grid(row=0,column=0) #sticky="nsew",padx=20,pady=10)

street_label = tk.Label(address_frame, text="Street")
street_label.grid(row=0,column=0)

street_entry = tk.Entry(address_frame)
street_entry.grid(row=1,column=0)

house_no_label = tk.Label(address_frame, text="House No")
house_no_label.grid(row=0,column=1)

house_no_entry = tk.Entry(address_frame)
house_no_entry.grid(row=1,column=1)

pin_code_label = tk.Label(address_frame, text="Pin Code")
pin_code_label.grid(row=2,column=0)

pin_code_entry = tk.Entry(address_frame)
pin_code_entry.grid(row=3,column=0)

city_label = tk.Label(address_frame, text="City")
city_label.grid(row=2,column=1)

city_entry = tk.Entry(address_frame)
city_entry.grid(row=3,column=1)

for widget in address_frame.winfo_children():
    widget.grid(padx=10,pady=10)

frame3 = tk.Frame(scrollbar_frame, bd=6, relief=tk.RIDGE, bg="gold")  # relief : flat, groove, raised, ridge, solid, or sunken
frame3.pack(padx=10, pady=10)

course_frame = tk.LabelFrame(frame3,text="Courses", bg="lightgrey", padx=10, pady=10)
course_frame.grid(row=0,column=0) #sticky="nsew",padx=20,pady=10)

course_label = tk.Label(course_frame, text="Course Name")
course_label.grid(row=0,column=0)

course_name = ttk.Combobox(course_frame, values=["FE","SE","TE","BE"])
course_name.grid(row=1,column=0)

subject1_label = tk.Label(course_frame, text="Subject 1")
subject1_label.grid(row=0,column=1)

subject1_entry = tk.Entry(course_frame)
subject1_entry.grid(row=1,column=1)

subject2_label = tk.Label(course_frame, text="Subject 2")
subject2_label.grid(row=0,column=2)

subject2_entry = tk.Entry(course_frame)
subject2_entry.grid(row=1,column=2)

subject3_label = tk.Label(course_frame, text="Subject 3")
subject3_label.grid(row=0,column=3)

subject3_entry = tk.Entry(course_frame)
subject3_entry.grid(row=1,column=3)

for widget in course_frame.winfo_children():
    widget.grid(padx=10,pady=10)

frame4 = tk.Frame(scrollbar_frame, bd=6, relief=tk.RIDGE, bg="silver")  # relief : flat, groove, raised, ridge, solid, or sunken
frame4.pack(padx=10, pady=10)

action_frame = tk.LabelFrame(frame4,text="Press Button", bg="lightgrey", padx=10, pady=10)
action_frame.grid(row=0,column=0) #sticky="nsew",padx=20,pady=10)

save_button = tk.Button(action_frame, text="Save", command=lambda :save_data())
save_button.grid(row=0,column=0)

clear_button = tk.Button(action_frame, text="Clear", command=lambda :save_data())
clear_button.grid(row=0,column=0)

close_button = tk.Button(action_frame, text="Close", command=root_window.quit)
close_button.grid(row=0,column=5)

root_window.mainloop()