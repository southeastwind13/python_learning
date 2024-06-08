'''
__repr__

- The __repr__ provides the official string representation of an object, aimed 
at the programmer (Use for debugging or logging purposes). -> It should show how 
we create the instance

__str__

- The __str__  provides the informal string representation of an object, aimed 
at the user. 

When we call print(object) it will call __str__ method and if it doesn't have 
then it will call __repr__.
'''

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'Employee({self.id}, {self.name}, {self.salary})'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.salary}'
    
emp1 = Employee(101, 'John', 10000)
print(emp1.__str__())
print(emp1.__repr__())
print(emp1)