'''
Static method

- A static method is a method that is bound to the class and not the object
    of the class. It doesn't require the class instance to be created to use

ne rule-of-thumb: ask yourself "Does it make sense to call this method, 
even if no object has been constructed yet?" If so, it should definitely 
be static.
'''
import datetime

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self, emp):
        print(emp.id, emp.name, emp.salary)

    @staticmethod
    def is_workday(day):
        '''
        We don't expect to create employee object to use this method.
        '''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        
        return True
    
print(Employee.is_workday(datetime.date.today()))