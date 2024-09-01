def fun_input():
    number1 = float(input("Enter Number : "))
    operator = input("Enter operator + - * / % ** : ")
    number2 = float(input("Enter Number : "))
    return number1, number2, operator


if __name__ == '__main__' :
    print("Inside input doing nothing", __name__)
    pass
else:
    print("Inside input : ", __name__)