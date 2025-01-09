import csv

def read_csv_file(filename):
        try:
            with open(filename, mode='r') as rd_file:
                records = csv.reader(rd_file)   
                for row in records:
                    print(row)
        except FileNotFoundError:
            print("Error File not found")
        except Exception as err:
            print(f"Error {err} has occurred while reading {filename}")

def write_csv_file(filename, records):
        try:
            with open(filename, mode='w', newline='\n') as wr_file:
                write_records = csv.writer(wr_file)
                write_records.writerows(records)
        except Exception as err:
            print(f"Error {err} has occurred while writing {filename}")

def append_csv_file(filename, record):
        try:
            with open(filename, mode='a', newline='\n') as ap_file:
                app_record = csv.writer(ap_file)
                app_record.writerow(record)
        except Exception as err:
            print(f"Error {err} has occurred while writing {filename}")

def read_dict_csv_file(filename):
        try:
            with open(filename, mode='r') as rd_file:
                records = csv.DictReader(rd_file)
                for row in records:
                    print(row)

        except FileNotFoundError:
            print("Error File not found")
        except Exception as err:
            print(f"Error {err} has occurred while reading {filename}")

def write_dict_csv_file(filename, records, column_names):
        try:
            with open(filename, mode='w', newline='\n') as wr_file:
                write_records = csv.DictWriter(wr_file, fieldnames=column_names)
                write_records.writeheader()
                write_records.writerows(records)

        except Exception as err:
            print(f"Error {err} has occurred while writing {filename}")


if __name__ == '__main__':
        file_name = 'Employee.csv'
        employees = [
            ["Swapnil", "Manager", 55000],
            ["Ulhas", "Developer", 60000],
            ["Naveen", "Designer", 50000]
        ]

        write_csv_file(file_name, employees)

        read_csv_file(file_name)

        employee =  ["Ashish", "Data Analyst", 65000]
        append_csv_file(file_name, employee)

        file_name = 'Employee_header.csv'
        column_names = ["Name", "Position", "Salary"]
        employees = [
            {"Name": "Vinay", "Position": "Scrum Master", "Salary": 55000},
            {"Name": "Sujit", "Position": "Python Developer", "Salary": 60000},
            {"Name": "Mandar", "Position": "Web Designer", "Salary": 50000}
        ]

        write_dict_csv_file(file_name, employees, column_names)

        read_dict_csv_file(file_name)