# ex: set ts=2 et:

# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,
#
# a^(2) + b^(2) = c^(2)
#
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# ok, what's the most straight-forward way to search exhaustively for
# Pythagorean triplets? 

import math
import os

assert 0 < 1 < 2

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = math.sqrt(a**2 + b**2)
        assert a < b < c
        if c != math.floor(c):
            continue  # sqrt(a^2+b^2) not natural
        print('%3u^2 + %3u^2 = %3.0f^2 ... %3u + %3u +%4u = %4.0f' % (
            a, b, c, a, b, c, a + b + c))
        if a + b + c == 1000:
            print('%u * %u * %.0f = %.0f' % (a, b, c, a * b * c))
            os._exit(0)

