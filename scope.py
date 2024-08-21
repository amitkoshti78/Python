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





class ConstantsNamespace():
    __slots__ = ()
    PI = 3.14159
    GRAVITY = 9.80665
    LIMIT = 10
    
constant = ConstantsNamespace()

#constant.PI = 100

def area(radius): 
    #constant.PI = 100
    return constant.PI * radius ** 2

print("Area : " , area(5))

from enum import Enum

class MyConstants(Enum):
    MY_PI = 3.14
    MY_GRAVITY = 9.81
    MONTH = "May"
    
#MyConstants.MY_PI = 100
#print(list(MyConstants))
    
for number in range(1,constant.LIMIT)  :
    print("x")
    
for index in range(1,constant.LIMIT):
    print("y")
    
for subscript in range(1,constant.LIMIT):
    print("z")

#MyConstants.MY_PI = 100