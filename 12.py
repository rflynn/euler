# ex: set ts=2 et:

# The sequence of triangle numbers is generated by adding the natural
# numbers. So the 7^(th) triangle number would be 1 + 2 + 3 + 4 + 5 +
# 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#    1: 1
#    3: 1,3
#    6: 1,2,3,6
#   10: 1,2,5,10
#   15: 1,3,5,15
#   21: 1,3,7,21
#   28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?

import math

# return list of (non-prime) factors of n
# NOTE: brute-force method, slow.
def factors(n):
  f = [1,n]
  for i in xrange(2, int(math.sqrt(n))+1):
    if n % i == 0:
      f.append(i)
      f.append(int(n/i))
  f.sort()
  return f

# check factors()
assert factors(1) == [1,1]
assert factors(2) == [1,2]
assert factors(3) == [1,3]
assert factors(6) == [1,2,3,6]
assert factors(10) == [1,2,5,10]
assert factors(15) == [1,3,5,15]
assert factors(21) == [1,3,7,21]
assert factors(28) == [1,2,4,7,14,28]
# ensure our sqrt math is right
assert factors(4) == [1,2,2,4]
assert factors(25) == [1,5,5,25]

tri = 0
i = 1
f = []

while len(f) <= 500:
  tri += i
  f = factors(tri)
  i += 1

print "%12u: (%u factors) %s" % (tri, len(f), ",".join(map(str,f)))
