# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def antisymmetric(matrix):
    rows = len(matrix)
    if (rows == 0):
        return True
    
    cols = len(matrix[0])
    if (rows != cols):
        return False

    #0,0 with 0,0 : 0,1 with 1,0 : 0,2 with 2,0
    #1,0 with 0,1 : 1,1 with 1,1 : 1,2 with 2,1
    #2,0 with 0,2 : 2,1 with 1,2 : 2,2 with 2,2

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return True

# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
