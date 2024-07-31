# Python Program to demonstrate usage of Lists, Sets, Tuples, and Dictionaries

# 1. Lists
# A list is an ordered collection of items that can be of different types.

fruits = ["apple", "banana", "cherry", "date"]
print("List of fruits:", fruits)

# Accessing elements in a list by index (0-based indexing)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding an item to the list
fruits.append("elderberry")
print("List after adding a new fruit:", fruits)

# Removing an item from the list
fruits.remove("banana")
print("List after removing a fruit:", fruits)

# 2. List of Lists
# A list can contain other lists, creating a matrix-like structure.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix (List of Lists):")
for row in matrix:
    print(row)

# Accessing elements in a list of lists
print("Element at first row, second column:", matrix[0][1])

# 3. Sets
# A set is an unordered collection of unique items.

numbers = {1, 2, 3, 4, 4, 5}
print("\nSet of numbers (duplicates removed):", numbers)

# Adding an element to the set
numbers.add(6)
print("Set after adding a number:", numbers)

# Removing an element from the set
numbers.remove(2)
print("Set after removing a number:", numbers)

# 4. Tuples
# A tuple is similar to a list, but it is immutable (cannot be changed after creation).

coordinates = (10.0, 20.0)
print("\nTuple of coordinates:", coordinates)

# Accessing elements in a tuple
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])

# Tuples can be used to store related data together
person_info = ("Amit", 30, "Engineer")
print("Person Info Tuple:", person_info)

# 5. Dictionaries
# A dictionary is an unordered collection of key-value pairs.

student_info = {
    "name": "Swapnil",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
print("\nDictionary of student information:", student_info)

# Accessing values in a dictionary by keys
print("Student's name:", student_info["name"])
print("Student's age:", student_info["age"])

# Adding a new key-value pair to the dictionary
student_info["grade"] = "A"
print("Dictionary after adding grade:", student_info)

# Updating a value in the dictionary
student_info["age"] = 22
print("Dictionary after updating age:", student_info)

# Removing a key-value pair from the dictionary
del student_info["courses"]
print("Dictionary after removing courses:", student_info)

# Summary of data structures used
print("\nSummary:")
print("List:", fruits)
print("List of Lists (Matrix):", matrix)
print("Set:", numbers)
print("Tuple:", coordinates)
print("Dictionary:", student_info)
