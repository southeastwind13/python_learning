'''
*args and **kwargs

*args is used to pass a non-keyworded, variable-length argument list
**kwargs is used to pass a keyworded, variable-length argument list
'''


# Example of *args
def add(*num):

    sum = 0

    for n in num:
        sum += n
    return sum


result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)   # 55


# Example of **kwargs
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)