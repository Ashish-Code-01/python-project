# ===============================
# Python Decorators Example Notes
# ===============================
# Decorators are functions that modify the behavior of other functions.
# They are often used for logging, access control, timing, etc.
# Syntax: Use '@decorator_name' above a function definition.

# *args and **kwargs:
# -------------------
# *args allows a function to accept any number of positional arguments as a tuple.
# **kwargs allows a function to accept any number of keyword arguments as a dictionary.
# They are useful when you want your function to handle variable numbers of arguments.


def greed(fx):
    # This is a decorator function
    def mfx(*args, **kwargs):
        print("Hello User!")  # Code before the original function
        fx(*args, **kwargs)  # Call the original function
        print("Byeeee!")  # Code after the original function

    return mfx


# Example 1: Decorating a simple function
@greed
def hello():
    print("Hello World!")


# Example 2: Decorating a function with arguments
@greed
def add(a, b):
    print(f"Sum is {a + b}")


# Function calls
hello()
add(5, 10)
