
class Student:
    def __init__(self, first_name, last_name, roll_nr, stream, year):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_nr = roll_nr
        self.stream = stream
        self.year = year

    def get_info(self):
        return (f"First Name : {self.first_name} \n"
                f"Last Name  : {self.last_name} \n"
                f"Roll No    : {self.roll_nr} \n"
                f"Stream     : {self.stream} \n"
                f"Year       : {self.year} \n")

    def change_first_name(self,first_name):
        self.first_name = first_name


student_1 = Student('Mona', 'Lisa', 101, 'Computer', 'FE'  )
student_2 = Student('James', 'Bond', 102, 'Computer', 'FE'  )

print(student_1.roll_nr)
print(student_2.year)
print(Student)

print(Student.get_info(student_1))
print(student_2.get_info())

student_1.change_first_name("Monika")
print(student_1.get_info())


''' student_1.first_name = 'Mona'
student_1.lasts_name = 'Lisa'
student_1.roll_nr = 101
student_1.stream = 'Computer'
student_1.year = 'FE'

student_2.first_name = 'James'
student_2.lasts_name = 'Bond'
student_2.roll_nr = 102
student_2.stream = 'Computer'
student_2.year = 'FE'

print(student_1.first_name)
print(student_2.first_name)'''