'''
wrap 

This is a decorator that wraps a function and adds functionality to it. It will
help to keep an information of the original function such as name, docstring,
arguments list, etc.
'''


from functools import wraps

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

# We losing name and docstring from f because it is decorated by with_logging
print(f.__name__) # with_logging
print(f.__doc__) #  None


'''
functools.wraps. This takes a function used in a decorator and adds the 
functionality of copying over the function name, docstring, arguments list, 
etc. And since wraps is itself a decorator, the following code does the 
correct thing:
'''

def logged2(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged2
def f2(x):
   """does some math"""
   return x + x * x

print(f2.__name__) # with_logging
print(f2.__doc__) #  None