
# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

rabbits_without_death = {}
rabbits_after_death = {}

def gen_fib(n):
    rabbits_without_death[0] = 0
    rabbits_without_death[1] = 1
    rabbits_without_death[2] = 1
    
    month = 3
    fib1 = 1
    fib2 = 1
    temp = 0
    for i in range (3, n+1):
        temp = fib2
        fib2 = fib1
        fib2 = temp + fib2
        fib1 = temp
        rabbits_without_death[i] = fib2
        print str(i), ":", rabbits_without_death[i]
    
    
def update_rabbits_after_death():
    for i in range(0,6):
        rabbits_after_death[i] = rabbits_without_death[i]
    n = len(rabbits_without_death)
    for i in range(6, n):
        rabbits_after_death[i] = rabbits_after_death[i - 1] + rabbits_after_death[i - 2] - rabbits_without_death[i - 5]
    return 
        

def rabbits(n):
    return rabbits_after_death[n]


gen_fib(36)
update_rabbits_after_death()
print rabbits(5)

print rabbits(10)
#>>> 35

s = ""
for i in range(1,12):
    s = s + str(rabbits(i)) + " "
print s
#>>> 1 1 2 3 5 7 11 16 24 35 52

