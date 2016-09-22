
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest number that is evenly divisible by all of the
# numbers from 1 to 20?

import math

# Is 2520 just 1..10 multipled??
print("1*2*3*4*5*6*7*8*9*10=" + str(1*2*3*4*5*6*7*8*9*10))
print("2*3*5*6*7=" + str(2*3*5*6*7))
print("2*3*5*7=" + str(2*3*5*7))

assert 2 == 2520/(2*3*5*6*7)

Step = 5*7*8*9
print("2520/%u = %f" % (Step, 2520.0 / Step))
#print(2520/(1*2*3*4*5*6*7*8*9*10))

# Find all prime factors in [1,20]
# 2 4 6 8 10 12 14 16 18 20
# 3 9 15
# 5
# 7
# 11
# 13
# 17
# 19

#Step = 2*3*5*7*12*#*13*17*19
#Step = 20*15*7*11*13*17*19
#Step = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
Step = 10*11*12*13*14*15*16*17*18*19
print("Step=" + str(Step))

# does denom divide evenly into num?
def even_div(num, denom):
    foo = float(num) / float(denom)
    return foo == math.floor(foo)

# test deven_div
assert     even_div(1, 1)
assert     even_div(2, 1)
assert not even_div(1, 2)
assert     even_div(4, 2)
assert not even_div(5, 2)
assert     even_div(100, 10)
assert not even_div(100000000000, 10000000001)

Div = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Div.reverse()
print(Div)

# is num evenly divisible by all our factors?
def div_1_20(num):
    for div in Div:
        if not even_div(num, div):
            return False
    return True

# obviously all our factors multiplied together will work...
Known = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
print("Known=" + str(Known))

assert div_1_20(Known)

Step = 20*19*18*17
n = Step
while n < Known:
    if div_1_20(n):
        break
    n = n + Step

print("n=%u Step=%u %u/%u=%f" % (n, Step, n, Step, float(n) / Step))

# n=232792560 Step=116280 232792560/116280=2002.000000

