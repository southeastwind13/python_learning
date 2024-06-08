'''
Lambda

A lambda function is a special type of function without the function name. 

For example, 

syntax
lambda arguments : expression
'''

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Pong')