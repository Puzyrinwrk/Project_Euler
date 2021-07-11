"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome_prod(N):
    palindrome_list = []
    for i in range(101, 1000):
        for j in range(121, 1000, (1 if i%11==0 else 11)):
            n = i*j
            x = str(n)
            if x == x[::-1]:
               if n < N:
                  palindrome_list.append(i*j)
    return max(palindrome_list)