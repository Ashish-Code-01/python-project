# Notes on Public, Protected, and Private Variables in Python
#
# 1. Public Variable:
#    - Can be accessed from anywhere (inside or outside the class).
#    - No special symbol needed.
#    - Example:
#      class Car:
#          def __init__(self):
#              self.color = 'red'  # public
#      c = Car()
#      print(c.color)  # Output: red
#
# 2. Protected Variable:
#    - Should not be accessed outside the class (just a convention, not enforced).
#    - Use a single underscore _ before the variable name.
#    - Example:
#      class Car:
#          def __init__(self):
#              self._mileage = 20  # protected
#      c = Car()
#      print(c._mileage)  # Output: 20 (still accessible, but not recommended)
#
# 3. Private Variable:
#    - Cannot be accessed directly outside the class.
#    - Use double underscore __ before the variable name.
#    - Example:
#      class Car:
#          def __init__(self):
#              self.__engine = 'V8'  # private
#      c = Car()
#      print(c.__engine)  # Error! Not accessible
#      # But can be accessed using: c._Car__engine
#      print(c._Car__engine)  # Output: V8
#
# Summary:
# - Public: self.var
# - Protected: self._var
# - Private: self.__var
