from typing import Final

x = 1              # global variable 0x567812345
PI = 3.14

def outer_fun():
    x  = 2             # local variable 0x333333333
    
    def inner_fun():
        #global x
        nonlocal x
        x = 3               # local varible 0x2345678
        print("inner function x and its adress : ", x, " --> ", hex(id(x)))
    
    inner_fun()     
    print("outer function x and its adress : ", x, " --> ", hex(id(x)))
    
outer_fun()    
print("global variable x and its adress: ", x, " --> ", hex(id(x)))

def area(radius):  
    global PI
    PI = 100 
    return PI * radius ** 2

print(area(5))

class ConstantsNamespace():
    __slots__ = ()
    PI = 3.14159
    GRAVITY = 9.80665
    
constant = ConstantsNamespace()

#constant.PI = 100

from enum import Enum

class MyConstants(Enum):
    MY_PI = 3.14
    MY_GRAVITY = 9.81
    MONTH = "May"
    
#MyConstants.MY_PI = 100
print(list(MyConstants))
    
    
 