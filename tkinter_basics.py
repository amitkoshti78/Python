import tkinter as tk
from tkinter import messagebox
import re

def on_save(name_entry, email_entry, phone_entry, address_entry, event=None):
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    
    with open("contacts.txt", "a") as file:
        file.write(f"{name}, {email}, {phone}, {address}\n")


    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def on_clear(name_entry, email_entry, phone_entry, address_entry, event=None):
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def validate_numeric(value):
    """Validate if the input value is numeric."""
    return (value.isdigit() and len(value) <= 10 ) or value == ""  # Allow empty input or digits only

def validate_characters(value):
    """Validate if the input value is numeric."""
    return value.isalpha() or value == ""  # Allow empty input or digits only


def validate_email_during_typing(value):
    """Allow typing of valid email characters and intermediate states."""
    if value == "":
        return True  # Allow empty input
    # Allow valid intermediate states
    pattern = r'^[a-zA-Z0-9._%+-]*@?[a-zA-Z0-9.-]*\.?[a-zA-Z]{0,}$'
    return re.match(pattern, value) is not None

def validate_email_final(value):
    """Check if the email is valid when completed."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, value) is not None

def on_focus_out(event):
    """Validate email on focus out."""
    value = email_entry.get()
    if value and not validate_email_final(value):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        email_entry.focus_set()  # Bring focus back to the entry widget

window = tk.Tk()
window.title("My APP!")
window.geometry("400x400")

name_lable = tk.Label(window, text="Name:")
name_lable.place(x=10, y=10)
#name_lable.pack(side=tk.TOP, anchor="nw")

vcmd_name = window.register(validate_characters)

name_entry = tk.Entry(window, validate="key", validatecommand=(vcmd_name, "%P"))
name_entry.place(x=75, y=10)
#name_entry.pack(side=tk.TOP, anchor="nw")



email_lable = tk.Label(window, text="Email:")
email_lable.place(x=10, y=50)
#email_lable.pack(side=tk.TOP, anchor="nw")

vcmd_email = window.register(validate_email_during_typing)

email_entry = tk.Entry(window, validate="key", validatecommand=(vcmd_email, "%P"))
email_entry.place(x=75, y=50)

# Bind the focus out event for final validation
email_entry.bind("<FocusOut>", on_focus_out)

phone_lable = tk.Label(window, text="Phone:")
phone_lable.place(x=10, y=90)

vcmd_phone =  window.register(validate_numeric)

phone_entry = tk.Entry(window, validate="key", validatecommand=(vcmd_phone, "%P"))
phone_entry.place(x=75, y=90)

address_lable = tk.Label(window, text="Address:")
address_lable.place(x=10, y=130)    

address_entry = tk.Entry(window)
address_entry.place(x=75, y=130)

save_button = tk.Button(window, text="Save", fg="blue", command=lambda : on_save(name_entry, email_entry, phone_entry, address_entry))
save_button.place(x=70, y=170 )

clear_button = tk.Button(window, text="Clear", fg="red", command=lambda : on_clear(name_entry, email_entry, phone_entry, address_entry))
clear_button.place(x=150, y=170)

close_button = tk.Button(window, text="Close", fg="green", command=window.quit)
close_button.place(x=230, y=170)

window.mainloop()


'''## Email Validation in Tkinter Using Regular Expressions
Let's break down the regular expressions used for email validation in the context of your query. We'll focus on the two regex patterns you've mentioned: one for validating during typing and another for validating when the email is finalized.

### 1. Regular Expression for Intermediate Email Validation

#### Pattern: regex
^[a-zA-Z0-9._%+-]*@?[a-zA-Z0-9.-]*\.?[a-zA-Z]{0,}$


#### Explanation:
- **`^`**: Asserts the start of the string.
- **`[a-zA-Z0-9._%+-]*`**: Matches zero or more characters that can be:
  - Lowercase letters (`a-z`)
  - Uppercase letters (`A-Z`)
  - Digits (`0-9`)
  - Special characters: dot (`.`), underscore (`_`), percent (`%`), plus (`+`), and hyphen (`-`).
  
  This part allows for the local part of the email (before the `@`) to be partially entered.

- **`@?`**: Matches zero or one `@` character. This allows users to type an email without having to enter the `@` symbol immediately.

- **`[a-zA-Z0-9.-]*`**: Matches zero or more characters that can be:
  - Lowercase letters, uppercase letters, digits
  - Special characters: dot (`.`) and hyphen (`-`).
  
  This part corresponds to the domain name of the email.

- **`\.?`**: Matches zero or one dot (`.`). This allows for partial domain entries.

- **`[a-zA-Z]{0,}$`**: Matches zero or more alphabetic characters at the end of the string. This part is used to allow for typing in the top-level domain (TLD) but does not enforce it yet.

- **`$`**: Asserts the end of the string.

### Summary
This regex pattern allows for typing valid email characters progressively, accommodating intermediate states like entering just before the `@`, after it, or even leaving parts blank. It provides flexibility during user input while still enforcing some structure.

### 2. Regular Expression for Final Email Validation

#### Pattern:
```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

#### Explanation:
- **`^`**: Asserts the start of the string.
  
- **`[a-zA-Z0-9._%+-]+`**: Matches one or more characters that can be:
  - Lowercase letters, uppercase letters, digits
  - Special characters: dot (`.`), underscore (`_`), percent (`%`), plus (`+`), and hyphen (`-`). 

  This part ensures that there is at least one character before the `@`.

- **`@`**: Matches exactly one `@`.

- **`[a-zA-Z0-9.-]+`**: Matches one or more characters that can be:
  - Lowercase letters, uppercase letters, digits
  - Special characters: dot (`.`) and hyphen (`-`). 

  This part ensures there is at least one character in the domain name.

- **`\.`**: Matches exactly one dot (`.`).

- **`[a-zA-Z]{2,}`**: Matches two or more alphabetic characters. This enforces that a valid top-level domain (like `.com`, `.org`, etc.) must be present.

- **`$`**: Asserts the end of the string.

### Summary
This regex pattern enforces a more strict structure for valid email addresses. It checks that there is a proper format with required components like a local part, an `@`, a domain name, and a valid TLD.

### Conclusion

Using these two regex patterns together allows for a flexible and user-friendly email entry experience in your Tkinter application. The first pattern provides real-time validation as users type, while the second pattern ensures that when they finish typing (on focus out), their input conforms to standard email formatting rules. This combination enhances usability by allowing partial inputs while still enforcing necessary validation rules when complete.

Citations:
[1] https://stackoverflow.com/questions/63721504/validate-email-in-entry-widget-content-more-than-once-tkinter
[2] https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
[3] https://www.geeksforgeeks.org/validating-entry-widget-in-python-tkinter/
[4] https://www.mailercheck.com/articles/email-validation-using-python
[5] https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
[6] https://uibakery.io/regex-library/email-regex-python '''

''' The window.register(...) method in Tkinter is a crucial feature that allows you to link Python functions with the Tcl interpreter, which is the underlying engine of Tkinter. Here’s a detailed explanation of how it works and why it’s important for input validation and other functionalities.
What is register()?
Purpose: The register() method is used to register a Python callable (function) so that it can be invoked from Tcl code. This is essential because Tkinter operates on top of Tcl/Tk, and any command that needs to be executed must be recognized by the Tcl interpreter.
Return Value: When you call window.register(function), it returns a string that represents the name of a Tcl command associated with the Python function. This string can then be used in various Tkinter options, such as validatecommand for Entry widgets.

How It Works
Binding Python Functions: When you register a function using register(), Tkinter creates a unique name for that function in the Tcl interpreter. This name acts as a bridge between Python and Tcl, allowing you to call the Python function from within Tcl scripts or commands.

Substitution Codes: The registered command can include substitution codes (like %P, %S, etc.) that Tkinter replaces with actual values at runtime. For example, %P represents the value of the Entry widget after an edit, which is useful for validation purposes.'''
