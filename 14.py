#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n):
    c = [n]
    while n > 1:
        if n & 1 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        c.append(n)
    return c

"""
longest = [1]
for n in range(2, 1000000+1):
    c = collatz(n)
    if len(c) > len(longest):
        longest = c
        print "longest:", longest
"""

def collatz_memoize(hi):
    d = {}
    while hi > 1:
        if hi not in d:
            n = hi
            while n > 1 and n not in d:
                if n & 1 == 0:
                    x = n // 2
                else:
                    x = 3 * n + 1
                d[n] = x
                n = x
        hi -= 1
    return d

def path_len(collatz, lx, n):
    l = 1
    orign = n
    while n > 1:
        if n in lx:
            l += lx[n]
            break
        else:
            n = collatz[n]
            l += 1
    lx[orign] = l # memoize path_len in lx
    return l

x = 1000000
a = collatz_memoize(x)
lx = {}
m, l = 1, path_len(a, lx, 1)
for m2 in xrange(2, x + 1):
    l2 = path_len(a, lx, m2)
    if l2 > l:
        print "%s -> %s" % (m2, l2)
        m = m2
        l = l2
print m

#from pprint import pprint
#pprint(a)

"""
print "digraph {"
for k,v in a.items():
    print "%s -> %s" % (k, v)
print "}"
"""

