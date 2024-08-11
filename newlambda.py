def max_func(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2
    
maxnum = max_func(34,12)
print("\n Max number is using normal function : ", maxnum)

maxnum = lambda number1, number2 : number1 if number1 > number2 else number2
print("\n Max number is using lambda function : ", maxnum(50,74))


square_of_number = lambda number : number ** 2
print("\n Square of a number is using lambda function : ", square_of_number(12))

import math

radius_of_circle = [30.12, 45.14, 9.32, 41.0, 47.3, 67.23]

def area_circle_fun(radius):
    area = math.pi * radius ** 2
    return round(area,2)

area_of_circle = []
for radius in radius_of_circle:
    area_of_circle.append(area_circle_fun(radius))
    
print("\n Area of Circle list :", area_of_circle)

area = lambda radius: round(math.pi * radius ** 2, 2) 

area_of_circle.clear()

for radius in radius_of_circle:
    area_of_circle.append(area(radius))

print("\n Area of Circle list using lambda :", area_of_circle)

area_of_circle.clear()

area_of_circle = list(map(lambda radius: round(math.pi * radius ** 2, 2), radius_of_circle ))
print("\n Area of Circle list using map lambda :", area_of_circle)

number_list = [number for number in range(1,51)]
print("\n Number list : " , number_list)

square_of_number = lambda number : number * number

#                               funtion name              list/tuple/dict/set     
square_of_num = list(map(lambda number: number * number, number_list))
print("\n Using map lambda : " ,square_of_num)

def square_fun(number): 
    return number * number

square_num = square_fun(12)
print("\n Square of number : ", square_num)

number_list = [1,2,3,4,6]
square_of_num_1 = list(map(square_fun, number_list)) 
print("\n Using function call :" , square_of_num_1)  

square_of_num_2 = list(map(lambda number: number ** 2, number_list))  
print("\n Using lambda function call :" , square_of_num_2)  


