
name = "Amit" 

#'A'  'm'  'i'  't'
#       0123             [0]  [1]  [2]  [3]
print(id(name[0]))


for char in name:
    print(char)
    
    

for subscript in range(len(name)):
    print(subscript, name[subscript])