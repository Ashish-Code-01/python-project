# Notes on @property with Inheritance in Python
#
# The @property decorator can be used in parent classes, and child classes can inherit and use these properties.
# You can also override property methods in child classes if needed.
#
# Example:
#
# class Animal:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
# class Dog(Animal):
#     @property
#     def name(self):
#         return "Dog: " + super().name
#
# a = Animal("Tiger")
# print(a.name)  # Output: Tiger
# d = Dog("Rocky")
# print(d.name)  # Output: Dog: Rocky
#
# This shows how property can be inherited and customized in subclasses.
# Notes on Inheritance in Python
#
# Inheritance is a feature in object-oriented programming that allows a class (child/subclass) to inherit properties and methods from another class (parent/superclass).
# This helps in code reuse and makes it easier to organize and manage code.
#
# Example in this file:
# - The class 'Employee' is the parent class.
# - The class 'Manager' is the child class that inherits from 'Employee'.
# - 'Manager' gets all the attributes and methods of 'Employee', and can also have its own (like 'department').
# - The 'showDetails' method is overridden in 'Manager' to add more information.
#
# Syntax:
# class Parent:
#     ...
# class Child(Parent):
#     ...
#
# Benefits:
# - Code reuse
# - Easier maintenance
# - Can extend or modify parent class behavior in child class


class Employee:
    def __init__(self, name, salary, id):
        self.name = name
        self.salary = salary
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}, Salary: {self.salary}, ID: {self.id}")


class Manager(Employee):
    def __init__(self, name, salary, id, department):
        super().__init__(name, salary, id)  # Calls Employee's class (constructor) __init__
        self.department = department

    def showDetails(self):
        super().showDetails()
        print(f"Department: {self.department}")


e1 = Employee("Ashish", 50000, 12345)
e1.showDetails()
e2 = Employee("Shweeta", 50000, 12345)
e2.showDetails()

m1 = Manager("Rohit", 80000, 54321, "Sales")
m1.showDetails()
