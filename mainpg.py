
from modinput import fun_input
from modadd import fun_add

def fun_sub(num1, num2):
    pass

def fun_mul(num1, num2):
    pass

def fun_div(num1, num2):
    pass

def fun_output(result):
    print("Result is ", result)

def main():
    num1, num2, oper = fun_input()
    print(num1, num2, oper)
    result = 0
    match oper:
        case '+':
            result = fun_add(number1=num1, number2=num2, operator=oper)
        case '-':
            result = fun_sub(num1, num2)  
        
        case '*':
            result = fun_mul(num1, num2)
        case '/':
            result = fun_div(num1, num2) 
    
    print(result)        
    fun_output(result)
    
if __name__ == '__main__' :
    print("inside main")
    main()