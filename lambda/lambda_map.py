'''
We can use map with lambda function.

syntax
map(function, iterable)

parameters
function: The function to apply to each element of the iterable.
iterable: The iterable to map.

returns
The mapped iterable.
'''

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)     # Output: [2, 10, 8, 12, 16, 22, 6, 24]