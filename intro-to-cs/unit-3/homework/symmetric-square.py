# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(matrix):
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
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False

print symmetric([])
