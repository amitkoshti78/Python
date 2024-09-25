class Student:
    def __init__(self, roll_num, first_name,last_name ):
        self.first_name = first_name
        self.roll_num = roll_num
        self.last_name = last_name

    def fun_get_values(self):
        return self.first_name, self.last_name, self.roll_num

    def fun_set_values(self, roll_num, first_name, last_name):
        self.roll_num = roll_num
        self.first_name = first_name
        self.last_name = last_name


student1 = Student(101, "Amit", "Koshti")

print(student1.fun_get_values())
student1.fun_set_values(102, "Omkar", "Bangal")
print(student1.fun_get_values())

class FY(Student):
    def __init__(self, roll_num, first_name, last_name, maths, phy, chem):
        super().__init__(roll_num, first_name, last_name)
        self.maths = maths
        self.phy = phy
        self.chem = chem

    def fun_get_marks(self):
        return self.first_name, self.last_name, self.roll_num, self.maths, self.phy, self.chem


FY_student1 = FY(101, "Amit", "Koshti", 78, 75, 79)
print(FY_student1.fun_get_values())
print(FY_student1.fun_get_marks())

FY_student1.roll_num = 202
FY_student1.first_name = "Omkar"
FY_student1.last_name = "Bangal"
print(FY_student1.fun_get_marks())


