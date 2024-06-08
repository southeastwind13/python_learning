'''
filter

syntax
filter(function, iterable)

parameters
function: The function to apply to each element of the iterable.
iterable: The iterable to filter.

returns
The filtered iterable.
'''

# returns True if the argument passed is even
def check_even(number):
    if number % 2 == 0:
          return True  
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(check_even, numbers))

print(filtered_numbers)