'''
__slots__ 

Definatio:
In Python, __slots__ is a special attribute in classes. 
It is a list of strings that define the set of attributes that a class 
can have.

Benefits:
1. It reduces memory usage. (By default when python crate an new instance, 
python create __dict__ for it.)
- Dictionary are memory expensive.
- Dictionary are base on hash map.
'''

class Employee:
    __slots__ = ['name', 'age', 'salary']

    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary


emp1 = Employee("John Doe", 30, 50000.0)
emp1.department = "IT" 
# -> AttributeError: 'Employee' object has no attribute 'department'