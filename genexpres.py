# Python Program to create list, list of lists (matrix), tuple, set, and dictionary using generator expressions

# 1. Creating a List using a list comprehension (which is a type of generator expression)
# A list comprehension allows you to create a list in a single line.
squares_list = [i ** 2 for i in range(1, 6)]  # Creates a list of squares of numbers from 1 to 5

print("List of squares:", squares_list)

# 2. Creating a List of Lists (Matrix) using a nested list comprehension
# A matrix is a 2D array, where each element is a list (row) containing other lists (columns).
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]  # 3x3 matrix with sequential numbers

print("\nMatrix (List of Lists):")
for row in matrix:
    print(row)

# 3. Creating a Tuple using a generator expression
# A generator expression is similar to a list comprehension but creates a generator instead of a list.
numbers_tuple = tuple(i for i in range(1, 6))  # Creates a tuple of numbers from 1 to 5

print("\nTuple of numbers:", numbers_tuple)

# 4. Creating a Set using a set comprehension
# A set comprehension is similar to a list comprehension but creates a set instead.
unique_set = {i % 5 for i in range(1, 11)}  # Creates a set of unique remainders when dividing numbers from 1 to 10 by 5

print("\nSet of unique remainders:", unique_set)

# 5. Creating a Dictionary using a dictionary comprehension
# A dictionary comprehension allows you to create a dictionary in a single line.
squares_dict = {i: i ** 2 for i in range(1, 6)}  # Creates a dictionary of numbers and their squares

print("\nDictionary of squares:")
for key, value in squares_dict.items():
    print(f"{key}: {value}")

# Explanation of Constructs:

# 1. List Comprehension:
#    - A list comprehension is a concise way to create lists. It follows the syntax:
#      [expression for item in iterable].
#    - Here, we used a list comprehension to create `squares_list` with squares of numbers.

# 2. Nested List Comprehension (Matrix):
#    - A nested list comprehension allows creating a 2D list (matrix) in a single line.
#    - The outer comprehension creates rows, and the inner one fills each row with elements.

# 3. Generator Expression (Tuple):
#    - A generator expression is similar to a list comprehension but uses parentheses instead of brackets.
#    - We used `tuple()` to convert the generator into a tuple.

# 4. Set Comprehension:
#    - A set comprehension is similar to a list comprehension but creates a set.
#    - It uses curly braces `{}` and automatically removes duplicate items.

# 5. Dictionary Comprehension:
#    - A dictionary comprehension allows creating a dictionary in a concise way.
#    - The syntax is {key: value for item in iterable}, and we used it to create `squares_dict`.
