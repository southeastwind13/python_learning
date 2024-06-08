'''
property decorator

Use to define attribute of class as a method.
- We can call this method as an attribute.
- We can modify value before return it.

Remark:
- Inside the property should use private parameter _{name} because it will not
create a finite loop when call this attribute.
- If we don't use @property decorator, we have to call attribute as a function 
and if can effect code in the downstream.
'''

class Dog():
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    # We get attribute as method

    @property
    def owner(self):
        return f"my owner is {self._owner}"
    
    @owner.setter
    def owner(self, value):
        self._owner = f"{value}@nomail.com"
    

gaga = Dog("gaga", 3)
gaga.owner = "testowner"
print(gaga.owner)