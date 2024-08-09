
def square_num(number):
    return number ** 2

square_of_num = square_num(5)

print("\n Square of number using function : ", square_of_num)

square_of_num = lambda number : number ** 2

print("\n Square of number using lambda : ", square_of_num(5))

area_of_cicle = lambda radius : radius * 3.14

print("\n Area of circle using lambda : ", area_of_cicle(5))

full_name = lambda fn, ln : fn.strip().title() + " "  + ln.strip().title()

print("\n Full name : " , full_name("   aMiT  ", "   kOsHtI  "))

student_list = [ "Bangal Omkar",  "Koshti amit", "Umbre Janhvi", "Marathe neha", "Nikam Avinash"]

student_list.sort(key = lambda name: name.split(" ")[1].lower())
print(student_list)

#map filter and reduce function in python

# area of a circle 
import math

 
def area_of_circle(radius): 
        return (math.pi * radius ** 2)
        
    
def cel_to_far(cel_temp):
    far_temp = (9/5) * cel_temp + 32
    return round(far_temp,2)

def cel_to_far_tuple(cel_temp_tuple):
    far_temp = (9/5) * cel_temp_tuple[1] + 32
    return (cel_temp_tuple[0], round(far_temp,2))

def main():
    radius_list = [10, 3.5, 6, 9.2, 8]
    area_list = []
    for radius in radius_list:
        area = area_of_circle(radius)
        area_list.append(area)

    print(f'\n Area of circle list using function : {area_list}')

# map function takes 2 arguments first is function and second is list)
    area_list.clear()
    area_list = list(map(area_of_circle, radius_list ))
    print(f'\n Area of circle list using map : {area_list}')
    
    area_list.clear()
    area_list = list(map(lambda radius : math.pi * radius ** 2, radius_list))
    print(f'\n Area of circle list using map and lambda : {area_list}')
    
    temp_list_cel = [("Delhi" , 38.5), ("Mumbai" , 31.2), ("Pune" , 28.1), ("Chennai" , 48.3), ("Kolkatta" , 25.9), ("Hydrabad" , 27.4) ]
    
    temp_list_far = []
 
    for temp_tuple in temp_list_cel:
        temp_in_far = cel_to_far(temp_tuple[1])
        temp_list_far.append((temp_tuple[0],temp_in_far))
    
    print("\n Temperature in Far using function : ", temp_list_far)
    
    temp_list_far.clear()
    temp_list_far = list(map(cel_to_far_tuple,temp_list_cel))
    print("\n Temperature in Far  using map function: ", temp_list_far)
    
    cel_to_far_lambda = lambda data: (data[0] , round((9/5) * data[1] + 32, 2) )   
    
    temp_list_far.clear()
    temp_list_far = list(map(cel_to_far_lambda,temp_list_cel))
    print("\n Temperature in Far using lambda : ", temp_list_far)
    
    number_list = [ i for i in range(1,51) ]
    number_list_GT25 = list(filter(lambda number: number > 25, number_list))
    print("List GT25: ", number_list_GT25, "\t Total number of Numbers GT 25 : ", len(number_list_GT25) )
    
    number_list_GT25 = []
    for number in range(1,51):
        if number > 25 :
            number_list_GT25.append(number)
            
    print("List GT25: ", number_list_GT25, "\t Total number of Numbers GT 25 : ", len(number_list_GT25) )
    
    marks_list = [90, 30, 21, 78, 35, 24, 65, 71, 43, 80, 82,44, 68, 73, 71, 70, 89, 40, 58, 52, 53, 57, 47, 55, 62, 77, 93]
    
    grade_A_plus = list(filter(lambda marks: marks >= 85, marks_list))
    
    grade_A = list(filter(lambda marks: marks >= 75 and marks < 85 , marks_list))
    
    grade_B_plus = list(filter(lambda marks: marks >= 60 and marks < 75, marks_list))
    
    grade_B = list(filter(lambda marks: marks >= 50 and marks < 60, marks_list))
    
    grade_C = list(filter(lambda marks: marks >= 40 and marks < 50, marks_list))
    
    grade_D = list(filter(lambda marks: marks < 40, marks_list))
    
    print("Grade A plus : ", grade_A_plus, "\tTotal Number of studentds in Grade A plus : ", len(grade_A_plus) )
    
    print("Grade A      : ", grade_A, "\tTotal Number of studentds in Grade A   : ", len(grade_A) )
    
    print("Grade B plus : ", grade_B_plus, "\tTotal Number of studentds in Grade B plus  : ", len(grade_B_plus) )
    
    print("Grade B      : ", grade_B, "\tTotal Number of studentds in Grade B   : ", len(grade_B) )
    
    print("Grade C      : ", grade_C, "\tTotal Number of studentds in Grade C   : ", len(grade_C) )
    
    print("Grade D      : ", grade_D, "\tTotal Number of studentds in Grade D   : ", len(grade_D) )
    
    marks_list = [90, 30, 21, 78, 35, 24, 65, 0, 71, 43, [], (), 80, 82,44, 68, 73, 71, 70 , '', 89, 40, 58, "", 52, 53, False, 57, 47, 0, 55, 62, 77, 93]
    
    final_marks_list = list(filter(None, marks_list))
    print("\n Final Marks List : ", final_marks_list)
    
    
main()