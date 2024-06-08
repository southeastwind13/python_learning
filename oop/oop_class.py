class Dog():

    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def calling(self):
        print(f"{self.name} is calling")

gaga = Dog("gaga", 3)
puipui = Dog("puipui", 5)
puipui.calling() # puipui is calling