'''
iterators

    An iterator is an object that can be iterated upon, meaning that you can
    iterate over it. An object is called iterable if we can get an iterator
    using the iter() function.

syntax
    iterator = iter(object)         

parameters
    object: The object to get the iterator from.

returns
    The iterator.
'''

# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0

print(next(iterator)) # StopIteration