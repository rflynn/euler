
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

assert [1,2,3][1:-1] == [2]

def is_palindrome(n):
        s = str(n)
        while len(s) > 1:
                if s[0] != s[-1]:
                        return False
                s = s[1:-1]
        return True

assert is_palindrome(0)
assert is_palindrome(1)
assert not is_palindrome(10)
assert is_palindrome(11)
assert is_palindrome(999)
assert is_palindrome(9999)

p = []
i = 999
while i >= 100:
        #print str(i) + "..."
        j = i
        while j >= 100:
                n = i * j
                if is_palindrome(n):
                        print("%u x %u = %u" % (i,j,n))
                        p.append(n)
                j = j-1
        i = i-1
print(p)
print(max(p))
