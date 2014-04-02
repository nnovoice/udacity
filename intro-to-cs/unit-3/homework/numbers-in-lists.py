# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal 
# to the proceeding number, the proceeding number should be inserted 
# into a sublist. Continue adding to the sublist until the proceeding number 
# is greater than the first number before the sublist. 
# Then add this bigger number to the normal list.

#Hint - "int()" turns a string's element into a number
def numbers_in_lists(string):
    # YOUR CODE
    # outer list and its first number
    # inner list and its first number
    # if current number is greater than outer list's first #, then append to outer list
    # else if current number is > inner list's first number, create a new list, append to the outer list, update the inner list first number
    # else append to the inner list
    outer_list = []
    outer_list_max_digit = 0
    inner_list = []
    inner_list_max_digit = 0

    if (len(string) == 0):
        return []
    
    for c in string:
        digit = int(c)
        if (digit > outer_list_max_digit):
            outer_list.append(digit)
            outer_list_max_digit = digit
        else:
            if (digit > inner_list_max_digit):
                if (len(inner_list) > 0):
                    outer_list.append(inner_list)
                inner_list = [digit]
                inner_list_max_digit = digit
            else:
                inner_list.append(digit)
                
    if (len(inner_list) > 0):
        outer_list.append(inner_list)

    print 'outer list=', outer_list
    return outer_list
        

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), 'got=', numbers_in_lists(string), 'expected=', result, numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
