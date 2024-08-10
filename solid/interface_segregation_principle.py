'''
Concept: 
Clients should not be forced to depend on interfaces they do not use.

Real-World Analogy: 
It is like having a universal remote control with so many buttons, most of which 
you never use. Instead, you would prefer a simpler remote with only the buttons 
you need.

In Practice: Instead of creating a large interface with many methods, 
create smaller, more specific interfaces for each type of functionality

Example: 
To follow the Interface Segregation Principle, we should create specific 
interfaces for each type of functionality:


Separate interfaces so wecan use it with different implementations
'''

from abc import ABC, abstractmethod

class TwoDimensionInterface(ABC):
    @abstractmethod
    def get_area(self):
        pass

class ThreeDimensionInterface(ABC):
    @abstractmethod
    def get_volume(self):
        pass

# Square doesn't need to implement get_volume method
class Rectangle(TwoDimensionInterface):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class cuboid(TwoDimensionInterface, ThreeDimensionInterface):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_area(self):
        return self.length * self.width
    
    def get_volume(self):
        return self.length * self.width * self.height