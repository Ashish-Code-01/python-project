# This is the class person
class Person:
    # This is the class Constructor it will take argument. when the class is created , like this  Person("Ashish", "Founder", "50M$", 19)
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


# create a object of class Person
a = Person("Ashish", "Founder", "50M$", 19)
# Run the class function, Like this
a.intro()
