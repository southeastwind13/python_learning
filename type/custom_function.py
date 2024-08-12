class Employee:
    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    '''
    Custome add function to add salaries of two employees
    '''
    def __add__(self, other):
        return self.salary + other.salary
    
emp1 = Employee("John Doe", 30, 50000.0)
emp2 = Employee("Jane Smith", 28, 60000.0)

total_salary = emp1 + emp2
print(f"Total salary of John Doe and Jane Smith: {total_salary}")