
def add_num(name, *numbers):
    sum = 0
    print(numbers)
    for num in numbers:
        sum = sum + num
    
    return sum, name.upper()

result, upp_name = add_num('amit', 1,3,7,8,2,7,56,12,78,90,12,45,34,98,12,32 )
print(f' Hi {upp_name} the sum of numbers is : {result}')

def upp_name(*names):
    upp_name_list = []
    print(names)
    for name in names:
        upp_name_list.append(name.upper())
    
    return upp_name_list

print(upp_name("Amit", "Neha", "Omkar", "Anurag", "Aditya"))

def student(**kwargs):

    print(kwargs)
    kwargs['age'] = 46
    for key, value in kwargs.items():
        #print(key, value)
        kwargs['sem'] = 4
        
        
    return kwargs

print(student(first_name="Amit", rnr = 101, yy = 2024, sem = 3))


def student_marks(*marks, **kwargs):

    print(kwargs)
    print(marks)
    for info in kwargs.items():
        print(info)

    
    
student_marks(60, 80, 90, first_name="Amit", rnr = 101, yy = 2024, sem = 3)


dict_phone = {
                'Amit'      : 2345678989 ,
                'Omkar'     : 3456789120 ,
                'Tanvi'     : 9856789123 ,
                'Anurag'    : 9145675681 ,
                'Neha'      : 7857789147 ,
                'Varad'     : 3418902382 , 
}
print(dict_phone)

for key , value in dict_phone.items():
    print(key, value)


dict_phone['Amit'] = 0
print(dict_phone)

print(dict_phone.popitem())
print(dict_phone)

print(dict_phone.get('Neha'))

dict_phone['Avinash'] = 3457812794
print(dict_phone)



# Python functions are very flexible when it comes to passing arguments. Let's go over #the different types of function arguments and their usage with examples.

# 1. Positional Arguments
# These are the most common type of arguments. When you call a function, the arguments #are assigned to parameters in the order in which they are passed.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Call the function with positional arguments
greet("Alice", 30)

# Explanation: Here, "Alice" is assigned to name, and 30 is assigned to age. The
# function prints: "Hello, Alice! You are 30 years old."

# 2. Keyword Arguments
# Keyword arguments allow you to specify arguments by parameter name, so the order doesn’t matter.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Call the function with keyword arguments
greet(age=30, name="Alice")

""" Explanation: By specifying the parameter names (age=30, name="Alice"), you can pass arguments in any order.

3. Default Arguments
You can provide default values for parameters. If the argument is not passed, the default value is used. """

def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")

# Call the function with and without the default argument
greet("Alice", 30)  # Uses the provided value
greet("Bob")        # Uses the default value

""" Explanation: In the second call (greet("Bob")), since age is not provided, the default value 25 is used.

4. Variable-length Arguments (*args)
If you want to pass a variable number of positional arguments, you can use *args. This collects additional positional arguments into a tuple.
 """
 
def add_numbers(*args):
    return sum(args)

# Call the function with different numbers of arguments
print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(5, 10, 15, 20))  # Output: 50

""" Explanation: Here, *args allows the function to accept any number of arguments, which are summed up and returned.

5. Variable-length Keyword Arguments (**kwargs)
If you want to pass a variable number of keyword arguments, use **kwargs. This collects them into a dictionary.
     """
     
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with various keyword arguments
print_details(name="Alice", age=30, city="New York")

""" Explanation: **kwargs allows the function to accept any number of keyword arguments, which are then printed.

6. Positional-only Arguments (Python 3.8+)
You can force some arguments to be passed positionally by using a / in the function signature. """

def greet(name, /, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call the function
greet("Alice")          # Positional argument required for 'name'
greet("Alice", "Hi")    # Positional arguments for both

""" Explanation: The / indicates that name must be passed positionally, so greet(name="Alice") would raise an error.

7. Keyword-only Arguments
You can force some arguments to be passed as keyword arguments by using * in the function signature. """

def greet(*, name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call the function
greet(name="Alice")          # Keyword argument required for 'name'
greet(name="Alice", greeting="Hi")  # Keyword arguments for both

""" Explanation: The * indicates that all following parameters must be passed as keyword arguments.

8. Combining Different Argument Types
You can combine positional, default, *args, **kwargs, positional-only, and keyword-only arguments in a single function. """

def complex_function(pos1, pos2, /, default_arg="default", *args, kwarg1, kwarg2="default_kwarg", **kwargs):
    print(f"Positional-only arguments: {pos1}, {pos2}")
    print(f"Default argument: {default_arg}")
    print(f"Variable-length positional arguments: {args}")
    print(f"Keyword-only arguments: {kwarg1}, {kwarg2}")
    print(f"Additional keyword arguments: {kwargs}")

# Call the function with various argument types
complex_function(1, 2, 3, 4, kwarg1="keyword", extra="extra_value")


def fun_sum(*arguments) -> float:
    sum = 0
    for number in arguments:
        sum = sum + number
    
    return f'{sum:0.2f}'

print(f'SUM OF NUMBERS : {fun_sum(1,2,3,4,5)}')


""" Explanation:
pos1 and pos2 must be passed positionally.
default_arg is optional and has a default value.
*args captures additional positional arguments.
kwarg1 must be passed as a keyword argument.
kwarg2 has a default value but can be overridden.
**kwargs captures any additional keyword arguments.

Summary:
Positional Arguments: Ordered and required.

Keyword Arguments: Specify by name, order doesn’t matter.

Default Arguments: Provide default values for parameters.

Variable-length Positional Arguments (*args): Accept a variable number of positional arguments as a tuple.

Variable-length Keyword Arguments (**kwargs): Accept a variable number of keyword arguments as a dictionary.

Positional-only Arguments (/): Force arguments to be passed positionally.

Keyword-only Arguments (*): Force arguments to be passed as keywords.

These different types of function arguments allow Python functions to be flexible and powerful, making it easy to handle a wide range of use cases.
"""