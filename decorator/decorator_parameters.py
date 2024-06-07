'''
decorator with parameters

The decorator with arguments should return a function that will take a 
function and return another function.

def decorator_factory(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            funny_stuff()
            something_with_argument(argument)
            result = function(*args, **kwargs)
            more_funny_stuff()
            return result
        return wrapper
    return decorator


Summary:
1. The decorator function take a arguments.
2. The decorator function return a function that will take a function and 
return another function.
'''

import time
from functools import wraps


def retry(retries=3, delay=3):
    
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs): 
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    print(f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        print(f'Error: {repr(e)} -> Retrying...')
                        time.sleep(delay)  # Add a delay before running the next iteration
        return wrapper
    return decorator
    
@retry(retries=3, delay=1)
def connect() -> None:
    time.sleep(1)
    raise Exception('Could not connect to internet...')

connect()