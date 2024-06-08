'''
Python closure is a nested function that allows us to access variables of 
the outer function even after the outer function is closed.


When to use closures?
Closures can be used to avoid global values and provide data hiding, and 
can be an elegant solution for simple cases with one or few methods.

'''

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

print(times3(9)) # 27
print(times3(5)) # 15