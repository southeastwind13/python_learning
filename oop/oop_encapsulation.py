'''
Encapsulation

Encapsulation is a mechanism of wrapping code and data together
in a single unit so that only the required data is visible to the user.

We use two double underscore for private variable. __{name}
- When user try to update the private variable, it isn't error but the private
variable isn't change.
- We have to use set method to update the private variable
'''

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()

c._maxprice = 1000      # Don't get an error but the private variable isn't change
c.sell()                # 900

c.setMaxPrice(1000)     # Wehave to use set method to change private variable
c.sell()                # 1000