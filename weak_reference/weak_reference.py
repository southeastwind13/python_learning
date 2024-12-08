'''
Gabage Collection 
In Python, garbage collection is a process that reclaims memory occupied by 
objects. 

Python running keeps a record of the number of references to each object. If 
there is at least one reference (Strong) to an object, then that object can't be 
garbage collected.


Weak refrence
In Python, weak references are objects that refer to objects outside of their 

'''

import ctypes

class Data:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f'Data({self.value})'
    

print("Create data item")
data = Data(1)

print("Obtains id of the list object")
id_data = id(data) # Use to check reference count

other_data1 = data
other_data2 = data

data = None

print("Chekc reference count of the data object")
ref_count = ctypes.c_long.from_address(id_data).value
print(ref_count)