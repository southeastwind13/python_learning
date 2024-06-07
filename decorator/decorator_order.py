'''
decorator

syntax
@decorator

parameters
decorator: decorator function

returns
decorator function

Remark:
If having multiple decorators, it will run from bottom to top.
'''

# Test decorator oder from bottom to top
def make_star(func):

    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrapper

def make_percentage(func):

    def wrapper(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)
    return wrapper

@make_percentage
@make_star
def greeting(name:str):
    print(f"Hello {name}")

b = greeting("Pong")
print(b)
