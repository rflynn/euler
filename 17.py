
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ref: https://projecteuler.net/problem=17
'''

from nose.tools import eq_


Nglish = [
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
    ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'],
    ['', '', 'twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-', 'ninety-'],
]


def nglish(n):
    if n == 1000:
        return 'one thousand'
    orign = n
    digits = list(reversed([int(c) for c in str(n)]))
    s = []
    if n > 99:
        s.append(Nglish[0][digits[2]])
        s.append('hundred')
        n = n % 100
        if n != 0:
            s.append('and')
    if n < 10:
        if orign < 100 or (orign > 99 and n != 0):
            s.append(Nglish[0][n])
    elif n < 20:
        s.append(Nglish[1][n - 10])
    elif n >= 20:
        s.append(Nglish[2][digits[1]])
        if digits[0]:
            s.append(Nglish[0][digits[0]])
    return ' '.join(s).replace('- ', '-').rstrip('-')


def letter_count(nstr):
    return len(nstr.replace(' ', '').replace('-', ''))


def test_example():
    eq_(nglish(342), 'three hundred and forty-two')
    eq_(nglish(115), 'one hundred and fifteen')


def test_mine():
    eq_(nglish(0), 'zero')
    eq_(nglish(1000), 'one thousand')
    eq_(nglish(10), 'ten')
    eq_(nglish(11), 'eleven')
    eq_(nglish(20), 'twenty')
    eq_(nglish(120), 'one hundred and twenty')


if __name__ == '__main__':
    print(sum(letter_count(nglish(n)) for n in range(1, 1001)))
    for n in range(1, 1001):
        print(n, nglish(n), letter_count(nglish(n)))
    

