'''
We can use combine filter with lambda function.

syntax
filter(function, iterable)

parameters
function: The function to apply to each element of the iterable.
iterable: The iterable to filter.

returns
The filtered iterable.
'''

# program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list) # [4, 6, 8, 12]