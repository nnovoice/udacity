# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    fact = 1
    i = 1
    while (i <= n):
        fact = fact * i
        i = i + 1
    return fact



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
print factorial(15)