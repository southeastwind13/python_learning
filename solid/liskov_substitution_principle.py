'''
Concept: 
Objects of a superclass should be replaceable with objects of subclasses without 
affecting the correctness of the program.

Real world situation: 
We are driving a vehicle, and we can change the type of it (car, plane, etc).


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