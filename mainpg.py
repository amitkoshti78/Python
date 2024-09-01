
from modinput import fun_input
from modadd   import fun_add
from modsub   import fun_sub
from modmult  import fun_mul
from moddiv   import fun_div
from modout   import fun_output

def main():
    num1, num2, oper = fun_input()
    
    print(num1, num2, oper)
    
    result = 0
    match oper:
        case '+':
            result = fun_add(number1=num1, number2=num2, operator=oper)
            
        case '-':
            result = fun_sub(number1=num1, number2=num2, operator=oper) 
        
        case '*':
            result = fun_mul(number1=num1, number2=num2, operator=oper)
            
        case '/':
            result = fun_div(number1=num1, number2=num2, operator=oper)
          
    fun_output(result)
    
if __name__ == '__main__' :
    print("inside main")
    main()