class Employee:
    company = "TechCorp"  # class variable
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, float(salary))

# Using the class method
Employee.change_company("NewCorp")  # Changes company for all instances

# Using as alternative constructor
emp = Employee.from_string("John-50000")