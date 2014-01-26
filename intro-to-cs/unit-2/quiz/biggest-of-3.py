# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
    if (a > b):
        if (a > c):
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c
            





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