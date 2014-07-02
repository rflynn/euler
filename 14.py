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

def collatz_memoize(hi):
    d = {}
    for n in xrange(hi, 1, -1):
        while n > 1 and n not in d:
            c = 3*n+1 if n & 1 else n >> 1 # memoize
            d[n] = c
            n = c
    return d

# TODO: if we reversed the paths we could find this much more cheaply
def path_len(collatz, lx, n):
    l = 1
    orign = n
    while n > 1 and n not in lx:
        n = collatz[n]
        l += 1
    lx[orign] = l # memoize path_len in lx
    l += lx[n]
    return l

x = 1000000
c = collatz_memoize(x)
lx = {}
m, l = 1, path_len(c, lx, 1)
for m2 in xrange(2, x + 1):
    l2 = path_len(c, lx, m2)
    if l2 > l:
        print "%s -> %s" % (m2, l2)
        m = m2
        l = l2

print m
print len(c)
print max(c.keys())

#from pprint import pprint
#pprint(a)

"""
print "digraph {"
for k,v in a.items():
    print "%s -> %s" % (k, v)
print "}"
"""

