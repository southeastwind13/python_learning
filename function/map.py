'''
map

The map() function executes a given function to each element of an iterable 
(such as lists, tuples, etc.).

syntax
map(function, iterable)     

parameters
function: The function to apply to each element of the iterable.
iterable: The iterable to map.

returns
The mapped iterable.
'''

numbers = [1,2,3,4]

# returns the square of a number
def square(number):
  return number * number

# apply square() to each item of the numbers list
squared_numbers = map(square, numbers)

# converting to list for printing
result = list(squared_numbers)
print(result) # Output: [1,4,9,16]