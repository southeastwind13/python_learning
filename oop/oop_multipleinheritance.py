'''
Multiple Inheritance

Multiple inheritance is when a class inherits from more than one class.
- If subclass use the method with name exist in the superclass, then subclass
will use method from the superclass on the left first. 

(Method Resolution Order (MRO) in Python)
'''

# Multople Inheritance

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

    def eat(self):
        print("Mammals can eat.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

    def eat(self):
        print("Winged animals can eat.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()
b1.mammal_info()            # Access Mammal superclass method
b1.winged_animal_info()     # Access WingedAnimal superclass method
b1.eat()                    # Access Mammal superclass method because it is 
                            # high priority on the left side of MRO