def fun_add(number1=0, number2=0, operator='+'):
    if operator == '+':
        addition = number1 + number2
        return addition
    else:
        return f"Invalid operator {operator}"
    
if __name__ == '__main__' :
    print("inside add doing nothing", __name__)
else:
    print("Inside add : ", __name__)