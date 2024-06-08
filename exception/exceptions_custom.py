'''
Custom exception

Sometimes we may need to create our own custom exceptions that serve our purpose.

'''

class InvalidAgeException(Exception):
    # Raise when the input value is less than 18
    pass

number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")