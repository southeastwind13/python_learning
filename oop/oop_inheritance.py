'''
Inheritance

Inheritance allows us to define a class that inherits all the methods
and properties from another class.

Super class is the class being inherited from, also called base class.
Sub class is the class that inherits from another class, also called
derived class.

Syntax: class SubClass(SuperClass):     


Summary:
1. Super class is the class being inherited from, also called base class.
2. Sub class is the class that inherits from another class, also called
derived class.
3. Subclass can access all methods and properties of its  Superclass.
4. Subclass can override methods and properties of its Superclass.
5. We can access Superclass methods and properties using super() function.
'''

class Animal:

    name = ""

    def speak(self):
        print("I don't know what to say")

    def bark(self):
        print("Woof!")
    

class Dog(Animal):

    def display(self):
        print(f"My name is {self.name}")

    # Override superclass method
    def bark(self):
        super().speak()     # Access superclass method in subclass
        print("Booow !")


labrador = Dog()            # Create instance of subclass

labrador.name = "Rex"       # Access superclass attribute
labrador.speak()            # Access superclass method
labrador.display()          # Access subclass method
labrador.bark()             # Access override method