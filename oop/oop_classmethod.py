'''
We can use class methods to 
1. Hold data between instances.
2. Alternate constructors for new instances.
'''

class Dog():
    number_of_dogs = 0
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

        # We can use class methods to hold 
        Dog.number_of_dogs += 1
    def calling(self):
        print(f"{self.name} is calling")

    # We can use class methods to be alternative constructors
    @classmethod
    def create_dog(cls, dog_str:str):
        name, age = dog_str.split('-')
        return cls(name, age)


gaga = Dog("gaga", 3)
puipui = Dog("puipui", 5)
puipui.calling() # puipui is calling
print(Dog.number_of_dogs)


gege = Dog.create_dog("brave-5")
print(gege.age)