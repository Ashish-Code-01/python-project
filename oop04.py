# Notes on Getter and Setter in Python
#
# Getter and Setter are methods used to get (retrieve) and set (update) the value of an object's attribute.
# They help control access to private variables and add validation or logic when getting or setting values.
#
# Example:
#
# class Person:
#     def __init__(self, name):
#         self._name = name  # _name is a 'protected' variable
#
#     # Getter method
#     def get_name(self):
#         return self._name
#
#     # Setter method
#     def set_name(self, value):
#         self._name = value
#
# p = Person('Ashish')
# print(p.get_name())  # Output: Ashish
# p.set_name('Rahul')
# print(p.get_name())  # Output: Rahul

# In Python, you can also use @property for a more elegant way:
#
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

p = Person('Ashish')
print(p.name)  # Output: Ashish
p.name = 'Rahul'
print(p.name)  # Output: Rahul
