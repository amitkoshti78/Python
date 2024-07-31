""" What is a Generator Expression?
A generator expression is a concise way to create an iterator that yields items one at a time. It is similar to list comprehensions, but instead of creating a list and storing all elements in memory, a generator expression creates an iterator that generates elements on the fly, saving memory and improving performance for large datasets.

The syntax of a generator expression is similar to a list comprehension but uses parentheses () instead of square brackets [].

Basic Examples
1. Creating a Simple Generator Expression """

gen_exp = (x * x for x in range(5))

""" Here, gen_exp is a generator expression that generates the squares of numbers from 0 to 4.
It does not compute all squares immediately. Instead, it produces one value at a time as needed.
To retrieve values from a generator, you can use a for loop or the next() function.
 """

# Using a for loop to iterate through the generator
print("\n List of squares")
for value in gen_exp:
    print(value)

# Resetting the generator expression
gen_exp = (x * x for x in range(5))

# Using the next() function
print("\n List of squares use of next")
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
print(next(gen_exp))  # Output: 4

""" 2. Filtering with Generator Expressions
You can use conditional expressions within generator expressions to filter elements.
 """

even_squares = (x * x for x in range(10) if x % 2 == 0)

print("\n List of squares divisible by 2")
for value in even_squares:
    print(value, end=" ")
    
""" This generator expression computes squares only for even numbers from 0 to 9.

3. Generator Expression with Functions
You can use generator expressions directly as arguments to functions.
 """

# Summing squares of numbers from 1 to 10
print("\n Sum of squares : ", end=" ")
sum_of_squares = sum(x * x for x in range(1, 11))
print(sum_of_squares)  # Output: 385


# Finding the maximum square of numbers from 1 to 10
print("\n Max of squares : ", end=" ")
max_square = max(x * x for x in range(1, 11))
print(max_square)  # Output: 100

""" 4. Generator Expression Inside Another Expression
Generator expressions can be part of larger expressions, making them versatile and concise.
 """

# Using a generator expression within a tuple
print("\n Tuple of squares : ", end=" ")
square_tuple = tuple(x * x for x in range(1, 6))
print(square_tuple)  # Output: (1, 4, 9, 16, 25)

# Using a generator expression within a list
print("\n List of squares : ", end=" ")
square_list = [x * x for x in range(1, 6)]
print(square_list)  # Output: [1, 4, 9, 16, 25]

""" Advanced Examples
1. Generator Expression with Multiple Iterables
You can use multiple iterables inside a generator expression.
 """


# Cartesian product of two sets using a generator expression
print("\n Co ordinates of x y axis of squares : ")
cartesian_product = ((x, y) for x in range(0, 6) for y in range(0, 6))

for pair in cartesian_product:
    print(pair)
    
""" This generator expression creates pairs of numbers from two ranges, resulting in a Cartesian product.
2. Using Generator Expressions to Process Large Files
Generator expressions are particularly useful for processing large datasets or files because they don't load everything into memory at once.
 """

# Assume we have a large file 'large_file.txt'
# We can process lines that contain a specific keyword efficiently with a generator expression

""" with open('large_file.txt') as file:
    lines_with_keyword = (line for line in file if 'keyword' in line)
    for line in lines_with_keyword:
        print(line)
The above code reads and processes one line at a time, which is memory-efficient for large files.
3. Combining Generator Expressions with itertools
Python's itertools module provides a collection of tools for working with iterators, and generator expressions can be used with these tools.
 """

import itertools

# Infinite sequence of even numbers
even_numbers = (x for x in itertools.count(0, 2))

# Take the first 10 even numbers
print("\n list of squares using itertools : ", end=" ")
first_10_evens = list(itertools.islice(even_numbers, 10))
print(first_10_evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

""" Here, itertools.count generates an infinite sequence of even numbers, and itertools.islice takes only the first 10 values.
Key Points to Remember
Memory Efficiency: Unlike list comprehensions, generator expressions do not store the entire sequence in memory. They generate items one at a time and only when needed.

Lazy Evaluation: Generator expressions use lazy evaluation, meaning they produce items on-the-fly rather than computing all items upfront.

Immutability: Generators are one-time-use objects. Once you've iterated over a generator, you cannot reset or reuse it. You would need to create a new generator expression to iterate again.

Performance: Generator expressions are more performant in situations where you are working with large datasets or when you only need a subset of the generated sequence.

When to Use Generator Expressions?

For large datasets: When working with large data where you don't need all elements at once, like reading big files line by line.
When memory is a concern: To avoid using too much memory, especially in resource-constrained environments.

For streaming data: When working with data streams or any scenario where data is produced over time, rather than all at once.
By understanding and using generator expressions, you can write more efficient and scalable Python code, especially when dealing with large datasets or performance-critical applications.
 """





