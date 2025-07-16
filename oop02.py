# This is the class person
class Person:
    # The __init__ function is called a constructor in Python.
    # It is automatically called when a new object of the class is created.
    # Its main job is to initialize (set up) the object's attributes with values provided as arguments.
    # Syntax: def __init__(self, ...):
    # 'self' refers to the current object being created.
    # Example usage: a = Person("Ashish", "Founder", "50M$", 19)
    def __init__(self, name, occupation, networth, age):
        self.name = name
        self.occupation = occupation
        self.netWorth = networth
        self.age = age

        # This is the functions of the class Person / We can make infine fncttions in any class

    def intro(self):
        print(
            f"Hii, My name is {self.name}, He is {self.occupation} and his networth is {self.netWorth}, he is {self.age} year old"
        )


# Notes on __init__ function:
"""
- __init__ is a special method in Python classes, known as the constructor.
- It is used to initialize the attributes of a class when an object is created.
- The first parameter is always 'self', which refers to the instance being created.
- You can pass any number of arguments to __init__, which are used to set up the object's state.
- Example:
    a = Person("Ashish", "Founder", "50M$", 19)
    This calls __init__ and sets the attributes for the object 'a'.
- Without __init__, you would have to set each attribute manually after creating the object.
"""

# create a object of class Person
a = Person("Ashish", "Founder", "50M$", 19)
# Run the class function, Like this
a.intro()
