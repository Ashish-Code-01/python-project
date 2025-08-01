class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
        
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name.strip(), int(salary.strip()))
        
e1 = Employee("Alice", 50000)
e1.display()
e2 = Employee.from_string("Bob-60000")
e2.display()