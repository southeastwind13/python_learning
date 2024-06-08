'''
Generators

In Python, a generator is a function that returns an iterator that produces a 
sequence of values when iterated over.

There are several reasons that make generators a powerful implementation.
1. Easy to Implement
    Generators can be implemented in a clear and concise way as compared to
    their iterator class counterpart.
2. Memory Efficient
    Generator implementation of such sequences is memory friendly and is 
    preferred since it only produces one item at a time.
3. Represent Infinite Stream
    Generators are excellent mediums to represent an infinite stream of data.
4. Pipelining Generators
    Multiple generators can be used to pipeline a series of operations. 
    This is best illustrated using an example.


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


# Pipelining ganerators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
