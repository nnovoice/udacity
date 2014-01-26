# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def bigger(a, b):
    if (a >= b):
        return a
    return b

def biggest(a, b, c):
    return bigger(bigger(a,b), c))
            





print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

print biggest(9, 9, 19)
print biggest(0, -1, -2)
print biggest(-1, 0, -1)
print biggest(-1, -2, 2)
print biggest(-1, -1, -1)