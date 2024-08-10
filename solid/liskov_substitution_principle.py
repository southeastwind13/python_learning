'''
Concept: 
Objects of a superclass should be replaceable with objects of subclasses without 
affecting the correctness of the program.

Real world situation: 
We are driving a vehicle, and we can change the type of it (car, plane, etc).

In Practice: Ensure that subclasses alter expected behavior. For example, if you 
have a class Bird with a method move(), each subclass should implement the 
move() method to reflect its specific type of movement

Example: To follow the Liskov Substitution Principle, we should ensure that 
subclasses override methods to reflect their behavior correctly:
'''

class Vehicle:
    def move(self):
        return "Moving"
    
class Car(Vehicle):
    def move(self):
        return "Car is moving"
    
class Plane(Vehicle):
    def move(self):
        return "Plane is flying"
    
vehicles = [Car(), Plane()]

for vehicle in vehicles:
    print(vehicle.move())