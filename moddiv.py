def fun_div(number1=0, number2=1, operator='/'):
    if operator == '/':
        div = number1 / number2
        return div
    else:
        return f"Invalid operator {operator}"
    
if __name__ == '__main__' :
    print("inside div doing nothing", __name__)
else:
    print("Inside div : ", __name__)