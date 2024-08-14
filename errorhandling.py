isnumeric_1 = "n"
isnumeric_2 = "n"
number1 = 0
number2 = 0
first_time = 1

try:
    number1 = int(input("Enter first number :"))
    
except ValueError:
    print("\n### Warning: Enter a valid Number ")
    isnumeric_1 = 'n'
else:
    isnumeric_1 = 'y'
    
try:
    number2 = int(input("Enter second number :"))
except ValueError:
    print("\n### Warning: Enter a valid Number ")
    isnumeric_2 = 'n'
else:
    isnumeric_2 = 'y'
    

while isnumeric_1 == 'n' or isnumeric_2 == 'n':

    if isnumeric_1 == 'n':
        try:
            number1 = int(input("Enter first number :"))
    
        except ValueError:
            print("\n### Warning:Enter a valid Number ")
            isnumeric_1 = 'n'
        else:
            isnumeric_1 = 'y'
  
    if isnumeric_2 == 'n':
        try:
            number2 = int(input("Enter second number :"))
        except ValueError:
            print("\n### Warning: Enter a valid Number ")
            isnumeric_2 = 'n'
        else:
            isnumeric_2 = 'y'
    
    if isnumeric_1 == 'y' and isnumeric_2 == 'y':
        break
    


add = number1 + number2
print("\n Addition is ", add) 
        



    
