
'''
ref: https://projecteuler.net/problem=19
'''

from datetime import datetime
from itertools import product

print(sum(datetime(year=y, month=m, day=1).date().isoweekday() == 7
            for m, y in product(range(1, 13), range(1901, 2001))))

