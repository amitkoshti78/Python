def fun_mul(number1=0, number2=0, operator='*'):
    if operator == '*':
        mult = number1 * number2
        return mult
    else:
        return f"Invalid operator {operator}"
    
if __name__ == '__main__' :
    print("inside mult doing nothing", __name__)
else:
    print("Inside mult : ", __name__)