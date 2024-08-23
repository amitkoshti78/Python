from typing import Final

x = 1             # global variable 0x567812345


'''def outer_fun():
    x  = 2             # local variable 0x333333333
    def middll_fun():
        x = 25
        def inner_fun():
            #global x
            nonlocal x
            #x = 3               # local varible 0x2345678
            print("inner function x and its adress : ", x, " --> ", hex(id(x)))
    
        inner_fun()     
        print("middle function x and its adress : ", x, " --> ", hex(id(x)))
    middll_fun()
    print("outer function x and its adress : ", x, " --> ", hex(id(x)))
outer_fun()    
print("global variable x and its adress: ", x, " --> ", hex(id(x)))

x = 2
print(x)
x = 3
print(x)'''

#PI = 3.14

""" class ConstantsNamespace():
    __slots__ = ()
    PI = 3.14159
    GRAVITY = 9.80665
    LIMIT = 10
    
constant = ConstantsNamespace()

#constant.PI = 100

def area(radius): 
    #constant.PI = 100
    return constant.PI * radius ** 2

#print("Area : " , area(5))

from enum import Enum

class MyConstants(Enum):
    MY_PI = 3.14
    MY_GRAVITY = 9.81
    MONTH = "May" """
    
#MyConstants.MY_PI = 100
#print(list(MyConstants))
    
# for number in range(1,constant.LIMIT)  :
#     print("x")
    
# for index in range(1,constant.LIMIT):
#     print("y")
    
# for subscript in range(1,constant.LIMIT):
#     print("z")

#MyConstants.MY_PI = 100

""" LEGB rule
Variable resolution in Python follows the LEGB rule. This means that the interpreter looks for a name in the following order:

Locals: Variables defined within the function body and not declared global.

Enclosing: Names in the local scope of all enclosing functions, from inner to outer.

Globals: Names defined at the top level of a module or declared global with the global keyword.

Built-in: Any built-in name in Python.

 """
 
#LEGB rule
""" from math import pi  # built in

pi = 100            # global
def outer_fun():
    pi = 200        #Enclosing
    def inner_fun():    
        pi = 300    #Enclosing
        def deep_inner_fun():
            pi = 400   #local
            print("Value of pi : ", pi)
        deep_inner_fun()
    inner_fun()
outer_fun()   """ 


x = 1

def sum_fun():
    global x
    print("Value of x inside function :", x)   
    x = x + 1


sum_fun()   
print("Value of x outside of function x :", x)  

def name_fun():
    name = "Amit"
    print(name) 
    
def myname_funct1():
    name = "Omkar"
    print(name)
    
name_fun()
myname_funct1()  

def add_fun(num1, num2):
    sum_int = num1 + num2  
    number1 = 10
    number2 = 30
    print("Sum is :", sum_int)

number1 = 1
number2 = 11

add_fun(number1, number2)
print(number1)
print(number2)
#print(sum_int)

add_fun(num1=10,num2=20)
#print(num1)
#print(num2)

#add_fun(x=1,y=20)

 
    