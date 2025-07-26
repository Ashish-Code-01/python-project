class Calculator:
    # Class variable
    company = "Calculator Inc."

    def __init__(self, model):
        self.model = model

    # Regular instance method (needs self)
    def display_info(self):
        return f"Calculator Model: {self.model}"

    # Static method - doesn't need access to instance or class
    @staticmethod
    def add(x, y):
        return x + y

    # Static method - another example
    @staticmethod
    def is_positive(number):
        return number > 0


# Using the static methods
print("Static method examples:")
# We can call static methods without creating an instance
print(f"5 + 3 = {Calculator.add(5, 3)}")  # Output: 5 + 3 = 8
print(f"Is 10 positive? {Calculator.is_positive(10)}")  # Output: Is 10 positive? True

# We can also call static methods from an instance
calc = Calculator("Scientific")
print(f"\nCalling static method from instance:")
print(f"2 + 3 = {calc.add(2, 3)}")  # This works too, but not recommended

# Regular instance method needs an instance
print(f"\nInstance method example:")
print(calc.display_info())  # Output: Calculator Model: Scientific
