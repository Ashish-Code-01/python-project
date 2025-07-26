class Car:
    # Class variable: shared by all instances of Car
    # Represents the general type of vehicle
    vehicle_type = "Automobile"

    def __init__(self, make, model):
        # Instance variables: unique to each Car object
        # Each car has its own make and model
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This is a {self.make} {self.model}. It is a {Car.vehicle_type}.")

# Create two instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing instance variables (unique to each object)
print(f"Car 1: {car1.make} {car1.model}") # Output: Car 1: Toyota Camry
print(f"Car 2: {car2.make} {car2.model}") # Output: Car 2: Honda Civic

# Accessing class variable (shared by all objects)
print(f"Vehicle type for car1: {car1.vehicle_type}") # Output: Vehicle type for car1: Automobile
print(f"Vehicle type for car2: {car2.vehicle_type}") # Output: Vehicle type for car2: Automobile
print(f"Vehicle type from class: {Car.vehicle_type}") # Output: Vehicle type from class: Automobile

# Modifying the class variable
Car.vehicle_type = "Passenger Car"

# Observe the change reflected in all instances and the class itself
print(f"\nAfter changing vehicle_type:")
print(f"Vehicle type for car1: {car1.vehicle_type}") # Output: Vehicle type for car1: Passenger Car
print(f"Vehicle type for car2: {car2.vehicle_type}") # Output: Vehicle type for car2: Passenger Car
print(f"Vehicle type from class: {Car.vehicle_type}") # Output: Vehicle type from class: Passenger Car

# Modifying an instance variable (does not affect other instances)
car1.make = "Nissan"
print(f"\nAfter changing car1's make:")
print(f"Car 1: {car1.make} {car1.model}") # Output: Car 1: Nissan Camry
print(f"Car 2: {car2.make} {car2.model}") # Output: Car 2: Honda Civic (unchanged)