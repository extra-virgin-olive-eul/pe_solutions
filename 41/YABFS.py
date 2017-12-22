# -*- coding: utf-8 -*-

from itertools import permutations
from math import sqrt

"""
YABFS: Yet Another Brute Force Solution(TM)


joe@nor:~/pe_solutions/41$ (master) time python3 YABFS.py 
<stdout redacted>

real    0m58.520s
user    0m57.888s
sys     0m0.628s


This is just __barely__ a solution. It technically computes
the correct answer under a minute, but only because I'd done
a bunch of prior testing to rule of the possibility of a 9-digit
pandigital prime.

(This program *cannot* search the 9-digit space efficiently!)

We run a primality check on the integer representation of each 
permutation of the string '87654321'.

If we find none, try 7 and so on and so forth. 
If a prime is found, break and print.
"""

def is_prime(n):
    """
    I learned about this mini-optimization from Wikipedia:
    (https://en.wikipedia.org/wiki/Primality_test#Simple_methods)

    "... Therefore, we can further eliminate testing divisors greater than √n. 
    We can also eliminate all the even numbers greater than 2, since if an 
    even number can divide n, so can 2."
    """
    def is_2_or_odd(n):
        if n == 2:
            return True
        if n % 2 != 0:
            return True
        return False

    for i in [j for j in range(2, int(sqrt(n)+1)) if is_2_or_odd(j)]:
        if n % i == 0:
            return False
    return True


def descending_pandigital_seq(digits):
    """
    Give me a number of digits., I'll give you back a 
    descending sequence to 1 as a string.

    >> descending_pandigital_sum(3) 
    '321'

    """
    seq = ''
    n = digits
    while n > 0:
        seq = seq+str(n)
        n = n-1
    return seq


def pandigital_prime_search(digits):
    """
    Search for digits-long pandigital prime.

    We want to find the max prime, so we'll start
    with the highest permutation of the seq.

    Example: 4 digits => '4321'
    """
    p = permutations(descending_pandigital_seq(digits))

    for elem in p:
        num = int(''.join(elem))
        if is_prime(num):
            return num
    
    return -1

if __name__ == '__main__':
    n = 8
    while n > 0:
        result = pandigital_prime_search(n)
        if result != -1:
            print(result)
            break
        n = n-1
