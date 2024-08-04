# list is nothing but array(in c or c++) of items.
# a list can have different values like numbers, characters, strings

student_info = [101, "Janhvi", 89, 94, 87, "A"]
#index           0      1      2    3   4   5

# list elements can be retrived by using its index
name = student_info[1]
grade = student_info[5]

print("\n Name = ", name, "& Grade = ", grade)

square_of_number = [25, 81, 49, 16, 1, 100, 9, 64, 4, 36] 
#                    0  1  2   3  4    5   6   7   8   9
#                                             -3  -2  -1    

# append method is used to add elelemt or list of elements at the end 
square_of_number.append(121)
print("\n New list after append :", square_of_number)

# extend method is used add list of elements at the end 
square_of_number.extend([144, 169, 225])
print("\n New list after extend :", square_of_number)

# replace 5th item with new value 200
square_of_number[5] = 200
print("\n Value of 5th element : ", square_of_number)

# replace 8th item with new value 225
square_of_number.insert(8,225)
print("\n Value of 8th element : ", square_of_number)

index = square_of_number.index(16)
print("\n Index of 16 in the list is : ", index)

# to remove the last element from the list
popped_item = square_of_number.pop()
print("\n Popped item is : ", popped_item, "\n List is :", square_of_number)

# to remove specific element from the list in this case 200 is removed
square_of_number.remove(200)
print("\n After Removing item 200 :" ,  square_of_number)

# #Queue = First in first out
# #Stack = last in last out

#[start:lenght:step]
# follwing for loop will print the every second number 
# starting from 3rd index till 10th index and
i = 3
for number in square_of_number[3:11:2]:
    
    print("\n element", i , " : ", number)
    i+=2
  
print("\n Original List  :" ,  square_of_number)  
  
# negative index can be used to access list from end 
print("\n Printing last with -1 number : " , square_of_number[-1], "\n")  
  
print("\n Printing second last with -2 number : " , square_of_number[-2], "\n")  

print("\n Printing 5th with -5 last number : " , square_of_number[-5], "\n")  

square_of_number[-5] = 1000
print("\n List with changed number at -5th position: " , square_of_number, "\n")  
print("\n Printing 5th last number : " , square_of_number[-5], "\n")  

# following for loop will print list in reverse order 
print("\n Printing in Reverse order : [", end = " ")
for number in square_of_number[::-1]:
    print(number, end= " ")
print("]")   

print("\n Original List  :" ,  square_of_number)  

print("\n Printing in Reverse every 2nd element with start index -3 : [", end = " ")
for number in square_of_number[-3::-2]:
    print(number, end= " ")
print("]")    

# to sort the list in asceding order                  
square_of_number.sort()
print("\n Sorted list in ascending order : ", square_of_number)

# to sort the list in descending order   
square_of_number.sort(reverse=True)
print("\n Sorted list in descending order : ", square_of_number)


fruits_list = ["Banana", "Apple", "Cherry", "Banana", "Apple", "Banana", "Banana" ]

print("\n List of fruits :", end=" ")
for fruit in fruits_list:
    print(fruit, end=" ")

print("\n\n enumerate function is used to return index and value ")
# enumerate function return the index and element from the list
print("\nIndex  Element")
for index, fruit in enumerate(fruits_list):
    print("\n" , index, "   ", fruit)
 
# if condition can be used to check if element is present in list or not
print("\n\n Checking mango is available in fruits_list ")        
if "Mango" in fruits_list:
    print("\n Mango is available means present in list")
else:
    print("\n Mango Sold out means not present in list")

# count method is used to count number of occurences of an item in the list
banana_count = fruits_list.count("Banana")
print("\n Banana occuers : ", banana_count, "times")


    
# # tuple are read only
tuple_numbers = (89,3,10,4,2,10,5,6,1,7,89,3,10)
print("\n Tuple is immutable ", tuple_numbers)

number = tuple_numbers[3]
print("\n 3rd element of a tuple is : " , number)

number = tuple_numbers[-5]
print("\n 5th last element of a tuple is : " , number)

# following will result in error as we can not change, add, remove, sort on tuple
# tuple_numbers[3] = 100

print("\nPrinting tuple index and elelement using enumerate function\n")
for index, number in enumerate(tuple_numbers):
    print(index, ":", number)
 
# as stated earlier lists are mutable and tuples are immutable data structures in python     
def fun_sum(list_number):
    sum = 0
    #try the code with uncommenting the below line and check what happens
    #list_number[3] = 100 
    for number in list_number:
        sum = sum + number
        
    return sum

# calling sum function using list 
add_num = fun_sum([1,2,3,4,5])
print("\n\n Sum of 5 numbers in set is :", add_num , "\n")

# calling sum function using tuple
add_num = fun_sum((1,2,3,4,5))
print("\n Sum of 5 numbers in tuple is :", add_num, "\n\n")



