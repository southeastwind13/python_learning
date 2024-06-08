'''
In Python, we use the try...except block to handle exceptions.

try-except-else-finally

try: This block is handled for exceptions
except: This block will be executed if there is an exception
else: This block will be executed if there is no exception
finally: This block will be executed no matter what
'''

try:
    print(10 / 1)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    # This block will run only if there is no exception
    print("Everything went well")
finally:
    print("I am always executed")