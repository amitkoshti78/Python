
def odd_even(n):
    return True if n % 2 == 0 else False

    
number1 = float(input("Enter Number : "))
operator = input("Enter operator + - * / % ** : ")
number2 = float(input("Enter Number : "))

match operator:
    case '+':
        result = number1 + number2

    case '-':
        result = number1 - number2

    case '*':
        result = number1 * number2

    case '/':
        result = number1 / number2
    
    case '**':
        result = number1 ** number2

    case '%':
        result = number1 % number2

print(f'{number1} {operator} {number2} =  {result:,.2f}' )

if odd_even(result):
    print("Even")
else:
    print("Odd")

month = int(input("Enter month : ")) 
match month:
    case 4 | 6 | 9 | 11 :
        print("Month ends on 30")
    case 1| 3 | 5| 7| 8 | 10 |12 :
        print("Month ends on 31")
    case 2:
        print("Month ends on 28 or 29")
    case _:
        print("Invalid Month")