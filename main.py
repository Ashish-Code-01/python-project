# ==========================================================
# Python Programming Notes
# ==========================================================


# 1. Recursion
# ------------
# Recursion is when a function calls itself to solve a smaller instance of the same problem
def factorial(n):
    """Calculate the factorial of a number using recursion"""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage:
# num = 5
# print(factorial(num))  # Output: 120

# 2. Sets
# -------
# Sets are unordered collections of unique elements
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8, 8, 4}  # Note: duplicate 8 will be removed
s1.update(s2)  # Combines both sets, removing duplicates
# print(s1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 3. Dictionaries
# --------------
# Dictionaries are key-value pairs
# Basic dictionary
person = {"name": "Ashu", "age": 18}
# print(person["name"])  # Accessing value using key

# Dictionary methods
info = {"name": "Ashu", "age": 18, "eligibility": True}
info.update({"age": 20, "eligibility": False})  # Updating multiple values
# print(info)

# 4. For Loop with Else
# --------------------
# The else block executes when the loop completes normally (not through break)
for i in range(1, 5):
    print(i)
    if i == 3:
        break
else:
    print("Loop completed normally")


# 5. Exception Handling
# -------------------
# Try-except blocks handle runtime errors gracefully
def safe_array_access():
    try:
        array = [2, 3, 4, 5, 1, 5, 7]
        index = int(input("Enter the index: "))
        print(array[index])
    except IndexError:
        print("Invalid index - array index out of bounds")
    except ValueError:
        print("Please enter a valid number")


# 6. Shorthand If-Else (Ternary Operator)
# -------------------------------------
a, b = 80, 60
result = "A" if a > b else "=" if a == b else "B"
# print(result)  # Output: "A"

# 7. Enumerate Function
# -------------------
# Enumerate provides counter with iterable
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 8. Global and Local Variables
# ---------------------------
x = 5  # Global variable


def demonstrate_scope():
    global x  # Declare we want to use the global x
    x = 4  # Modifies the global x
    print(f"Value of x inside function: {x}")


# demonstrate_scope()
# print(f"Value of x outside function: {x}")


# 9. File Input/Output
# ------------------
def file_operations_demo():
    # Writing to file
    with open("demo.txt", "w") as f:
        f.write("Hello, World!\n")
        f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

    # Reading from file
    with open("demo.txt", "r") as f:
        content = f.read()
        # print(content)


# 10. Lambda Functions
# -----------------
# Lambda functions are small anonymous functions
square = lambda x: x * x
multiply = lambda x, y: x * y


def apply_function(func, value):
    """Higher order function that applies a function to a value"""
    return func(value)


# Example usage:
# print(square(5))  # Output: 25
# print(multiply(3, 4))  # Output: 12
# print(apply_function(square, 6))  # Output: 36
# 11. Functional Programming: Map, Filter, and Reduce
# --------------------------------------------
from functools import reduce

# MAP: Transforms each element in an iterable
numbers = [1, 2, 3, 4, 5]
# Using map to double each number
doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)  # Output: [2, 4, 6, 8, 10]

# Practical map example: Converting temperatures
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
# print(f"Celsius: {celsius}")
# print(f"Fahrenheit: {fahrenheit}")

# FILTER: Selects elements based on a condition
# Get even numbers using filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4]

# Practical filter example: Finding specific strings
names = ["Alice", "Bob", "Alex", "John", "Anna"]
a_names = list(filter(lambda name: name.startswith("A"), names))
# print(f"Names starting with A: {a_names}")

# REDUCE: Aggregates elements to a single value
# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
# print(f"Product of numbers: {product}")  # Output: 120

# Practical reduce example: Finding the longest string
longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)
# print(f"Longest name: {longest_name}")

# =========================================================
# End of Python Programming Notes
# =========================================================
