import csv
import tkinter as tk
from tkinter import filedialog

def open_csv_file(data):
    file_name = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_name:
         write_csv_file(file_name, data)
         read_csv_file(file_name)

def write_csv_file(file_name, data):
    try:
        with open(file_name, mode='w', newline='\n') as file_handle:
            writer = csv.writer(file_handle)
            writer.writerows(data)
    except Exception as e:
        print(f"Error while writing a file {e}")

def read_csv_file(file_name):
    try:
        with open(file_name, mode='r') as file_handle:
            reader = csv.reader(file_handle)
            entry.delete(0, tk.END)
            for row in reader:
              
                row = row + "\n"
                entry.insert(tk.END, row)
                
    except Exception as e:
        print(f"Error while reading a file {e}")
              
if __name__ == "__main__":
    data = [
        ['Name', 'Age', 'City'],     # row1
        ['John Doe', 33, 'New York'], # row2
        ['Jane Doe', 30, 'Chicago'], # row3
        ['Tom Smith', 45, 'Los Angeles'],
        ['Jen Smith', 40, 'Houston']
    ]

    #file_name = open_csv_file()

   

    window = tk.Tk()
    window.geometry("600x600")
    window.title("Open CSV File")

    entry = tk.Entry(window,font=('Arial', 14))
    entry.place(height=800,width=800 )
    entry.pack(padx=25,pady=25)

    open_button = tk.Button(window,text="Open CSV File",command=lambda : open_csv_file(data))
    open_button.pack(padx=35,pady=35)

    close_button = tk.Button(window,text="Close",command=window.destroy)
    close_button.pack(padx=35,pady=35)

    window.mainloop()