# word_disct = {
#    # key    :   value 
#     "for"   : "for is a loop for repeating instructions in definite number of times",
#     "while" : "while is a loop for repeating instructions in ifinite number of times",
#     "if"    : "if is a condtional statement to decide the flow of a program",
   
# }

# print(word_disct["while"])
# print(word_disct["if"])
# print(word_disct["for"])

# print(word_disct)

# for key, value in word_disct.items():
#     print(key, ":" , value)
#    print(word_disct[key])  


# student_dict = {
#   # unique key  
#     101         : "Omkar B",
#     102         : "Omkar K",
#     103         : "Janhvi U",
#     104         : "Amit K"
# }

# student_dict["105"] = "Sakshi G"
# student_dict["Banana"] = "Yellow"
# student_dict["A"] = "Apple"

# print(student_dict)

# student_dict = {}
# student_list = ["Omkar", "Janhvi", "Amit", "Sakshi" ]
# roll_number = 101
# for student in student_list:
#     student_dict[roll_number] = student
#     roll_number += 1
    
# for roll_number, name in student_dict.items():
#     print("\n", roll_number, " : " , name)

sqaure_of_number_1 = {1, 2, 4, 9, 16, 25}
sqaure_of_number_2 = set([4, 9, 81,100, 144, 225, 4, 9, 100])

print(sqaure_of_number_2)

new_list = [4,9,81,100,144,225]
number_list = [4, 9, 81,100, 144, 225, 4, 9, 100]

for value in number_list:
    if not value in new_list: # check if number exists in a new list. True --> False   False --> True
        new_list.append(value)
    
        
        
print(new_list)
    

# print(sqaure_of_number_1 | sqaure_of_number_2) # union
# print(sqaure_of_number_1 & sqaure_of_number_2) # interstection
# print(sqaure_of_number_1 - sqaure_of_number_2) # difference 
# print(sqaure_of_number_2 - sqaure_of_number_1)
# print(sqaure_of_number_1 ^ sqaure_of_number_2) # symetric difference

