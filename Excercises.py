Given that you've requested solutions and explanations for 75 complex Python assignments, providing solutions for all of them would require an extensive amount of time and space. However, I can start by giving you solutions and detailed explanations for a selection of these assignments, and then you can let me know if you'd like to continue with more. Let's begin with a few sample problems from each category.

---

### **Sample Solutions with Explanations**

---

### **1. Palindrome Checker (Topic: Strings)**

**Problem:**
Write a function that takes a string and returns whether the string is a palindrome (reads the same forward and backward).

```python
def is_palindrome(s):
    # Normalize the string by converting to lowercase and removing spaces
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False
```

**Explanation:**
- The function first normalizes the input by removing spaces (`replace(" ", "")`) and converting all characters to lowercase (`lower()`).
- Then, we compare the string to its reverse (`s[::-1]`). If they are equal, the string is a palindrome.
- We use slicing `[::-1]` to reverse the string.

---

### **2. Temperature Conversion with f-strings (Topic: f-strings)**

**Problem:**
Display a list of temperature conversions between Celsius, Fahrenheit, and Kelvin using f-strings.

```python
def temperature_conversion_table(celsius_values):
    for celsius in celsius_values:
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")

# Test
temperature_conversion_table([0, 25, 100])
```

**Explanation:**
- The function `temperature_conversion_table()` takes a list of Celsius temperatures as input.
- For each Celsius value, it calculates the corresponding Fahrenheit and Kelvin values.
- The results are printed using f-strings, with 2 decimal places for formatting (`.2f`).

---

### **3. Number Guessing Game (Topic: while loops)**

**Problem:**
Write a number guessing game that gives feedback on whether the guess is too high, too low, or correct.

```python
import random

def guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        
        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Correct! The number was {target_number}. You guessed it in {attempts} attempts.")
            break

# Play the game
guessing_game()
```

**Explanation:**
- The function generates a random number between 1 and 100 using `random.randint(1, 100)`.
- The game runs in an infinite loop (`while True`), and the user is repeatedly prompted for a guess.
- Based on the guess, the program provides feedback: "Too low!" or "Too high!". If the guess is correct, it exits the loop and displays the number of attempts.

---

### **4. Prime Factorization (Topic: for loops)**

**Problem:**
Write a program that returns all the prime factors of a given number using for loops.

```python
def prime_factors(n):
    factors = []
    
    # Check for number of 2s
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# Test
print(prime_factors(56))  # [2, 2, 2, 7]
print(prime_factors(97))  # [97] (since 97 is prime)
```

**Explanation:**
- The function first removes all factors of 2 from `n` using a `while` loop.
- Then, it checks odd numbers starting from 3 for prime factors using a `for` loop.
- If the remaining `n` is greater than 2, it is a prime number, and it is added to the list of factors.

---

### **5. Simple Calculator with `match/case` (Topic: match/case)**

**Problem:**
Write a basic calculator that performs addition, subtraction, multiplication, and division using `match/case`.

```python
def calculator(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Cannot divide by zero"
            return a / b
        case _:
            return "Invalid operator"

# Test
print(calculator(10, 5, "+"))  # 15
print(calculator(10, 0, "/"))  # Cannot divide by zero
print(calculator(10, 5, "^"))  # Invalid operator
```

**Explanation:**
- The function uses Python's `match/case` (Python 3.10+) to select the appropriate operation based on the input operator.
- The `case` handles different operators (+, -, *, /). If the operator is invalid, the default case (`_`) returns an error message.
- Division by zero is handled explicitly.

---

### **6. Area Calculator Using Default Parameters (Topic: Function Parameters)**

**Problem:**
Write a function that calculates the area of a circle, square, or rectangle based on user input, using default and keyword arguments.

```python
def calculate_area(shape="circle", radius=1, length=1, width=1):
    if shape == "circle":
        return 3.1416 * radius * radius
    elif shape == "square":
        return length * length
    elif shape == "rectangle":
        return length * width
    else:
        return "Invalid shape"

# Test
print(calculate_area())  # Default circle area: 3.1416
print(calculate_area(shape="square", length=4))  # Square area: 16
print(calculate_area(shape="rectangle", length=4, width=5))  # Rectangle area: 20
```

**Explanation:**
- The function has default values for all parameters (shape defaults to "circle", and dimensions default to 1).
- Depending on the shape, it calculates the area accordingly. If no arguments are passed, it calculates the area of a default circle.
- Keyword arguments are used to specify the shape and dimensions.

---

### **7. Context Manager for File Handling (Topic: Exception Handling)**

**Problem:**
Write a context manager that opens a file, reads its content, and ensures the file is closed, even if an exception occurs.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        return True  # Suppress exceptions

