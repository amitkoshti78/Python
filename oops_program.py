class Student:
    
    #list variable to hold all objects of Student class
    all_students = []

    #attributes/properties
    # constructor : __init__ is used to initialize the attributes of the class
    def __init__(self, roll_number, first_name, last_name, age, marks, branch, year, college):
        self.roll_number = roll_number   #stud_1.roll_number = 101  stud_2.roll_number = 102
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marks = marks
        self.branch = branch
        self.year = year
        self.college = college
        # append/add the object to the list
        Student.all_students.append(self)

        #methods
    def change_year(self,new_year, new_roll_number):
        self.year = new_year
        self.roll_number = new_roll_number

    
    def __str__(self):
        return f"{self.roll_number}, {self.first_name}, {self.last_name}, {self.age}, {self.marks}, {self.branch}, {self.year}, {self.college}"    
    
    @classmethod
    def get_all_students(cls):
        return cls.all_students
 
    
stud_1= Student(101, "Omkar", "Bangal", 18, 9, "Computer", "FE", "IIIT") # stud_1 is an object/instance of Student class
stud_2 = Student(102, "Omkar", "Kollure", 18, 9, "Computer", "FE", "Moze")  # stud_2 is an object/instance of Student class

#print(stud_1.__dict__)
#print(stud_2.__dict__)

'''stud_3 = Student()
stud_3.roll_number = 103
stud_3.first_name = "Monika"
stud_3.last_name = "Kadam"
stud_3.age = 19
stud_3.marks = 9
stud_3.branch = "Electronics"
stud_3.year = "SE"
stud_3.college = "IIIT"'''

#stud_1.change_year("SE", 201)
#stud_2.change_year("SE", 202)

#Student.change_year(stud_1, "TE", 301)

#print(stud_1.__str__())

#print(stud_1)
#print(stud_2.__dict__)

#print(stud_1.last_name)
#print(stud_2.last_name)

for student in Student.get_all_students():
    print(student)



