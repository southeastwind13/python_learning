'''
zip

Function to integrate two or more iterable objects into one object.

Syntax
zip(iter1, iter2, iter3, ...)

Parameters
iter1, iter2, iter3, ...: The iterables to zip together.

Returns
The zipped object.
'''

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e', 'f']

print(list(zip(a, b)))  