# Test
with FileManager("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

**Explanation:**
- The `FileManager` class is a context manager that implements `__enter__()` and `__exit__()` methods.
- When entering the context (`with` block), it opens the file, and on exiting, it closes the file.
- If an exception occurs inside the `with` block, it catches the exception and prints the error message, ensuring that the file is closed regardless of errors.

---

I hope these sample solutions provide a clear understanding of how to approach and solve intermediate-level Python problems. These examples illustrate different Python features, including loops, conditionals, functions, exception handling, and more. 

Let me know if you'd like to continue with more solutions, or if you have any specific assignments you'd like me to cover next!

Great! Let's continue with more solutions and detailed explanations for some of the other assignments from the previous list. I'll cover a few more programs from different topics and dive deep into how they work.

---

### **8. Vowel Counter (Topic: Strings)**

**Problem:**
Write a program that counts the number of vowels in a given string.

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"  # Define a string of vowels
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
            
    return count

# Test
print(count_vowels("Hello World"))  # 3
print(count_vowels("Python Programming"))  # 4
```

**Explanation:**
- We create a `vowels` string containing all lowercase and uppercase vowels.
- We iterate through each character in the input string `s` and check if it exists in the `vowels` string.
- If it does, we increment the `count` by 1. Finally, we return the total count of vowels.

---

### **9. Reverse a String Using a for Loop (Topic: for loops)**

**Problem:**
Write a program that reverses a given string using a for loop.

```python
def reverse_string(s):
    reversed_string = ""
    
    for char in s:
        reversed_string = char + reversed_string  # Add each character to the beginning
    
    return reversed_string

# Test
print(reverse_string("hello"))  # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

**Explanation:**
- We initialize an empty string `reversed_string`.
- We iterate over each character in the string `s`, and for each character, we add it to the beginning of `reversed_string`.
- This effectively builds the reversed string one character at a time.

---

### **10. FizzBuzz (Topic: if, elif, else)**

**Problem:**
Write a program that prints numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz".

```python
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Run the program
fizzbuzz()
```

**Explanation:**
- The program uses a `for` loop to iterate through numbers from 1 to 100.
- For each number, we check the conditions:
  - If it's divisible by both 3 and 5, we print "FizzBuzz".
  - If it's divisible by 3 only, we print "Fizz".
  - If it's divisible by 5 only, we print "Buzz".
  - Otherwise, we print the number itself.

---

### **11. Number of Digits in a Number (Topic: while loops)**

**Problem:**
Write a program that takes an integer and returns the number of digits in the number using a while loop.

```python
def count_digits(n):
    n = abs(n)  # Make sure n is positive
    count = 0
    
    if n == 0:
        return 1  # Special case for 0
    
    while n > 0:
        n //= 10  # Remove the last digit
        count += 1
    
    return count

# Test
print(count_digits(12345))  # 5
print(count_digits(-9876))  # 4
print(count_digits(0))  # 1
```

**Explanation:**
- We handle negative numbers by using `abs()` to convert them to positive.
- If the number is 0, we return 1 (since 0 has one digit).
- We repeatedly divide the number by 10 to remove the last digit until the number becomes 0. Each time we divide, we increment the `count`.

---

### **12. Logical Operators (and/or) in Voting Eligibility Checker (Topic: Conditional Operators)**

**Problem:**
Write a program that checks if a person is eligible to vote based on age and citizenship using `and/or` logical operators.

```python
def check_voting_eligibility(age, citizenship):
    if age >= 18 and citizenship == "US":
        return "Eligible to vote"
    elif age < 18:
        return "Too young to vote"
    else:
        return "Not eligible to vote due to citizenship"

# Test
print(check_voting_eligibility(20, "US"))  # Eligible to vote
print(check_voting_eligibility(16, "US"))  # Too young to vote
print(check_voting_eligibility(25, "Canada"))  # Not eligible to vote due to citizenship
```

**Explanation:**
- The function checks if both conditions (`age >= 18` and `citizenship == "US"`) are met using the `and` operator.
- If the person is too young, it prints an appropriate message. Otherwise, it checks citizenship and prints an appropriate message for ineligible voters.

---

### **13. List Comprehension for Even Numbers (Topic: Lists)**

**Problem:**
Write a program that generates a list of even numbers from 1 to 100 using list comprehension.

```python
def even_numbers():
    return [x for x in range(1, 101) if x % 2 == 0]

# Test
print(even_numbers())  # [2, 4, 6, 8, ..., 100]
```

**Explanation:**
- List comprehension is used to create a list of even numbers by iterating through the range of numbers from 1 to 100.
- We include a condition (`if x % 2 == 0`) to select only even numbers.

---

### **14. Set Operations: Union and Intersection (Topic: Sets)**

**Problem:**
Write a program that performs union and intersection operations on two sets of numbers.

```python
def set_operations(set1, set2):
    union_result = set1 | set2  # Union
    intersection_result = set1 & set2  # Intersection
    
    return union_result, intersection_result

# Test
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union, intersection = set_operations(set1, set2)
print("Union:", union)  # {1, 2, 3, 4, 5, 6}
print("Intersection:", intersection)  # {3, 4}
```

**Explanation:**
- We use the `|` operator for union and the `&` operator for intersection.
- The union operation combines all unique elements from both sets, while the intersection operation finds elements common to both sets.

---

### **15. Random Password Generator (Topic: random Package)**

**Problem:**
Write a program that generates a random password of a specified length using the `random` package.

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test
print(generate_password(12))  # Example: sJ9$kL3*H@cX
```

**Explanation:**
- We use the `string` module to get a list of all possible characters (letters, digits, punctuation).
- We use `random.choice()` to select a random character from the list for each position in the password.
- The password is generated by joining these random characters into a string of the specified length.

---

### **16. Exception Handling in Division (Topic: Exception Handling)**

**Problem:**
Write a program that handles division by zero using `try/except`.

```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return result

# Test
print(divide_numbers(10, 2))  # 5.0
print(divide_numbers(10, 0))  # Cannot divide by zero
```

**Explanation:**
- The division operation is wrapped in a `try` block to catch potential `ZeroDivisionError`.
- If the exception occurs, the `except` block returns an error message. Otherwise, the result of the division is returned.

---

### **17. Recursive Factorial with Exception Handling (Topic: Recursive Functions)**

**Problem:**
Write a recursive function that computes the factorial of a number and handles invalid input using exceptions.

```python
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except ValueError as e:
        return str(e)

# Test
print(factorial(5))  # 120
print(factorial(-5))  # Factorial is not defined for negative numbers.
```

**Explanation:**
- We use a recursive function to compute the factorial of a number.
- A `try/except` block handles invalid input (negative numbers). If the number is negative, a `ValueError` is raised and caught, returning a custom error message.

---

These examples

 continue to build on the concepts from various categories. Let me know if you'd like me to continue with more topics or specific types of programs!
 
 Sure! Let's continue providing more solutions to the practice programs, covering different Python concepts as requested. I'll provide the code along with detailed explanations for each program.

---

### **18. Average of Numbers Using a List (Topic: Lists)**

**Problem:**
Write a program that takes a list of numbers as input and returns the average.

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Test
numbers = [10, 20, 30, 40, 50]
print(f"Average: {calculate_average(numbers)}")  # 30.0
```

**Explanation:**
- We calculate the average by summing all the numbers in the list using `sum()` and dividing by the length of the list using `len()`.
- This is a simple and effective way to compute the average of any list of numbers.

---

### **19. Sorting a List of Tuples by Second Element (Topic: Tuples)**

**Problem:**
Write a program that sorts a list of tuples based on the second element of each tuple.

```python
def sort_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1])

# Test
tuples = [(1, 2), (3, 1), (5, 4), (2, 3)]
print(f"Sorted tuples: {sort_by_second_element(tuples)}")  
# Output: [(3, 1), (1, 2), (2, 3), (5, 4)]
```

**Explanation:**
- We use Python's `sorted()` function to sort the list of tuples.
- The `key` argument is a `lambda` function that tells `sorted()` to use the second element (`x[1]`) of each tuple as the key for sorting.

---

### **20. Basic Calculator with `while` Loop (Topic: while loops)**

**Problem:**
Write a program that continuously asks the user to perform arithmetic operations (addition, subtraction, multiplication, or division) until the user chooses to exit.

```python
def calculator():
    while True:
        print("Options: +, -, *, /, or 'exit' to quit")
        operator = input("Enter an operation: ")
        
        if operator == "exit":
            break
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if operator == "+":
                print(f"Result: {a + b}")
            elif operator == "-":
                print(f"Result: {a - b}")
            elif operator == "*":
                print(f"Result: {a * b}")
            elif operator == "/":
                if b == 0:
                    print("Cannot divide by zero.")
                else:
                    print(f"Result: {a / b}")
            else:
                print("Invalid operator.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
```

**Explanation:**
- The program continuously asks the user for an arithmetic operation until the user enters `"exit"`.
- Inside the loop, we perform basic operations (`+`, `-`, `*`, `/`) based on the user's input.
- We use `try/except` to handle invalid numeric inputs and to check for division by zero.

---

### **21. Finding the Maximum of Three Numbers (Topic: if-elif-else)**

**Problem:**
Write a function that finds the maximum of three numbers using `if-elif-else` statements.

```python
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test
print(max_of_three(10, 20, 15))  # 20
print(max_of_three(25, 25, 20))  # 25
```

**Explanation:**
- We compare the three numbers using `if-elif-else` statements to find the largest one.
- The function returns the largest of the three numbers.

---

### **22. Fibonacci Generator (Topic: Generator Functions)**

**Problem:**
Write a generator function that yields the Fibonacci sequence up to a certain limit.

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Test
fib_sequence = fibonacci(100)
print(list(fib_sequence))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

**Explanation:**
- The generator function `fibonacci()` generates Fibonacci numbers up to a given limit using the `yield` statement.
- Generators allow us to iterate over potentially infinite sequences without storing them all in memory.

---

### **23. Using `map()` to Square Elements of a List (Topic: map function)**

**Problem:**
Write a program that uses `map()` to square all the elements in a list.

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(f"Squared numbers: {squared_numbers}")  # [1, 4, 9, 16, 25]
```

**Explanation:**
- The `map()` function applies the `square()` function to each element of the `numbers` list.
- We convert the result of `map()` back to a list and print it.

---

### **24. Using `filter()` to Keep Even Numbers (Topic: filter function)**

**Problem:**
Write a program that uses `filter()` to keep only even numbers in a list.

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))

print(f"Even numbers: {even_numbers}")  # [2, 4, 6]
```

**Explanation:**
- The `filter()` function applies the `is_even()` function to filter out odd numbers from the list.
- We convert the result to a list and print the even numbers.

---

### **25. Factorial Using a Lambda Function (Topic: Lambda Functions)**

**Problem:**
Write a program that uses a lambda function to calculate the factorial of a number.

```python
from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

# Test
print(factorial(5))  # 120
```

**Explanation:**
- We use a lambda function in conjunction with `reduce()` to compute the factorial of a number.
- The `reduce()` function applies the lambda function to accumulate the product of numbers from 1 to `n`.

---

### **26. Creating a Set of Unique Words (Topic: Sets)**

**Problem:**
Write a program that takes a string as input and returns a set of unique words.

```python
def unique_words(text):
    words = text.split()
    return set(words)

# Test
text = "Python is great and Python is powerful"
print(unique_words(text))  # {'Python', 'is', 'great', 'and', 'powerful'}
```

**Explanation:**
- We split the input string into words using `split()`, then convert the list of words into a set, which automatically removes duplicates.
- This allows us to return a set of unique words.

---

### **27. Dictionary of Word Frequencies (Topic: Dictionaries)**

**Problem:**
Write a program that takes a string as input and returns a dictionary with the frequency of each word.

```python
def word_frequencies(text):
    words = text.split()
    frequencies = {}
    
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    return frequencies

# Test
text = "python python code code code"
print(word_frequencies(text))  # {'python': 2, 'code': 3}
```

**Explanation:**
- The input string is split into words, and we use a dictionary to store the frequency of each word.
- We iterate through the list of words, updating the dictionary with the count of each word.

---

### **28. Rolling a Die Using `random` (Topic: random Package)**

**Problem:**
Write a program that simulates rolling a six-sided die 10 times and prints the result of each roll.

```python
import random

def roll_die():
    for _ in range(10):
        print(random.randint(1, 6))

# Simulate rolling the die
roll_die()
```

**Explanation:**
- The program uses `random.randint(1, 6)` to simulate rolling a six-sided die, printing the result of each roll.
- This function is executed in a loop 10 times.

---

### **29. Exception Handling with Try/Except/Finally (Topic: Exception Handling)**

**Problem:**
Write a program that demonstrates `try`, `except`, `else`, and `finally` blocks in exception handling by dividing two numbers.

```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution complete.")

# Test
divide_numbers(10, 2)  # Result

: 5.0, Execution complete.
divide_numbers(10, 0)  # Error: Cannot divide by zero., Execution complete.
```

**Explanation:**
- We perform division inside a `try` block and catch `ZeroDivisionError`.
- If no exception occurs, the result is printed in the `else` block.
- The `finally` block executes regardless of whether an exception occurred, ensuring that the "Execution complete" message is printed every time.

---

### **30. Capitalize Words Using `map()` and `lambda` (Topic: Lambda and map Functions)**

**Problem:**
Write a program that takes a list of lowercase words and capitalizes the first letter of each word using `map()` and a lambda function.

```python
words = ["python", "java", "c++", "javascript"]

capitalized_words = list(map(lambda word: word.capitalize(), words))

print(capitalized_words)  # ['Python', 'Java', 'C++', 'Javascript']
```

**Explanation:**
- We use `map()` with a lambda function to apply the `capitalize()` method to each word in the list.
- The result is a list of words with their first letter capitalized.

---

These solutions cover a broad range of Python concepts, such as loops, functions, exceptions, and data structures. If you want to see more solutions from specific categories or need further explanations, feel free to ask!

Let's continue with more solutions and explanations for the programming assignments. Here are more solutions to some of the remaining assignments:

---

### **31. Check if a String is a Palindrome (Topic: Strings)**

**Problem:**
Write a function that checks whether a given string is a palindrome (a word, phrase, or sequence that reads the same backward as forward).

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Test
print(is_palindrome("radar"))  # True
print(is_palindrome("Python"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
```

**Explanation:**
- We first convert the input string to lowercase and remove any spaces to handle cases where the input contains spaces or mixed case.
- Then, we check if the string is equal to its reverse using slicing (`s[::-1]`).
- If they are the same, the function returns `True`, indicating that the string is a palindrome.

---

### **32. Format Currency with `f-strings` (Topic: f-strings)**

**Problem:**
Write a program that formats a floating-point number to display as currency using `f-strings`.

```python
def format_currency(amount):
    return f"${amount:,.2f}"

# Test
print(format_currency(1234567.89))  # $1,234,567.89
```

**Explanation:**
- The `f-string` is used to format the number as currency.
- The `:,.2f` inside the curly braces ensures that the number is formatted with commas as thousand separators and with two decimal places.

---

### **33. Checking Leap Year (Topic: if, elif, else)**

**Problem:**
Write a function to determine if a given year is a leap year.

```python
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test
print(is_leap_year(2024))  # True
print(is_leap_year(2021))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
```

**Explanation:**
- A year is a leap year if it is divisible by 4 and not divisible by 100, unless it is also divisible by 400.
- This function implements the leap year rule using `if-elif-else` statements.

---

### **34. Multiplication Table Using `for` Loop (Topic: for loops)**

**Problem:**
Write a program that prints the multiplication table for a given number using a `for` loop.

```python
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Test
multiplication_table(5)
```

**Explanation:**
- The function prints the multiplication table for a number `n` from 1 to 10 using a `for` loop.
- `f-strings` are used to format the output in a readable way.

---

### **35. Finding the Greatest Common Divisor (GCD) (Topic: Functions)**

**Problem:**
Write a function that finds the greatest common divisor (GCD) of two numbers.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test
print(gcd(48, 18))  # 6
print(gcd(101, 103))  # 1
```

**Explanation:**
- The function uses the Euclidean algorithm to find the GCD.
- In each iteration, `a` is assigned the value of `b`, and `b` is assigned the remainder of `a` divided by `b`. This process continues until `b` becomes zero, and at that point, `a` holds the GCD.

---

### **36. Count Words in a String (Topic: Strings)**

**Problem:**
Write a program that counts the number of words in a string.

```python
def count_words(s):
    words = s.split()
    return len(words)

# Test
print(count_words("Hello World"))  # 2
print(count_words("Python programming is fun"))  # 4
```

**Explanation:**
- The `split()` function splits the string into words using spaces as delimiters.
- The `len()` function then returns the number of words in the list.

---

### **37. Infinite Fibonacci Sequence Generator (Topic: Generator Functions)**

**Problem:**
Write a generator function that generates an infinite Fibonacci sequence.

```python
def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test
fib_gen = infinite_fibonacci()
for _ in range(10):
    print(next(fib_gen))
```

**Explanation:**
- This generator function continuously yields the next Fibonacci number.
- We use `yield` to return each number one at a time. The `while True` loop makes this generator infinite, so it will keep generating Fibonacci numbers indefinitely until stopped.

---

### **38. Find Primes Using `filter()` and `lambda` (Topic: filter and lambda)**

**Problem:**
Write a program that filters out all the prime numbers in a list using `filter()` and a `lambda` function.

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = list(range(1, 50))
primes = list(filter(lambda x: is_prime(x), numbers))

print(f"Primes: {primes}")  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

**Explanation:**
- The `is_prime()` function checks if a number is prime by testing divisibility up to the square root of the number.
- The `filter()` function applies `is_prime()` to each element in the `numbers` list, filtering out non-prime numbers.
- The resulting primes are then converted back to a list.

---

### **39. Sum of Even Numbers Using List Comprehension (Topic: Lists and List Comprehension)**

**Problem:**
Write a program that calculates the sum of all even numbers in a list using list comprehension.

```python
def sum_of_evens(numbers):
    return sum([x for x in numbers if x % 2 == 0])

# Test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_evens(numbers))  # 30
```

**Explanation:**
- We use list comprehension to create a list of even numbers from the input list.
- The `sum()` function adds up all the even numbers in the list.

---

### **40. Simple Interest Calculator (Topic: Function Parameters)**

**Problem:**
Write a program that calculates simple interest using a function that takes `principal`, `rate`, and `time` as parameters.

```python
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Test
print(simple_interest(1000, 5, 3))  # 150.0
```

**Explanation:**
- The function calculates the simple interest using the formula `(principal * rate * time) / 100`.
- The `principal`, `rate`, and `time` are passed as parameters to the function.

---

### **41. Factorial of a Number Using Recursion (Topic: Recursion)**

**Problem:**
Write a recursive function that calculates the factorial of a given number.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test
print(factorial(5))  # 120
print(factorial(0))  # 1
```

**Explanation:**
- The function calls itself recursively until it reaches the base case (`n == 0` or `n == 1`).
- For other cases, the function returns `n * factorial(n - 1)`.

---

### **42. Merge Two Dictionaries (Topic: Dictionaries)**

**Problem:**
Write a program that merges two dictionaries into one.

```python
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Test
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # {'a': 1, 'b': 3, 'c': 4}
```

**Explanation:**
- We first create a copy of `dict1` to avoid modifying the original dictionary.
- We then use the `update()` method to add the key-value pairs from `dict2` to the merged dictionary. If a key exists in both dictionaries, the value from `dict2` overwrites the value from `dict

Let's continue with more solutions and explanations for the programming assignments. Here are more solutions to some of the remaining assignments:

---

### **31. Check if a String is a Palindrome (Topic: Strings)**

**Problem:**
Write a function that checks whether a given string is a palindrome (a word, phrase, or sequence that reads the same backward as forward).

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Test
print(is_palindrome("radar"))  # True
print(is_palindrome("Python"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
```

**Explanation:**
- We first convert the input string to lowercase and remove any spaces to handle cases where the input contains spaces or mixed case.
- Then, we check if the string is equal to its reverse using slicing (`s[::-1]`).
- If they are the same, the function returns `True`, indicating that the string is a palindrome.

---

### **32. Format Currency with `f-strings` (Topic: f-strings)**

**Problem:**
Write a program that formats a floating-point number to display as currency using `f-strings`.

```python
def format_currency(amount):
    return f"${amount:,.2f}"

# Test
print(format_currency(1234567.89))  # $1,234,567.89
```

**Explanation:**
- The `f-string` is used to format the number as currency.
- The `:,.2f` inside the curly braces ensures that the number is formatted with commas as thousand separators and with two decimal places.

---

### **33. Checking Leap Year (Topic: if, elif, else)**

**Problem:**
Write a function to determine if a given year is a leap year.

```python
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test
print(is_leap_year(2024))  # True
print(is_leap_year(2021))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
```

**Explanation:**
- A year is a leap year if it is divisible by 4 and not divisible by 100, unless it is also divisible by 400.
- This function implements the leap year rule using `if-elif-else` statements.

---

### **34. Multiplication Table Using `for` Loop (Topic: for loops)**

**Problem:**
Write a program that prints the multiplication table for a given number using a `for` loop.

```python
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Test
multiplication_table(5)
```

**Explanation:**
- The function prints the multiplication table for a number `n` from 1 to 10 using a `for` loop.
- `f-strings` are used to format the output in a readable way.

---

### **35. Finding the Greatest Common Divisor (GCD) (Topic: Functions)**

**Problem:**
Write a function that finds the greatest common divisor (GCD) of two numbers.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test
print(gcd(48, 18))  # 6
print(gcd(101, 103))  # 1
```

**Explanation:**
- The function uses the Euclidean algorithm to find the GCD.
- In each iteration, `a` is assigned the value of `b`, and `b` is assigned the remainder of `a` divided by `b`. This process continues until `b` becomes zero, and at that point, `a` holds the GCD.

---

### **36. Count Words in a String (Topic: Strings)**

**Problem:**
Write a program that counts the number of words in a string.

```python
def count_words(s):
    words = s.split()
    return len(words)

# Test
print(count_words("Hello World"))  # 2
print(count_words("Python programming is fun"))  # 4
```

**Explanation:**
- The `split()` function splits the string into words using spaces as delimiters.
- The `len()` function then returns the number of words in the list.

---

### **37. Infinite Fibonacci Sequence Generator (Topic: Generator Functions)**

**Problem:**
Write a generator function that generates an infinite Fibonacci sequence.

```python
def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test
fib_gen = infinite_fibonacci()
for _ in range(10):
    print(next(fib_gen))
```

**Explanation:**
- This generator function continuously yields the next Fibonacci number.
- We use `yield` to return each number one at a time. The `while True` loop makes this generator infinite, so it will keep generating Fibonacci numbers indefinitely until stopped.

---

### **38. Find Primes Using `filter()` and `lambda` (Topic: filter and lambda)**

**Problem:**
Write a program that filters out all the prime numbers in a list using `filter()` and a `lambda` function.

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = list(range(1, 50))
primes = list(filter(lambda x: is_prime(x), numbers))

print(f"Primes: {primes}")  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

**Explanation:**
- The `is_prime()` function checks if a number is prime by testing divisibility up to the square root of the number.
- The `filter()` function applies `is_prime()` to each element in the `numbers` list, filtering out non-prime numbers.
- The resulting primes are then converted back to a list.

---

### **39. Sum of Even Numbers Using List Comprehension (Topic: Lists and List Comprehension)**

**Problem:**
Write a program that calculates the sum of all even numbers in a list using list comprehension.

```python
def sum_of_evens(numbers):
    return sum([x for x in numbers if x % 2 == 0])

# Test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_evens(numbers))  # 30
```

**Explanation:**
- We use list comprehension to create a list of even numbers from the input list.
- The `sum()` function adds up all the even numbers in the list.

---

### **40. Simple Interest Calculator (Topic: Function Parameters)**

**Problem:**
Write a program that calculates simple interest using a function that takes `principal`, `rate`, and `time` as parameters.

```python
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Test
print(simple_interest(1000, 5, 3))  # 150.0
```

**Explanation:**
- The function calculates the simple interest using the formula `(principal * rate * time) / 100`.
- The `principal`, `rate`, and `time` are passed as parameters to the function.

---

### **41. Factorial of a Number Using Recursion (Topic: Recursion)**

**Problem:**
Write a recursive function that calculates the factorial of a given number.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test
print(factorial(5))  # 120
print(factorial(0))  # 1
```

**Explanation:**
- The function calls itself recursively until it reaches the base case (`n == 0` or `n == 1`).
- For other cases, the function returns `n * factorial(n - 1)`.

---

### **42. Merge Two Dictionaries (Topic: Dictionaries)**

**Problem:**
Write a program that merges two dictionaries into one.

```python
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Test
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # {'a': 1, 'b': 3, 'c': 4}
```

**Explanation:**
- We first create a copy of `dict1` to avoid modifying the original dictionary.
- We then use the `update()` method to add the key-value pairs from `dict2` to the merged dictionary. If a key exists in both dictionaries, the value from `dict2` overwrites the value from `dict

1`.

---

### **43. Random Password Generator (Topic: `random` Package)**

**Problem:**
Write a program that generates a random password of a given length.

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Test
print(generate_password(12))  # Example: '5gZ!tD0@Wq2^'
```

**Explanation:**
- The `string` module provides predefined character sets (`ascii_letters`, `digits`, and `punctuation`).
- We use `random.choice()` to randomly select characters from the combined set and create the password of the specified length.

---

### **44. Handle Multiple Exceptions (Topic: Exception Handling)**

**Problem:**
Write a program that handles multiple exceptions, such as `ValueError` and `ZeroDivisionError`.

```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Test
try:
    print(divide_numbers(10, 0))  # Error: Cannot divide by zero.
    print(divide_numbers("10", 2))  # Error: Invalid input. Please enter numeric values.
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

**Explanation:**
- We handle two specific exceptions (`ZeroDivisionError` and `ValueError`) within the `try` block.
- If either exception occurs, a specific error message is printed.

---

I hope these additional solutions help! We can continue expanding on these concepts with more programs if needed. Let me know if you'd like to explore specific topics or have more problems solved!

Certainly! Let’s continue generating solutions for additional practice programs based on the provided topics.

---

### **31. Using `match` to Classify Day of the Week (Topic: Match Case)**

**Problem:**
Write a program that classifies the day of the week using `match` statements (Python 3.10+).

```python
def classify_day(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

# Test
print(classify_day("Monday"))  # Weekday
print(classify_day("Saturday"))  # Weekend
print(classify_day("Holiday"))  # Invalid day
```

**Explanation:**
- The `match` statement is used to compare the `day` input to known values.
- We use pattern matching to classify the day as a "Weekday", "Weekend", or "Invalid day" based on the input.

---

### **32. Generator for Prime Numbers (Topic: Generator Functions)**

**Problem:**
Write a generator function that yields prime numbers up to a given limit.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# Test
primes = list(prime_numbers(50))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

**Explanation:**
- The `is_prime()` function checks if a number is prime.
- The `prime_numbers()` generator yields prime numbers up to a given limit by iterating and applying the `is_prime()` function.

---

### **33. Filtering Positive Numbers (Topic: filter function)**

**Problem:**
Write a program that uses `filter()` to keep only positive numbers from a list.

```python
def is_positive(x):
    return x > 0

numbers = [-10, 15, 0, 20, -5]
positive_numbers = list(filter(is_positive, numbers))

print(positive_numbers)  # [15, 20]
```

**Explanation:**
- We use `filter()` with the `is_positive()` function to filter out non-positive numbers from the list.
- The result is a list of positive numbers.

---

### **34. Lambda Function for Adding Two Numbers (Topic: Lambda Functions)**

**Problem:**
Write a program that uses a lambda function to add two numbers.

```python
add = lambda x, y: x + y

# Test
print(add(5, 3))  # 8
print(add(10, -2))  # 8
```

**Explanation:**
- A lambda function is used to perform addition of two numbers.
- The lambda function takes two arguments and returns their sum.

---

### **35. List Comprehension to Generate Squares (Topic: Lists)**

**Problem:**
Write a program that generates a list of squares for numbers from 1 to 10 using list comprehension.

```python
squares = [x**2 for x in range(1, 11)]

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Explanation:**
- We use list comprehension to create a list of squares by squaring each number in the range from 1 to 10.

---

### **36. Updating Dictionary Values (Topic: Dictionaries)**

**Problem:**
Write a program that updates the value of a specific key in a dictionary.

```python
def update_dict(d, key, value):
    if key in d:
        d[key] = value
    else:
        print(f"Key '{key}' not found in the dictionary.")
    
    return d

# Test
my_dict = {"a": 1, "b": 2, "c": 3}
print(update_dict(my_dict, "b", 5))  # {'a': 1, 'b': 5, 'c': 3}
print(update_dict(my_dict, "d", 7))  # Key 'd' not found in the dictionary.
```

**Explanation:**
- The `update_dict()` function checks if the key exists in the dictionary.
- If it exists, it updates the value; otherwise, it prints an error message.

---

### **37. Set Difference (Topic: Sets)**

**Problem:**
Write a program that finds the difference between two sets.

```python
def set_difference(set1, set2):
    return set1 - set2

# Test
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set_difference(set1, set2))  # {1, 2}
```

**Explanation:**
- The `-` operator is used to find the difference between `set1` and `set2`, which includes elements in `set1` but not in `set2`.

---

### **38. Exception Handling with Multiple Except Clauses (Topic: Exception Handling)**

**Problem:**
Write a program that handles multiple types of exceptions during file operations.

```python
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading file."
    finally:
        print("Attempted to read the file.")

# Test
print(read_file("example.txt"))  # Depends on the existence of "example.txt"
```

**Explanation:**
- The `try` block attempts to read a file.
- `except` blocks handle specific exceptions: `FileNotFoundError` and `IOError`.
- The `finally` block always executes, providing a message that the attempt to read the file was made.

---

### **39. Use `math` to Calculate Square Root (Topic: math Package)**

**Problem:**
Write a program that calculates the square root of a number using the `math` package.

```python
import math

def calculate_square_root(n):
    if n < 0:
        return "Cannot compute square root of a negative number."
    return math.sqrt(n)

# Test
print(calculate_square_root(25))  # 5.0
print(calculate_square_root(-4))  # Cannot compute square root of a negative number.
```

**Explanation:**
- We use `math.sqrt()` to compute the square root.
- A check is added to handle negative numbers, as the square root of a negative number is not defined in real numbers.

---

### **40. Use `random` to Shuffle a List (Topic: random Package)**

**Problem:**
Write a program that shuffles a list of numbers randomly using the `random` package.

```python
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Test
numbers = [1, 2, 3, 4, 5]
print(shuffle_list(numbers))  # Output will be a shuffled version of the list
```

**Explanation:**
- The `random.shuffle()` method is used to shuffle the list in place.
- The list is modified directly, and the shuffled list is returned.

---

### **41. Find Common Elements in Two Lists (Topic: Lists and Sets)**

**Problem:**
Write a program to find common elements between two lists.

```python
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common_elements(list1, list2))  # [4, 5]
```

**Explanation:**
- Convert the lists to sets and use the `&` operator to find common elements.
- Convert the result back to a list and return it.

---

### **42. Using `for` to Create a Multiplication Table (Topic: for loops)**

**Problem:**
Write a program that generates a multiplication table for numbers 1 through 10.

```python
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()

# Generate multiplication table
multiplication_table()
```

**Explanation:**
- The outer `for` loop iterates through the numbers 1 to 10.
- The inner `for` loop multiplies the current number by each number from 1 to 10 and prints the result.
- The `end=""` parameter in `print()` prevents newline after each number, and `print()` with no arguments moves to the next line.

---

### **43. Use `f-string` to Format a Sentence (Topic: f-strings)**

**Problem:**
Write a program that formats a sentence using `f-strings`.

```python
def format_sentence(name, age, city):
    return f"Hello, my name is {name}. I am {age

} years old and I live in {city}."

# Test
print(format_sentence("Alice", 30, "New York"))
```

**Explanation:**
- We use an f-string to embed variables directly into a formatted string.
- This makes string interpolation more readable and concise.

---

### **44. Compute Factorial Using Recursive Function (Topic: Function Parameters)**

**Problem:**
Write a recursive function to compute the factorial of a number.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test
print(factorial(5))  # 120
```

**Explanation:**
- The `factorial()` function calls itself recursively to compute the factorial of a number.
- Base case: if `n` is 0 or 1, return 1. Otherwise, return `n` times the factorial of `n-1`.

---

### **45. Remove Duplicates from a List (Topic: Lists and Sets)**

**Problem:**
Write a program to remove duplicate elements from a list.

```python
def remove_duplicates(lst):
    return list(set(lst))

# Test
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  # [1, 2, 3, 4, 5]
```

**Explanation:**
- Convert the list to a set to remove duplicates, then convert it back to a list.
- The resulting list contains only unique elements.

---

### **46. Convert a List to a Dictionary (Topic: Lists and Dictionaries)**

**Problem:**
Write a program to convert a list of tuples into a dictionary.

```python
def list_to_dict(tuples_list):
    return dict(tuples_list)

# Test
tuples = [("a", 1), ("b", 2), ("c", 3)]
print(list_to_dict(tuples))  # {'a': 1, 'b': 2, 'c': 3}
```

**Explanation:**
- The `dict()` constructor is used to convert a list of tuples into a dictionary.
- Each tuple is treated as a key-value pair.

---

### **47. Check if a Key Exists in a Dictionary (Topic: Dictionaries)**

**Problem:**
Write a program to check if a key exists in a dictionary.

```python
def key_exists(d, key):
    return key in d

# Test
my_dict = {"a": 1, "b": 2, "c": 3}
print(key_exists(my_dict, "b"))  # True
print(key_exists(my_dict, "d"))  # False
```

**Explanation:**
- Use the `in` operator to check if the key is present in the dictionary.
- The function returns `True` if the key exists, otherwise `False`.

---

### **48. Count Occurrences of Each Character in a String (Topic: Strings)**

**Problem:**
Write a program that counts the occurrences of each character in a string.

```python
def char_count(text):
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

# Test
print(char_count("hello world"))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

**Explanation:**
- Iterate through each character in the string and use a dictionary to count occurrences.
- The function returns a dictionary where keys are characters and values are counts.

---

### **49. Find Maximum and Minimum in a List (Topic: Lists)**

**Problem:**
Write a program to find the maximum and minimum values in a list.

```python
def find_max_min(lst):
    return max(lst), min(lst)

# Test
numbers = [10, 20, 30, 40, 50]
print(find_max_min(numbers))  # (50, 10)
```

**Explanation:**
- Use the `max()` and `min()` functions to find the largest and smallest values in the list.
- The function returns a tuple with both maximum and minimum values.

---

### **50. Calculate Compound Interest (Topic: Functions)**

**Problem:**
Write a function to calculate compound interest given principal, rate, and time.

```python
def compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

# Test
principal = 1000
rate = 0.05
time = 5
n = 4
print(compound_interest(principal, rate, time, n))  # 1283.68
```

**Explanation:**
- The formula for compound interest is used: `A = P * (1 + r / n) ** (n * t)`
- `P` is the principal, `r` is the annual interest rate, `n` is the number of times interest is compounded per year, and `t` is the time in years.

---

These solutions should provide ample practice for students working with various Python concepts. Feel free to request more problems or detailed explanations on specific topics!

Certainly! Let's continue with more solutions covering a range of Python topics.

---

### **51. Count Words in a String (Topic: Strings)**

**Problem:**
Write a program that counts the number of words in a string.

```python
def count_words(text):
    words = text.split()
    return len(words)

# Test
text = "Python programming is fun and educational."
print(count_words(text))  # 6
```

**Explanation:**
- We use `split()` to break the string into words.
- `len()` then counts the number of words in the resulting list.

---

### **52. Using `match` to Identify a Month (Topic: Match Case)**

**Problem:**
Write a program that identifies the month from its number using `match` statements.

```python
def identify_month(month_number):
    match month_number:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return "Invalid month number"

# Test
print(identify_month(5))  # May
print(identify_month(13))  # Invalid month number
```

**Explanation:**
- The `match` statement matches the month number to its corresponding month name.
- Handles invalid month numbers with a default case.

---

### **53. Flatten a List of Lists (Topic: Lists)**

**Problem:**
Write a program to flatten a list of lists into a single list.

```python
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Test
nested_list = [[1, 2, 3], [4, 5], [6]]
print(flatten_list(nested_list))  # [1, 2, 3, 4, 5, 6]
```

**Explanation:**
- We use list comprehension to iterate through each sublist and then through each item in the sublist.
- This flattens the nested list into a single list.

---

### **54. Generate a Fibonacci Sequence Using a Generator (Topic: Generator Functions)**

**Problem:**
Write a generator function to yield a Fibonacci sequence up to a given number of terms.

```python
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Test
print(list(fibonacci_generator(7)))  # [0, 1, 1, 2, 3, 5, 8]
```

**Explanation:**
- The generator yields Fibonacci numbers up to `n` terms.
- Each call to `yield` produces the next number in the sequence.

---

### **55. Use `map()` to Convert Strings to Integers (Topic: map function)**

**Problem:**
Write a program that converts a list of string numbers to integers using `map()`.

```python
def to_int(s):
    return int(s)

strings = ["1", "2", "3", "4"]
integers = list(map(to_int, strings))

print(integers)  # [1, 2, 3, 4]
```

**Explanation:**
- The `map()` function applies `to_int()` to each string in the list.
- The result is a list of integers.

---

### **56. Remove Duplicates from a List Using Set (Topic: Sets)**

**Problem:**
Write a program to remove duplicates from a list using a set.

```python
def remove_duplicates(lst):
    return list(set(lst))

# Test
lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))  # [1, 2, 3, 4, 5]
```

**Explanation:**
- Convert the list to a set to automatically remove duplicates.
- Convert the set back to a list.

---

### **57. Use `filter()` to Keep Strings Longer Than 3 Characters (Topic: filter function)**

**Problem:**
Write a program that filters out strings longer than 3 characters using `filter()`.

```python
def longer_than_three(s):
    return len(s) > 3

strings = ["hi", "hello", "world", "ok"]
filtered_strings = list(filter(longer_than_three, strings))

print(filtered_strings)  # ['hello', 'world']
```

**Explanation:**
- The `filter()` function uses `longer_than_three()` to select strings longer than 3 characters.
- Converts the result to a list.

---

### **58. Calculate the Greatest Common Divisor (GCD) (Topic: Math Package)**

**Problem:**
Write a program to calculate the GCD of two numbers using the `math` package.

```python
import math

def gcd(a, b):
    return math.gcd(a, b)

# Test
print(gcd(48, 18))  # 6
```

**Explanation:**
- The `math.gcd()` function computes the greatest common divisor of two numbers.

---

### **59. Implement a Basic Voting System (Topic: if-elif-else)**

**Problem:**
Write a program that simulates a basic voting system where users can vote for candidates.

```python
def voting_system(vote):
    candidates = {
        "Alice": 0,
        "Bob": 0,
        "Charlie": 0
    }
    
    if vote in candidates:
        candidates[vote] += 1
        return f"Vote counted for {vote}"
    else:
        return "Invalid candidate"

# Test
print(voting_system("Alice"))  # Vote counted for Alice
print(voting_system("Dave"))  # Invalid candidate
```

**Explanation:**
- The program maintains a dictionary of candidates.
- Votes are counted if the candidate exists; otherwise, it reports an invalid candidate.

---

### **60. Create a Function with Default Parameters (Topic: Function Parameters)**

**Problem:**
Write a function that greets a user with a default message if no name is provided.

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

# Test
print(greet())  # Hello, Guest!
print(greet("Alice"))  # Hello, Alice!
```

**Explanation:**
- The `greet()` function has a default parameter value of "Guest".
- If no argument is passed, it uses the default value.

---

### **61. Use a While Loop to Calculate the Sum of Numbers (Topic: while loops)**

**Problem:**
Write a program that uses a `while` loop to calculate the sum of numbers from 1 to 100.

```python
def sum_numbers(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Test
print(sum_numbers(100))  # 5050
```

**Explanation:**
- The `while` loop adds numbers from 1 to `n` to a `total` variable.
- The loop continues until `i` exceeds `n`.

---

### **62. Use `try` to Handle File Not Found Exception (Topic: Exception Handling)**

**Problem:**
Write a program that attempts to open a file and handles the `FileNotFoundError` exception.

```python
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

# Test
print(read_file("nonexistent_file.txt"))  # File not found.
```

**Explanation:**
- The program tries to open and read a file.
- If the file is not found, it handles the `FileNotFoundError` and returns a message.

---

### **63. Use List Comprehension to Filter Even Numbers (Topic: Lists)**

**Problem:**
Write a program that filters out even numbers from a list using list comprehension.

```python
def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# Test
numbers = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(numbers))  # [2, 4, 6]
```

**Explanation:**
- List comprehension is used to create a new list containing only even numbers from the original list.

---

### **64. Use a Lambda Function to Find the Maximum Value (Topic: Lambda Functions)**

**Problem:**
Write a program that uses a lambda function to find the maximum value in a list.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_value = max(numbers, key=lambda x: x)

print(max_value)  # 9
```

**Explanation:**
- The `max()` function with a lambda function is used to find the maximum value in the list.
- The lambda function simply returns the value itself for comparison.

---

### **65. Create a Set from a List of Tuples (Topic

: Tuples and Sets)**

**Problem:**
Write a program that converts a list of tuples into a set of tuples.

```python
def tuples_to_set(tuples_list):
    return set(tuples_list)

# Test
tuples = [(1, 2), (2, 3), (3, 4), (1, 2)]
print(tuples_to_set(tuples))  # {(1, 2), (2, 3), (3, 4)}
```

**Explanation:**
- The `set()` constructor is used to convert a list of tuples into a set, removing duplicate tuples.

---

### **66. Check if a Number is Prime (Topic: Conditional Operators)**

**Problem:**
Write a program to check if a number is prime using conditional operators.

```python
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Test
print(is_prime(11))  # True
print(is_prime(12))  # False
```

**Explanation:**
- A number is prime if it's greater than 1 and not divisible by any number other than 1 and itself.
- We use conditional operators to check divisibility.

---

### **67. Use `map()` to Compute Square of Each Number (Topic: map function)**

**Problem:**
Write a program that computes the square of each number in a list using `map()`.

```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))

print(squares)  # [1, 4, 9, 16, 25]
```

**Explanation:**
- The `map()` function applies the `square()` function to each element in the list.
- The result is a list of squared numbers.

---

### **68. Extract Numbers from a String (Topic: Strings)**

**Problem:**
Write a program to extract all numbers from a string.

```python
import re

def extract_numbers(text):
    return re.findall(r'\d+', text)

# Test
text = "There are 24 apples and 30 oranges."
print(extract_numbers(text))  # ['24', '30']
```

**Explanation:**
- The `re.findall()` function is used to find all sequences of digits in the string.
- It returns a list of numbers as strings.

---

### **69. Using `any()` to Check for True Values (Topic: Conditional Operators)**

**Problem:**
Write a program to check if any value in a list is True using `any()`.

```python
values = [False, False, True, False]
result = any(values)

print(result)  # True
```

**Explanation:**
- The `any()` function returns `True` if at least one element in the list is `True`.

---

### **70. Using `all()` to Check if All Values are True (Topic: Conditional Operators)**

**Problem:**
Write a program to check if all values in a list are True using `all()`.

```python
values = [True, True, True]
result = all(values)

print(result)  # True

values = [True, False, True]
result = all(values)

print(result)  # False
```

**Explanation:**
- The `all()` function returns `True` if all elements in the list are `True`.

---

### **71. Implement a Simple Calculator (Topic: if-elif-else)**

**Problem:**
Write a program that implements a simple calculator with operations: addition, subtraction, multiplication, and division.

```python
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid operation"

# Test
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # Division by zero error
```

**Explanation:**
- The `calculator()` function performs different operations based on the provided operator.
- Handles division by zero and invalid operations.

---

### **72. Calculate Power Using `math.pow()` (Topic: Math Package)**

**Problem:**
Write a program to calculate the power of a number using `math.pow()`.

```python
import math

def calculate_power(base, exponent):
    return math.pow(base, exponent)

# Test
print(calculate_power(2, 3))  # 8.0
print(calculate_power(5, 2))  # 25.0
```

**Explanation:**
- The `math.pow()` function is used to raise `base` to the power of `exponent`.

---

### **73. Use List Comprehension to Create a List of Tuples (Topic: Lists)**

**Problem:**
Write a program that creates a list of tuples from a list of numbers, where each tuple contains the number and its square.

```python
numbers = [1, 2, 3, 4, 5]
list_of_tuples = [(x, x ** 2) for x in numbers]

print(list_of_tuples)  # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**Explanation:**
- List comprehension is used to create tuples of each number and its square.

---

### **74. Check If a String Contains Only Digits (Topic: Strings)**

**Problem:**
Write a program to check if a string contains only digits.

```python
def is_digits(s):
    return s.isdigit()

# Test
print(is_digits("12345"))  # True
print(is_digits("123a5"))  # False
```

**Explanation:**
- The `isdigit()` method returns `True` if all characters in the string are digits.

---

### **75. Calculate the Mean of a List Using `sum()` and `len()` (Topic: Lists)**

**Problem:**
Write a program to calculate the mean of a list of numbers.

```python
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

# Test
numbers = [10, 20, 30, 40, 50]
print(calculate_mean(numbers))  # 30.0
```

**Explanation:**
- The mean is calculated by dividing the sum of the list by the number of elements.
- Handles empty lists by returning 0.

---

These additional problems should provide a robust set of practice exercises for students across a variety of Python topics. If you need further elaboration or more examples, feel free to ask!

Absolutely! Let's continue generating more solutions for various programming assignments.

---

### **76. Create a Function to Count Vowels in a String (Topic: Strings)**

**Problem:**
Write a program to count the number of vowels in a string.

```python
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

# Test
print(count_vowels("Hello World"))  # 3
```

**Explanation:**
- Convert the string to lowercase for case-insensitive counting.
- Use a generator expression within `sum()` to count vowels.

---

### **77. Use `try` to Handle ZeroDivisionError (Topic: Exception Handling)**

**Problem:**
Write a program that divides two numbers and handles division by zero.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Cannot divide by zero.
```

**Explanation:**
- The `try` block attempts to perform the division.
- The `except` block handles the `ZeroDivisionError` and provides a user-friendly message.

---

### **78. Check if All Elements in a List are Unique (Topic: Lists)**

**Problem:**
Write a program to check if all elements in a list are unique.

```python
def all_unique(lst):
    return len(lst) == len(set(lst))

# Test
print(all_unique([1, 2, 3, 4, 5]))  # True
print(all_unique([1, 2, 2, 4, 5]))  # False
```

**Explanation:**
- Convert the list to a set, which removes duplicates.
- Compare the length of the original list to the length of the set.

---

### **79. Filter Even Numbers Using `filter()` (Topic: filter function)**

**Problem:**
Write a program that filters out even numbers from a list using `filter()`.

```python
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # [2, 4, 6]
```

**Explanation:**
- The `filter()` function applies `is_even()` to each number and keeps only even numbers.

---

### **80. Use `map()` to Convert Temperature from Celsius to Fahrenheit (Topic: map function)**

**Problem:**
Write a program that converts a list of temperatures in Celsius to Fahrenheit using `map()`.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

print(fahrenheit_temps)  # [32.0, 68.0, 98.6, 212.0]
```

**Explanation:**
- The `map()` function applies `celsius_to_fahrenheit()` to each temperature in the list.

---

### **81. Create a Function with Variable Number of Arguments (Topic: Function Parameters)**

**Problem:**
Write a function that calculates the sum of a variable number of arguments.

```python
def sum_all(*args):
    return sum(args)

# Test
print(sum_all(1, 2, 3, 4))  # 10
print(sum_all(5, 10, 15))   # 30
```

**Explanation:**
- Use `*args` to accept a variable number of arguments.
- `sum()` calculates the sum of all arguments.

---

### **82. Create a Function to Generate Random Password (Topic: Random Package)**

**Problem:**
Write a function that generates a random password with letters and digits.

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Test
print(generate_password(10))  # Example: 'a9B7kL2QpX'
```

**Explanation:**
- Use `string.ascii_letters` and `string.digits` to get possible characters.
- `random.choice()` picks a random character for each position in the password.

---

### **83. Use List Comprehension to Filter Positive Numbers (Topic: Lists)**

**Problem:**
Write a program that filters out positive numbers from a list using list comprehension.

```python
def filter_positive(lst):
    return [x for x in lst if x > 0]

# Test
numbers = [-10, -5, 0, 5, 10]
print(filter_positive(numbers))  # [5, 10]
```

**Explanation:**
- List comprehension filters out positive numbers from the list.

---

### **84. Create a Tuple with Repeated Elements (Topic: Tuples)**

**Problem:**
Write a program to create a tuple with repeated elements.

```python
def repeat_element(element, times):
    return (element,) * times

# Test
print(repeat_element('hello', 3))  # ('hello', 'hello', 'hello')
print(repeat_element(5, 4))        # (5, 5, 5, 5)
```

**Explanation:**
- Create a tuple with a repeated element using multiplication.

---

### **85. Generate Random Float Numbers (Topic: Random Package)**

**Problem:**
Write a program that generates a list of random float numbers within a given range.

```python
import random

def generate_random_floats(count, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

# Test
print(generate_random_floats(5, 1.0, 10.0))  # Example: [1.234, 8.567, 4.123, 7.890, 2.345]
```

**Explanation:**
- Use `random.uniform()` to generate a random float within the specified range.

---

### **86. Count Occurrences of a Substring in a String (Topic: Strings)**

**Problem:**
Write a program that counts the occurrences of a substring in a string.

```python
def count_substring(text, substring):
    return text.count(substring)

# Test
print(count_substring("banana", "na"))  # 2
print(count_substring("hello world", "o"))  # 2
```

**Explanation:**
- Use the `count()` method of strings to count occurrences of a substring.

---

### **87. Implement a Simple Bank Account Class (Topic: Object-Oriented Programming)**

**Problem:**
Write a class to represent a simple bank account with methods to deposit, withdraw, and check balance.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount

    def check_balance(self):
        return self.balance

# Test
account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.check_balance())  # 50
```

**Explanation:**
- The `BankAccount` class has methods to deposit, withdraw, and check balance.
- Handles insufficient funds during withdrawal.

---

### **88. Use `try` to Handle ValueError for Conversion (Topic: Exception Handling)**

**Problem:**
Write a program that attempts to convert a string to an integer and handles `ValueError`.

```python
def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Invalid integer."

# Test
print(convert_to_int("123"))  # 123
print(convert_to_int("abc"))  # Invalid integer.
```

**Explanation:**
- The `try` block attempts to convert the string to an integer.
- The `except` block handles the `ValueError` and returns an error message.

---

### **89. Find the Intersection of Two Sets (Topic: Sets)**

**Problem:**
Write a program that finds the intersection of two sets.

```python
def intersection(set1, set2):
    return set1 & set2

# Test
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(intersection(set_a, set_b))  # {3, 4}
```

**Explanation:**
- Use the `&` operator to find common elements between two sets.

---

### **90. Implement a Simple To-Do List (Topic: Lists and Dictionaries)**

**Problem:**
Write a program to manage a simple to-do list using a dictionary.

```python
def add_task(todo_list, task):
    todo_list.append(task)
    return todo_list

def remove_task(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
    return todo_list

def list_tasks(todo_list):
    return todo_list

# Test
tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Call mom")
tasks = remove_task(tasks, "Buy groceries")
print(list_tasks(tasks))  # ['Call mom']
```

**Explanation:**
- Use list operations to manage tasks

 in a simple to-do list.

---

### **91. Generate a Random Integer within a Range (Topic: Random Package)**

**Problem:**
Write a program to generate a random integer within a given range.

```python
import random

def generate_random_int(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

# Test
print(generate_random_int(1, 100))  # Example: 42
```

**Explanation:**
- Use `random.randint()` to generate a random integer within the specified range.

---

### **92. Create a Function to Capitalize Each Word in a String (Topic: Strings)**

**Problem:**
Write a program that capitalizes each word in a string.

```python
def capitalize_words(text):
    return text.title()

# Test
print(capitalize_words("hello world"))  # Hello World
```

**Explanation:**
- Use the `title()` method to capitalize the first letter of each word.

---

### **93. Implement a Function to Reverse a List (Topic: Lists)**

**Problem:**
Write a program to reverse a list.

```python
def reverse_list(lst):
    return lst[::-1]

# Test
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

**Explanation:**
- Use slicing with `[::-1]` to reverse the list.

---

### **94. Calculate the Factorial of a Number Using `math.factorial()` (Topic: Math Package)**

**Problem:**
Write a program to calculate the factorial of a number using `math.factorial()`.

```python
import math

def calculate_factorial(n):
    return math.factorial(n)

# Test
print(calculate_factorial(5))  # 120
```

**Explanation:**
- Use `math.factorial()` to compute the factorial of a number.

---

### **95. Find the Longest Word in a List (Topic: Lists)**

**Problem:**
Write a program to find the longest word in a list.

```python
def find_longest_word(words):
    return max(words, key=len)

# Test
print(find_longest_word(["apple", "banana", "cherry"]))  # banana
```

**Explanation:**
- Use `max()` with `key=len` to find the longest word in the list.

---

### **96. Create a Function to Merge Two Dictionaries (Topic: Dictionaries)**

**Problem:**
Write a program to merge two dictionaries.

```python
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Test
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
print(merge_dicts(dict_a, dict_b))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

**Explanation:**
- Use dictionary unpacking to merge two dictionaries.

---

### **97. Use `match-case` to Match Days of the Week (Topic: match-case)**

**Problem:**
Write a program to match days of the week using `match-case`.

```python
def day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

# Test
print(day_type("Monday"))  # Weekday
print(day_type("Sunday"))  # Weekend
```

**Explanation:**
- The `match-case` statement is used to handle different days of the week, categorizing them as weekdays or weekends.

---

### **98. Create a Function to Check for Palindromes (Topic: Strings)**

**Problem:**
Write a program to check if a string is a palindrome.

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False
```

**Explanation:**
- Convert the string to lowercase and remove spaces.
- Check if the string reads the same backward.

---

### **99. Calculate the Sum of Squares of a List Using `sum()` and List Comprehension (Topic: Lists)**

**Problem:**
Write a program to calculate the sum of squares of elements in a list using `sum()` and list comprehension.

```python
def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

# Test
print(sum_of_squares([1, 2, 3, 4]))  # 30
```

**Explanation:**
- Use list comprehension to calculate squares and `sum()` to find the total.

---

### **100. Create a Function to Sort a Dictionary by Values (Topic: Dictionaries)**

**Problem:**
Write a program to sort a dictionary by its values.

```python
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Test
my_dict = {'apple': 2, 'banana': 1, 'cherry': 3}
print(sort_dict_by_values(my_dict))  # {'banana': 1, 'apple': 2, 'cherry': 3}
```

**Explanation:**
- Use `sorted()` with a lambda function to sort dictionary items by their values.

---

### **101. Generate a Random Float within a Range (Topic: Random Package)**

**Problem:**
Write a program that generates a random float number within a specific range.

```python
import random

def generate_random_float(lower_bound, upper_bound):
    return random.uniform(lower_bound, upper_bound)

# Test
print(generate_random_float(1.5, 5.5))  # Example: 3.276
```

**Explanation:**
- Use `random.uniform()` to generate a random float within the specified range.

---

### **102. Implement a Function to Remove Duplicates from a List (Topic: Lists)**

**Problem:**
Write a program that removes duplicates from a list.

```python
def remove_duplicates(lst):
    return list(set(lst))

# Test
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
```

**Explanation:**
- Convert the list to a set to remove duplicates and then back to a list.

---

### **103. Check if Two Strings Are Anagrams (Topic: Strings)**

**Problem:**
Write a program to check if two strings are anagrams.

```python
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Test
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
```

**Explanation:**
- Sort both strings and compare them to determine if they are anagrams.

---

### **104. Create a Function to Find the Maximum Element in a List (Topic: Lists)**

**Problem:**
Write a program to find the maximum element in a list.

```python
def find_max(lst):
    return max(lst) if lst else None

# Test
print(find_max([1, 2, 3, 4, 5]))  # 5
print(find_max([]))               # None
```

**Explanation:**
- Use the `max()` function to find the largest element in the list.
- Handle empty lists by returning `None`.

---

### **105. Use List Comprehension to Generate a List of Squares (Topic: Lists)**

**Problem:**
Write a program that generates a list of squares from 1 to 10 using list comprehension.

```python
squares = [x ** 2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Explanation:**
- Use list comprehension to generate squares of numbers from 1 to 10.

---

These additional problems provide a wide range of practice opportunities on various Python topics, challenging students to apply their knowledge in different ways. If you have more topics or need further elaboration, let me know!

Certainly! Let’s continue with more programming assignments and solutions.

---

### **106. Convert a List of Strings to Uppercase (Topic: Strings)**

**Problem:**
Write a program that converts all strings in a list to uppercase.

```python
def to_uppercase(strings):
    return [s.upper() for s in strings]

# Test
words = ["hello", "world", "python"]
print(to_uppercase(words))  # ['HELLO', 'WORLD', 'PYTHON']
```

**Explanation:**
- Use list comprehension to convert each string in the list to uppercase using the `upper()` method.

---

### **107. Implement a Function to Count Words in a Sentence (Topic: Strings)**

**Problem:**
Write a program to count the number of words in a sentence.

```python
def count_words(sentence):
    return len(sentence.split())

# Test
print(count_words("This is a simple sentence."))  # 5
```

**Explanation:**
- Use the `split()` method to split the sentence into words and then count the number of words.

---

### **108. Use `any()` to Check if Any Element is Negative (Topic: Conditional Operators)**

**Problem:**
Write a program that checks if any element in a list is negative using `any()`.

```python
def has_negative(numbers):
    return any(n < 0 for n in numbers)

# Test
print(has_negative([1, 2, 3, -4, 5]))  # True
print(has_negative([1, 2, 3, 4, 5]))   # False
```

**Explanation:**
- Use `any()` with a generator expression to check if any number in the list is negative.

---

### **109. Calculate the Sum of All Even Numbers in a List (Topic: Lists)**

**Problem:**
Write a program to calculate the sum of all even numbers in a list.

```python
def sum_of_evens(numbers):
    return sum(n for n in numbers if n % 2 == 0)

# Test
print(sum_of_evens([1, 2, 3, 4, 5, 6]))  # 12
```

**Explanation:**
- Use a generator expression within `sum()` to add only even numbers from the list.

---

### **110. Implement a Function to Find the Common Elements Between Two Lists (Topic: Lists)**

**Problem:**
Write a program to find the common elements between two lists.

```python
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Test
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
```

**Explanation:**
- Convert both lists to sets and use the `&` operator to find common elements, then convert the result back to a list.

---

### **111. Create a Function to Remove Duplicates from a String (Topic: Strings)**

**Problem:**
Write a program to remove duplicate characters from a string while preserving the original order.

```python
def remove_duplicates(s):
    seen = set()
    return ''.join(char for char in s if not (char in seen or seen.add(char)))

# Test
print(remove_duplicates("programming"))  # 'progamin'
```

**Explanation:**
- Use a set to track seen characters and list comprehension to filter out duplicates while preserving order.

---

### **112. Implement a Function to Merge Two Lists Alternately (Topic: Lists)**

**Problem:**
Write a program to merge two lists alternately.

```python
def merge_alternately(list1, list2):
    return [item for pair in zip(list1, list2) for item in pair] + list1[len(list2):] + list2[len(list1):]

# Test
print(merge_alternately([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
```

**Explanation:**
- Use `zip()` to pair elements from both lists and flatten the result using list comprehension.
- Append any remaining elements from the longer list.

---

### **113. Calculate the GCD of Two Numbers (Topic: Math Package)**

**Problem:**
Write a program to calculate the greatest common divisor (GCD) of two numbers using the `math.gcd()` function.

```python
import math

def calculate_gcd(a, b):
    return math.gcd(a, b)

# Test
print(calculate_gcd(48, 18))  # 6
```

**Explanation:**
- Use `math.gcd()` to compute the GCD of two numbers.

---

### **114. Filter Odd Numbers Using `filter()` (Topic: filter function)**

**Problem:**
Write a program that filters out odd numbers from a list using `filter()`.

```python
def is_odd(n):
    return n % 2 != 0

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(is_odd, numbers))

print(odd_numbers)  # [1, 3, 5]
```

**Explanation:**
- The `filter()` function applies `is_odd()` to each element and keeps only odd numbers.

---

### **115. Create a Function to Return the Index of an Element in a List (Topic: Lists)**

**Problem:**
Write a program to return the index of a specified element in a list.

```python
def find_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return "Element not found."

# Test
print(find_index([10, 20, 30, 40], 30))  # 2
print(find_index([10, 20, 30, 40], 50))  # Element not found.
```

**Explanation:**
- Use the `index()` method to find the index of the element.
- Handle the case where the element is not found using a `try`-`except` block.

---

### **116. Implement a Function to Count the Number of Characters in Each Word of a String (Topic: Strings)**

**Problem:**
Write a program to count the number of characters in each word of a string.

```python
def count_chars_per_word(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

# Test
print(count_chars_per_word("Hello world Python programming"))  
# {'Hello': 5, 'world': 5, 'Python': 6, 'programming': 11}
```

**Explanation:**
- Split the sentence into words and use a dictionary comprehension to count the characters in each word.

---

### **117. Create a Function to Return the Fibonacci Sequence Up to a Given Number (Topic: Functions)**

**Problem:**
Write a program to return the Fibonacci sequence up to a given number.

```python
def fibonacci_up_to(max_num):
    a, b = 0, 1
    sequence = []
    while a <= max_num:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test
print(fibonacci_up_to(10))  # [0, 1, 1, 2, 3, 5, 8]
```

**Explanation:**
- Generate Fibonacci numbers and add them to a list until reaching the maximum number.

---

### **118. Use `lambda` to Sort a List of Tuples by the Second Element (Topic: lambda Functions)**

**Problem:**
Write a program that sorts a list of tuples by the second element using `lambda`.

```python
def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

# Test
print(sort_by_second_element([(1, 3), (2, 2), (3, 1)]))  # [(3, 1), (2, 2), (1, 3)]
```

**Explanation:**
- Use the `sorted()` function with a `lambda` function as the key to sort tuples based on their second element.

---

### **119. Create a Function to Return the Union of Two Sets (Topic: Sets)**

**Problem:**
Write a program to return the union of two sets.

```python
def union_of_sets(set1, set2):
    return set1 | set2

# Test
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(union_of_sets(set_a, set_b))  # {1, 2, 3, 4, 5}
```

**Explanation:**
- Use the `|` operator to find the union of two sets.

---

### **120. Use `math.sqrt()` to Calculate Square Root (Topic: Math Package)**

**Problem:**
Write a program to calculate the square root of a number using `math.sqrt()`.

```python
import math

def calculate_sqrt(n):
    return math.sqrt(n)

# Test
print(calculate_sqrt(16))  # 4.0
print(calculate_sqrt(25))  # 5.0
```

**Explanation:**
- Use `math.sqrt()` to compute the square root of a number.

---

### **121. Create a Function to Return the Difference Between Two Sets (Topic: Sets)**

**Problem:**
Write a program to return the difference between two sets.

```python
def difference_of_sets(set1, set2

):
    return set1 - set2

# Test
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(difference_of_sets(set_a, set_b))  # {1, 2}
```

**Explanation:**
- Use the `-` operator to find the difference between two sets.

---

### **122. Implement a Function to Extract Even Numbers from a List Using `filter()` (Topic: filter function)**

**Problem:**
Write a program that extracts even numbers from a list using `filter()`.

```python
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # [2, 4, 6]
```

**Explanation:**
- Define a function `is_even()` to identify even numbers and use `filter()` to extract them from the list.

---

### **123. Create a Function to Sort a List of Strings by Length (Topic: Lists)**

**Problem:**
Write a program to sort a list of strings by their length.

```python
def sort_by_length(strings):
    return sorted(strings, key=len)

# Test
print(sort_by_length(["apple", "banana", "kiwi", "cherry"]))  # ['kiwi', 'apple', 'banana', 'cherry']
```

**Explanation:**
- Use the `sorted()` function with `key=len` to sort strings by their length.

---

### **124. Use `map()` to Convert a List of Strings to Integers (Topic: map function)**

**Problem:**
Write a program to convert a list of string numbers to integers using `map()`.

```python
def convert_to_int(s):
    return int(s)

str_numbers = ["1", "2", "3", "4"]
int_numbers = list(map(convert_to_int, str_numbers))

print(int_numbers)  # [1, 2, 3, 4]
```

**Explanation:**
- Use `map()` to apply `convert_to_int()` to each element of the list.

---

### **125. Implement a Function to Count Vowels in a String (Topic: Strings)**

**Problem:**
Write a program to count the number of vowels in a string.

```python
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

# Test
print(count_vowels("Hello World"))  # 3
```

**Explanation:**
- Use a generator expression to count vowels in the string, considering case-insensitivity.

---

### **126. Create a Function to Return the Difference of Two Lists (Topic: Lists)**

**Problem:**
Write a program to return the difference of two lists.

```python
def list_difference(list1, list2):
    return list(set(list1) - set(list2))

# Test
print(list_difference([1, 2, 3, 4], [3, 4, 5, 6]))  # [1, 2]
```

**Explanation:**
- Convert lists to sets and find the difference, then convert back to a list.

---

### **127. Create a Function to Find the Intersection of Two Lists (Topic: Lists)**

**Problem:**
Write a program to find the intersection of two lists.

```python
def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

# Test
print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
```

**Explanation:**
- Use set intersection to find common elements between two lists.

---

### **128. Implement a Function to Check for Prime Numbers (Topic: Functions)**

**Problem:**
Write a program to check if a number is prime.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(11))  # True
print(is_prime(15))  # False
```

**Explanation:**
- Check divisibility up to the square root of the number to determine if it’s prime.

---

### **129. Use `lambda` to Compute the Square of Numbers (Topic: lambda Functions)**

**Problem:**
Write a program that uses `lambda` to compute the square of numbers in a list.

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

print(squares)  # [1, 4, 9, 16, 25]
```

**Explanation:**
- Use `map()` with a `lambda` function to compute squares of numbers in the list.

---

### **130. Implement a Function to Find the Longest Common Prefix of a List of Strings (Topic: Strings)**

**Problem:**
Write a program to find the longest common prefix in a list of strings.

```python
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test
print(longest_common_prefix(["flower", "flow", "flight"]))  # 'fl'
print(longest_common_prefix(["dog", "racecar", "car"]))     # ''
```

**Explanation:**
- Start with the first string as the prefix and check each subsequent string. Reduce the prefix length until all strings share the prefix.

---

### **131. Create a Function to Find the Maximum of Three Numbers (Topic: Conditional Operators)**

**Problem:**
Write a program to find the maximum of three numbers.

```python
def max_of_three(a, b, c):
    return max(a, b, c)

# Test
print(max_of_three(10, 20, 30))  # 30
print(max_of_three(5, 2, 9))    # 9
```

**Explanation:**
- Use the `max()` function to find the largest of three numbers.

---

### **132. Generate a Random Choice from a List (Topic: Random Package)**

**Problem:**
Write a program to select a random item from a list.

```python
import random

def random_choice(lst):
    return random.choice(lst)

# Test
print(random_choice([10, 20, 30, 40, 50]))  # Example: 30
```

**Explanation:**
- Use `random.choice()` to pick a random element from the list.

---

### **133. Implement a Function to Compute the Power of a Number (Topic: Functions)**

**Problem:**
Write a program to compute the power of a number.

```python
def power(base, exponent):
    return base ** exponent

# Test
print(power(2, 3))  # 8
print(power(5, 4))  # 625
```

**Explanation:**
- Use the exponentiation operator `**` to compute the power of a number.

---

### **134. Create a Function to Return the Last N Elements of a List (Topic: Lists)**

**Problem:**
Write a program to return the last N elements of a list.

```python
def last_n_elements(lst, n):
    return lst[-n:]

# Test
print(last_n_elements([1, 2, 3, 4, 5], 3))  # [3, 4, 5]
```

**Explanation:**
- Use slicing to get the last N elements of the list.

---

### **135. Implement a Function to Check for Even or Odd Numbers Using `if-else` (Topic: if-elif-else)**

**Problem:**
Write a program to check if a number is even or odd.

```python
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test
print(even_or_odd(10))  # Even
print(even_or_odd(7))   # Odd
```

**Explanation:**
- Use an `if-else` statement to check the remainder when dividing by 2 to determine even or odd.

---

### **136. Create a Function to Return All Unique Elements in a List (Topic: Lists)**

**Problem:**
Write a program to return all unique elements in a list.

```python
def unique_elements(lst):
    return list(set(lst))

# Test
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
```

**Explanation:**
- Convert the list to a set to remove duplicates and then back to a list.

---

### **137. Implement a Function to Filter Numbers Greater Than a Given Value Using `filter()` (Topic: filter function)**

**Problem:**
Write a program to filter numbers greater than a given value from a list.

```python
def greater_than(value, numbers):
    return list(filter(lambda x: x > value, numbers))

# Test
print(greater_than(3, [1, 4, 5, 2, 8]))  # [4

, 5, 8]
```

**Explanation:**
- Use `filter()` with a `lambda` function to keep numbers greater than the specified value.

---

### **138. Create a Function to Merge Two Dictionaries (Topic: Dictionaries)**

**Problem:**
Write a program to merge two dictionaries.

```python
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# Test
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # {'a': 1, 'b': 3, 'c': 4}
```

**Explanation:**
- Use `copy()` to create a copy of the first dictionary and then use `update()` to merge the second dictionary into it.

---

### **139. Implement a Function to Calculate the Sum of Squares of a List of Numbers (Topic: Lists)**

**Problem:**
Write a program to calculate the sum of the squares of a list of numbers.

```python
def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

# Test
print(sum_of_squares([1, 2, 3, 4]))  # 30
```

**Explanation:**
- Use a generator expression to compute squares of each number and sum them up.

---

### **140. Create a Function to Find the Minimum of a List (Topic: Lists)**

**Problem:**
Write a program to find the minimum value in a list.

```python
def find_minimum(lst):
    return min(lst)

# Test
print(find_minimum([5, 3, 9, 1, 7]))  # 1
```

**Explanation:**
- Use the `min()` function to find the smallest element in the list.

---

### **141. Implement a Function to Convert a List of Strings to Uppercase Using `map()` (Topic: map function)**

**Problem:**
Write a program to convert all strings in a list to uppercase using `map()`.

```python
def to_uppercase(s):
    return s.upper()

strings = ["hello", "world", "python"]
uppercase_strings = list(map(to_uppercase, strings))

print(uppercase_strings)  # ['HELLO', 'WORLD', 'PYTHON']
```

**Explanation:**
- Use `map()` with `to_uppercase` to apply uppercase conversion to each string.

---

### **142. Create a Function to Remove All Occurrences of a Specific Value from a List (Topic: Lists)**

**Problem:**
Write a program to remove all occurrences of a specific value from a list.

```python
def remove_value(lst, value):
    return [x for x in lst if x != value]

# Test
print(remove_value([1, 2, 3, 4, 2], 2))  # [1, 3, 4]
```

**Explanation:**
- Use list comprehension to filter out the specified value from the list.

---

### **143. Create a Function to Check for Palindrome Using `if-else` (Topic: if-elif-else)**

**Problem:**
Write a program to check if a string is a palindrome.

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test
print(is_palindrome("Racecar"))  # True
print(is_palindrome("hello"))   # False
```

**Explanation:**
- Normalize the string by converting to lowercase and removing spaces, then check if it reads the same forwards and backwards.

---

### **144. Implement a Function to Return All Subsets of a Set (Topic: Sets)**

**Problem:**
Write a program to return all subsets of a set.

```python
def subsets(s):
    result = [[]]
    for elem in s:
        result += [curr + [elem] for curr in result]
    return result

# Test
print(subsets({1, 2, 3}))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

**Explanation:**
- Generate all subsets using a combination of current subsets and adding new elements.

---

### **145. Create a Function to Reverse a List Using `reversed()` (Topic: Lists)**

**Problem:**
Write a program to reverse a list using the `reversed()` function.

```python
def reverse_list(lst):
    return list(reversed(lst))

# Test
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

**Explanation:**
- Use `reversed()` to get an iterator that yields the elements in reverse order, then convert it back to a list.

---

### **146. Implement a Function to Find the Median of a List (Topic: Lists)**

**Problem:**
Write a program to find the median of a list of numbers.

```python
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Test
print(find_median([3, 1, 2, 5, 4]))  # 3
print(find_median([1, 2, 3, 4]))     # 2.5
```

**Explanation:**
- Sort the list and find the middle element(s) to compute the median.

---

### **147. Create a Function to Check for Armstrong Numbers (Topic: Functions)**

**Problem:**
Write a program to check if a number is an Armstrong number (where the sum of its own digits each raised to the power of the number of digits equals the number itself).

```python
def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

# Test
print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
```

**Explanation:**
- Calculate the sum of each digit raised to the power of the number of digits and compare it to the original number.

---

### **148. Implement a Function to Return the Most Frequent Element in a List (Topic: Lists)**

**Problem:**
Write a program to find the most frequent element in a list.

```python
from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

# Test
print(most_frequent([1, 2, 2, 3, 3, 3]))  # 3
```

**Explanation:**
- Use `collections.Counter` to count occurrences and retrieve the most common element.

---

### **149. Create a Function to Flatten a Nested List (Topic: Lists)**

**Problem:**
Write a program to flatten a nested list.

```python
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

# Test
print(flatten([1, [2, [3, 4]], 5]))  # [1, 2, 3, 4, 5]
```

**Explanation:**
- Recursively extend the result list if the item is a list.

---

### **150. Use `try-except` to Handle Division by Zero Error (Topic: Exception Handling)**

**Problem:**
Write a program that handles division by zero using `try-except`.

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Cannot divide by zero.
```

**Explanation:**
- Use `try-except` to handle potential `ZeroDivisionError` and return an appropriate message.

---

Feel free to ask if you need more examples or specific topics!