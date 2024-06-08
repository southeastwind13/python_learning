'''
Polymorphism
- Polymorphism is the ability of an object to take on many forms.
- Polymorphism is achieved through method overriding.
- Polymorphism is achieved through method overloading.


Polymorphism describes the concept that you can access objects of different 
types through the same interface. Each type can provide its own independent 
implementation of this interface.
'''

class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()     # renders Square

# create an object of Circle
c1 = Circle()
c1.render()     # renders Circle