
def square_num(number):
    return number ** 2

square_of_num = square_num(5)

print("\n Square of number using function : ", square_of_num)

square_of_num = lambda number : number ** 2

print("\n Square of number using lambda : ", square_of_num(5))

area_of_cicle = lambda radius : radius * 3.14

print("\n Area of circle using lambda : ", area_of_cicle(5))

full_name = lambda fn, ln : fn.strip().title() + " "  + ln.strip().title()

print("\n Full name : " , full_name("aMiT", "kOsHtI"))

student_list = [ "Bangal Omkar",  "Koshti Amit", "Umbre Janhvi", "Marathe Neha", "Nikam Avinash"]

student_list.sort(key = lambda name: name.split(" ")[-1].lower())
print(student_list)