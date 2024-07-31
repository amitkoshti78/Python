# Python Program to create list, list of lists (matrix), tuple, set, and dictionary #using for loops

# 1. Creating a List using a for loop
# A list is an ordered collection of items. Here, we'll create a list of square numbers.
squares_list = []
for i in range(1, 6):  # range(1, 6) generates numbers from 1 to 5
    squares_list.append(i ** 2)  # Append the square of each number to the list

print("List of squares:", squares_list)

# 2. Creating a List of Lists (Matrix) using nested for loops
# A matrix is a 2D array, where each element is a list (row) containing other lists ###
# (columns).
matrix = []
for i in range(3):  # 3 rows
    row = []  # Create an empty row
    for j in range(3):  # 3 columns
        row.append(i * 3 + j + 1)  # Populate the row with sequential numbers
    matrix.append(row)  # Add the row to the matrix

print("\nMatrix (List of Lists):")
for row in matrix:
    print(row)

# 3. Creating a Tuple using a for loop
# A tuple is an ordered, immutable collection of items.
numbers_tuple = tuple(i for i in range(1, 6))  # Using a generator expression to create a tuple

print("\nTuple of numbers:", numbers_tuple)

# 4. Creating a Set using a for loop
# A set is an unordered collection of unique items.
unique_set = set()
for i in range(1, 11):
    unique_set.add(i % 5)  
# Add the remainder when dividing by 5, resulting in unique items

print("\nSet of unique remainders:", unique_set)

# 5. Creating a Dictionary using a for loop
# A dictionary is an unordered collection of key-value pairs.
squares_dict = {}
for i in range(1, 6):
    squares_dict[i] = i ** 2  # Key is the number, value is its square

print("\nDictionary of squares:")
for key, value in squares_dict.items():
    print(f"{key}: {value}")

# Explanation of Constructs:

# 1. List:
#    - A list is a dynamic array that can hold elements of different types. It allows 
# # duplicate items.
#    - We created `squares_list` using a for loop and `append()` method to add items.

# 2. List of Lists (Matrix):
#    - A matrix is a collection of lists within a list, creating a 2D array.
#    - We created `matrix` using nested for loops: the outer loop creates rows, and the #inner loop fills each row.

# 3. Tuple:
#    - A tuple is like a list, but it is immutable (cannot be modified after creation).
#    - We used a generator expression within `tuple()` to create `numbers_tuple`.

# 4. Set:
#    - A set stores unique elements in an unordered way. It automatically removes #duplicates.
#    - We used `add()` method in a loop to populate `unique_set` with unique remainders #of division.

# 5. Dictionary:
#    - A dictionary stores data in key-value pairs, where each key is unique.
#    - We created `squares_dict` by assigning keys and their corresponding squared #values inside a loop.
