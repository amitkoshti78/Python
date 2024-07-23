

#to multiply string number of times
for i in range(1,6):
    print(i, (i * "#"))

print("\n")
# nested loops
for x in range(0,3):
    for y in range(0,3):
        print(f"({x}, {y})")

print("\n")
letter_list = ["A", "B", "C", "D"]
number_list = [1, 2, 3, 4]
repeat_list = [0] * 5

final_list = letter_list + number_list + repeat_list
print(final_list)
print("\nCount : " , final_list.count(0))

final_list = [letter_list, number_list, repeat_list]
print("\n")
print(final_list)

range_list = list(range(0,50,3))
print(range_list)

print("\n")
char_list = list("Python Programming")
print(char_list)

print("\n")
topper_list = ["Anurag", "Omakr", "Sakshi", "Tanvi", "Avinash", "Viraj"]
first, second, *other = topper_list
print("First : " , first)
print("Second : ", second)
print("Other : ", other)

print("\n")
first, *other, last = topper_list
print("First : " , first)
print("Last : ", last)
print("Other : ", other)

print("\n")
for index, name in enumerate(topper_list):
    print(index, name)

print("\n")
topper_list.append("Amit")
topper_list.insert(2, "Akshara")
topper_list.remove("Viraj")
print(topper_list)
topper_list1 = topper_list.copy()

print("\n")
print("Index for Tanvi" , topper_list.index("Tanvi"))

print("\n")
topper_list.extend("Hitesh")
print(topper_list)

print("\n")
topper_list.clear()
print(topper_list)
print(topper_list1)


# functuion parameters and scope of variables, enumerate, tuples, 
# boolean operations, __main__ , isdigit, not operator, lambda, regular expressions, sys.argv
# packages and functions like random, math, sort, map and filter function of lambda

print("\n")
number_list = [1, 4, 2, 3, 4, 5, 3, 4, 1]
print("Number 4 occurs " , number_list.count(4), "times")

# to eliminate duplicates from the list
number_list = [1, 4, 2, 3, 4, 5, 3, 4, 1]
# empty list to hold unique numbers, initially empty
unique_list = []  

# for loop to iterate through number_list one element at a time
# number variable will hold 1 number at a time from number_list
# checking if number is already exists in unique_list
# if number is not presnet in unique_list it will be appended to the list
# and if number is not presnet in unique_listnumber, it will be ignored 

for number in number_list:
    if number not in unique_list: 
      unique_list.append(number)

print(unique_list)

# sorted is a in built function to sort the list in ascending or descending order
print("\n")
number_list = [1, 4, 2, 3, 4, 5, 3, 4, 1]
sorted_list = sorted(number_list)
print(sorted_list)
sorted_list = sorted(number_list, reverse=True)
print(sorted_list)



# tuple are immutable means so we can not add or remove or modify items in the tuple

print("\n")
number_tuple = (3, 6, 7, 8, 9, 1, 5)
print("Tuple : " , number_tuple)
a,y,*other,z,v  = number_tuple
print(a,y,z,v) 
a = number_tuple[0]
print("Value in a is " , a)

print(f'\n Index  Value ')
for index, number in enumerate(number_tuple):
    print(f'   {index}      {number}')

#sets in python : sets are unordered list of items and we can not have duplicates in it
number_list1 = [1, 4, 2, 3, 4, 5, 3, 4, 1]
set1 = set(number_list1)
print("\n")
print("Set1 : ", set1)
number_list2 = [3, 6, 7, 8, 9, 1, 5]
set2 = set(number_list2)
print("Set2 : ", set2)


print("\n")
print("Union of set : " , set1 | set2)
print("Common Items in set i.e. Intersection : ",  set1 & set2)
print("Difference of set : " , set1 - set2)
print("Present in one but not in other : " , set1 ^ set2)



