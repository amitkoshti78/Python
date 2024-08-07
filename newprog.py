square_numbers = []
for i in range(1,11):
    if i % 2 == 0 :
        square_numbers.append(i ** 2) 
    
    
print("\n Square list :" ,  square_numbers)
square_numbers.clear()
#                 varible/expression   for loop             if condition
even_numbers = [   i               for i in range(1,21) ]

  
print("\n even list generator expression :" ,  even_numbers)
even_numbers = []
for i in range(1,21):   
#    if i % 2 == 0:
        even_numbers.append(i)    
        
        
print("\n even list using for loop:" ,  even_numbers)
#                   2 : 2 ** 2                  4                    4 % 2 == 0 
#                   2 : 4
                  
#                   4 : 4 ** 2
#                   4 : 16    
  
square_dict = {}                  
for i in range (1,21):
    if i % 2 == 0:
        square_dict[i] = i ** 2                  


print("\n Square list :" ,  square_dict)

print("\n",  square_dict[2])
#               variable/expression     for loop             if condtion
square_dict = {i : i            for i in range (1,51) if i % 3 == 0 }  
print("\n Square list :" ,  square_dict)


# square_dict = {
# #  key  value    
#     2 : 4         if i % 2 == 0 even numbers    even number :  square
#     4 : 16
#     6 : 36
#     8 : 64 ....
    
#     20: 400
# }

# dict_of_student {
#     key    value
#     101 : "Amit"
#     102 : "Omkar"
#     103 : "Janhvi"
# }

# dict_of_student[103]




