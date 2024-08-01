# create a empty list
square_list = []

# for loop to add square of first 20 numbers to list
for element in range(1,21):
    square_list.append(element * element)

print(f'\nList of squares{square_list}')

# clear/empty the list
square_list.clear()

print(f'\nEmpty List {square_list}')

# Generator Expression to create a list of squares for first 20 numbers
# where element/number is divisible by 4
#              varaible/expression  for loop                    if condition
square_list = [element * element   for element in range(1,21) if element % 4 == 0]

print(f'\nList of squares{square_list}')
      
# create a matrix of 3*3 i.e. list of lists.
matirx_list = []
for i in range(1,4):     
    row_list = []
    for row in range(1,4):      
        row_list.append(row * i)   

    print(f'\n Row {i} : {row_list}')
    matirx_list.append(row_list)

print(f'\n Matrix List {matirx_list}')

matirx_list = [ [row * i for row in range(1,4)] for i in range(1,4)]
print(f'\n Matrix List {matirx_list}')

# create a tuple. Tuple is immutable object.
my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(f'\n Tuple {my_tuple}')

# Generator Expression to create tuple of square numbers
my_tuple1 = tuple(number * number for number in range(1,11))
print(f'\n Tuple {my_tuple1}')


# math is a package/librarary in python for mathematical functions.
# from this math package, pi is imported into our program so that we 
# use  the value of pi to calculate the radius of a circle

from math import pi 

print("\n", pi)

# creating a empty set
circle_area_set = set()

# variables to set the range of values
range_from = 3
range_to = 8

# for loop to create a set of radius of circles form 3 cm to 7 cm radius
for r in range(range_from,range_to): 
    circle_area_set.add((r ** 2) * pi)

print(f'\n Area of cirlcle {circle_area_set}')

# Generator Expression to create set of radius of circles from 3 cm to 7 cm radius
circle_area_set = {(r ** 2) * pi for r in range(range_from,range_to) }
print(f'\n Area of cirlcle {circle_area_set}')

# Generator Expression to create set of radius of circles from 3 cm to 7 cm radius 
# using set function
circle_area_set = set((r ** 2) * pi for r in range(range_from,range_to))
print(f'\n Area of cirlcle {circle_area_set}')


# to create a disctionary of litre:price (key:value) from 1 litre to 30 litre of petrol.
#  key : value
# litre: price 
#{  1  : 103.44
#   2  : 206.88
#   3  : 310.32
#   .....
#   29 : 2999.7599999999998
#   30 : 3103.2    
#}
petrol_price = 103.44
range_from = 1
range_to = 31

# create a empty dictionary
amount_tobe_paid = {}   

# for loop to add key and value pair of litre:price to dictionary 
for litre in range(range_from, range_to): 
                   # {key  :      value}
    amount_tobe_paid[litre] = petrol_price * litre

print(f'\n Amount to be paid : {amount_tobe_paid}')

# Generator expression to create a dictonary of litre:price (key:value) pairs 
# from 1 litre to 30 litres of petrol
amount_tobe_paid = {litre : petrol_price * litre for litre in range(1, 31)}
                      
amount_tobe_paid = {litre : petrol_price * litre for litre in range(range_from, range_to ) }
print(f'\n Amount to be paid : {amount_tobe_paid}')

# it is list of various sets 
#                 0         1                     2                   3
list_of_sets = [{1,2,3}, {8,1,2,4,6,0,7,9,3}, {"Amit", "Koshti"}, {'A', 'B', 'C'}]
print(f'\n List of sets : {list_of_sets}')

set1 = list_of_sets[2]
print(f'\n List of set1 : {set1}')

for element in list_of_sets[3]:
    print(f'\n Element of 4th set : {element}')
  
# to retirve value of third element from the list. 
# This value is nothing but a set {'A', 'B', 'C'} 
# pop method on set is used to remove an item from the set.  
set3 = list_of_sets[3] 
print(f'\n Set3 before pop: {set3}')
print(f'\npopped item : {set3.pop()}')
print(f'\n Set3 after pop : {set3}')

set2 = list_of_sets[1]
print(f'\n Set2 before pop: {set2}')
print(f'\npopped item : {set2.pop()}')
print(f'\n Set2 after pop : {set2}')

# list containing 3 tuples
list_of_tuple = [(1,2,3), (1,4,6),(1,8,18)]
print(f'\n List of tuples : {list_of_tuple}')

tuple1 = list_of_tuple[2]
print(tuple1)

