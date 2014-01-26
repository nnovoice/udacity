# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

#x = 3.14159
#x = 27.63
#x = 0.56
#x = 1.1
#x = 1.5
#x = 1024.4
#x = 22.7
#x = 1.0
#x = 2.9
#x = 99009900990.5
#x = 99009900990.4
x = 9.89327

#ENTER CODE BELOW HERE
y = x + 1
str_x = str(x)
str_y = str(y)

num_x =  str_x[0:str_x.find('.')]
frac_x = str_x[str_x.find('.') + 1:]
sig_digit = frac_x[0]
#print sig_digit

num_y = str_y[0:str_y.find('.')]

#extract all digits except the last
ceiling = num_x[:-1]

#get the last digit of x and last digit of y and put it in last_digits_xy
last_digits_xy = num_x[-1] + num_y[-1]
#print last_digits_xy

digits = "0123456789"
sig_digit_pos = digits.find(sig_digit)

last_digit_end_pos = sig_digit_pos/5 - 2;
#print last_digit_end_pos

ceiling = ceiling + last_digits_xy[last_digit_end_pos]
print ceiling
#has error for x = 9.89327















