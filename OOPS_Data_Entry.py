import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")
        self.root.geometry("800x600+500+200")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.create_personal_info_frame()
        self.create_contact_info_frame()
        self.create_course_info_frame()
        self.create_terms_frame()
        self.create_submit_button()

    def create_personal_info_frame(self):
        personal_info_frame = ttk.LabelFrame(self.frame, text="Personal Information")
        personal_info_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)

        first_name_label = tk.Label(personal_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)

        last_name_label = tk.Label(personal_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)

        title_label = tk.Label(personal_info_frame, text="Title")
        title_label.grid(row=0, column=2)

        self.first_name_entry = tk.Entry(personal_info_frame)
        self.first_name_entry.grid(row=1, column=0)

        self.last_name_entry = tk.Entry(personal_info_frame)
        self.last_name_entry.grid(row=1, column=1)

        self.title_combobox = ttk.Combobox(personal_info_frame, values=["Mr.", "Mrs.", "Ms."])
        self.title_combobox.grid(row=1, column=2)

        dob_label = tk.Label(personal_info_frame, text="DOB")
        dob_label.grid(row=0, column=3)

        self.cal = DateEntry(personal_info_frame, selectmode='day', year=2025, month=2, day=19)
        self.cal.grid(row=1, column=3)

        for widget in personal_info_frame.winfo_children():
            widget.grid(padx=5, pady=5)

    def create_contact_info_frame(self):
        contact_info_frame = ttk.LabelFrame(self.frame, text="Contact Information")
        contact_info_frame.grid(row=1, column=0, sticky="nesw", padx=20, pady=10)

        email_label = tk.Label(contact_info_frame, text="Email")
        email_label.grid(row=0, column=0)

        self.email_entry = tk.Entry(contact_info_frame)
        self.email_entry.grid(row=1, column=0)

        phone_label = tk.Label(contact_info_frame, text="Phone")
        phone_label.grid(row=0, column=1)

        self.phone_entry = tk.Entry(contact_info_frame)
        self.phone_entry.grid(row=1, column=1)

        address_frame = ttk.LabelFrame(contact_info_frame, text="Address")
        address_frame.grid(row=2, column=0, rowspan=1, columnspan=2, sticky="nesw", padx=20, pady=10)

        address_label = tk.Label(address_frame, text="Enter Address")
        address_label.grid(row=0, column=0)

        self.address_text = tk.Text(address_frame, width=40, height=3)
        self.address_text.grid(row=0, column=1, padx=20, pady=5)

        for widget in contact_info_frame.winfo_children():
            widget.grid(padx=5, pady=5)

    def create_course_info_frame(self):
        course_frame = ttk.LabelFrame(self.frame, text="Course Details")
        course_frame.grid(row=2, column=0, sticky="nesw", padx=20, pady=10)

        course_label = tk.Label(course_frame, text="Select Course")
        course_label.grid(row=0, column=0)

        self.course_combobox = ttk.Combobox(course_frame, values=["FE", "SE", "TE", "BE"])
        self.course_combobox.grid(row=1, column=0)

        sub1_label = tk.Label(course_frame, text="Subject 1")
        sub1_label.grid(row=0, column=1)

        self.sub1_entry = tk.Entry(course_frame)
        self.sub1_entry.grid(row=1, column=1)

        sub2_label = tk.Label(course_frame, text="Subject 2")
        sub2_label.grid(row=0, column=2)

        self.sub2_entry = tk.Entry(course_frame)
        self.sub2_entry.grid(row=1, column=2)

      
        sub3_label = tk.Label(course_frame, text="Subject 3")
        sub3_label.grid(row=0, column=3)

        self.sub3_entry = tk.Entry(course_frame)
        self.sub3_entry.grid(row=1, column=3)

        for widget in course_frame.winfo_children():
            widget.grid(padx=5, pady=5)

    def create_terms_frame(self):
        terms_frame = tk.LabelFrame(self.frame, text="Terms & Conditions")
        terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        self.registered_var = tk.StringVar(value="Not Registered")
        registered_check = tk.Checkbutton(
            terms_frame, 
            text="I would like to register for above course.",
            variable=self.registered_var, 
            onvalue="Registered", 
            offvalue="Not Registered"
        )
        registered_check.grid(row=0, column=0)

        self.accept_var = tk.StringVar(value="Not Accepted")
        terms_check = tk.Checkbutton(
            terms_frame, 
            text="I accept the terms and conditions.",
            variable=self.accept_var, 
            onvalue="Accepted", 
            offvalue="Not Accepted"
        )
        terms_check.grid(row=1, column=0)

        for widget in terms_frame.winfo_children():
            widget.grid(padx=5, pady=5)

    def create_submit_button(self):
        button = tk.Button(self.frame, text="Enter data", command=self.enter_data)
        button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    def enter_data(self):
        # This method will handle the data entry logic
        # For now, it just prints the collected data to the console
        print("First Name:", self.first_name_entry.get())
        print("Last Name:", self.last_name_entry.get())
        print("Title:", self.title_combobox.get())
        print("DOB:", self.cal.get_date())
        print("Email:", self.email_entry.get())
        print("Phone:", self.phone_entry.get())
        print("Address:", self.address_text.get("1.0", tk.END).strip())
        print("Course:", self.course_combobox.get())
        print("Subject 1:", self.sub1_entry.get())
        print("Subject 2:", self.sub2_entry.get())
        print("Subject 3:", self.sub3_entry.get())
        print("Registered:", self.registered_var.get())
        print("Accepted Terms:", self.accept_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()