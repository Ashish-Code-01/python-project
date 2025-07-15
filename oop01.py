# Object-Oriented Programming Example
# ==============================

# This example demonstrates basic OOP concepts using a Person class


class Person:
    """
    A class to represent a Person with their basic information.

    Class Attributes:
        name (str): The person's name, default empty string
        age (int): The person's age, default 0
        networth (float): The person's net worth, default 0
        occupation (str): The person's occupation, default empty string

    Methods:
        info(): Prints formatted information about the person
    """

    # Class attributes with default values
    name = ""
    age = 0
    networth = 0
    occupation = ""

    def info(self):
        """
        Print formatted information about the person.

        Displays the person's name, age, net worth, and occupation in a readable format.
        """
        print(
            f"Name: {self.name}, Age: {self.age}, Net Worth: {self.networth}, Occupation: {self.occupation}"
        )


# Creating instances of the Person class
# ====================================

# First instance - Person 'a'
a = Person()  # Create a new Person object
a.age = 20  # Set age
a.name = "Ashish"  # Set name
a.occupation = "Full stack Developer"  # Set occupation
a.networth = 2000000000  # Set net worth

# Display information for person 'a'
a.info()

# Second instance - Person 'b'
b = Person()  # Create another Person object
b.age = 18  # Set age
b.name = "shweta"  # Set name
b.occupation = "Data Scientist"  # Set occupation
b.networth = 200  # Set net worth

# Display information for person 'b'
b.info()

"""
Code Explanation:
----------------
1. We define a Person class with class attributes (name, age, networth, occupation)
2. The class has an info() method that prints formatted information about a person
3. We create two instances of the Person class: 'a' and 'b'
4. For each instance, we set different values for their attributes
5. We call the info() method on each instance to display their information

Output Example:
--------------
Name: Ashish, Age: 20, Net Worth: 2000000000, Occupation: Full stack Developer
Name: shweta, Age: 18, Net Worth: 200, Occupation: Data Scientist
"""
