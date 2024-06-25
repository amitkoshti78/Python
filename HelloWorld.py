
name = input("Enter the name : ")
print("\n Welcome",  name , "to my calulator!!! \n")

answer = "y"

while answer == ("y" or "Y"):

    number_a = float(input("\n Enter the first number : "))
    print(" 1st number : ", number_a) 

    number_b = float(input("\n Enter the second number : "))
    print(" 2nd number : ", number_b)

    operator = input("\n Enter the oprator '+ or - or * or / or % or **' : ")
    print(" Operator : ", operator)


    match operator:
        case "+" :
            result = number_a + number_b
        case "-" :
            result = number_a - number_b
        case "*" :
             result = number_a * number_b
        case "/" :
             result = round(number_a / number_b, 2)
        case "%" :
             result = number_a % number_b
        case "**" :
             result = number_a ** number_b

    print("\n Answer --> ", number_a , operator , number_b , "=" , result)
    answer = input("\n Do you want to continue y/n: ")

birthdate = input("Enter your birth date dd/mm/yyyy foramt: ")
#                                        0123456789
birth_day = birthdate[0:2]
birth_month = birthdate[3:5]
birth_year = birthdate[6:10]
print(birth_day, birth_month, birth_year )





