def fun_sub(number1=0, number2=0, operator='-'):
    if operator == '-':
        subtract = number1 - number2
        return subtract
    else:
        return f"Invalid operator {operator}"
    
if __name__ == '__main__' :
    print("inside sub doing nothing", __name__)
else:
    print("Inside sub : ", __name__)