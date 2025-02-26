class Student:
    def __init__(self, name, age, marks, stream, college, year, branch, roll_no):  # student_1, name, age, marks
        self.name = name      # attributes
        self.age = age      # attributes
        self.marks = marks # attributes
        self.stream = stream
        self.college = college
        self.year = year
        self.branch = branch
        self.roll_no = roll_no

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}, Stream: {self.stream}, College: {self.college}, Year: {self.year}, Branch: {self.branch}, Roll No: {self.roll_no}"
    
    def update_year(self, new_year):
        self.year = new_year


student_1 = Student('Omkar', 19, 80, 'Science', 'XYZ', 'FE', 'Computer', '101')  # object
student_2 = Student('Swapnil', 19, 75, 'Science', 'ABC', 'SE', 'Electrical', '101')  # object

#print(student_1.name)
#print(student_2.name)


#print(student_1.college)
#print(student_2.college)

print(student_1.get_details())
print(student_2.get_details())

student_1.update_year('TE') # student_1.year = 'TE'
print(student_1.get_details())

'''student_3 = Student()
student_3.name = 'Monika'
student_3.age = 20
student_3.marks = 85
student_3.stream = 'Science'
student_3.college = 'PQR'
student_3.year = 'TE'
student_3.branch = 'Mechanical'
student_3.roll_no = '01'

print(student_3.get_details())'''



