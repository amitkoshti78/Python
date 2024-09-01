def fun_output(result):
    print (f"The final answer is {result}")
    
if __name__ == '__main__' :
    print("inside output doing nothing", __name__)
else:
    print("Inside output : ", __name__)