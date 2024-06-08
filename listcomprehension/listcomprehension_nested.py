'''
We are able to create nested list using list comprehension.
'''

multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]

print(multiplication)