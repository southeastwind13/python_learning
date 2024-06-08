'''
Generators

In Python, a generator is a function that returns an iterator that produces a 
sequence of values when iterated over.

syntax
    def function_name():
        # Yield statement
        yield value         

    function_name()     
    next(function_name())  


Generators are useful when we want to produce a large sequence of values, 
but we don't want to store all of them in memory at once.                             
    
'''

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

data = my_generator(3)
print(next(data))
print(next(data))
print(next(data))
print(next(data))