""" 
This works but is fairly slow: 

    joe@nor:~/pe_solutions/3$ time python3 genprimes.py 
    <stdout redacted>

    real    0m46.972s
    user    0m44.964s
    sys 0m2.000s

I really ought to investigate less naive ways of determining primality.
"""

cache = {2,3,5}
UPPERBOUND = 10002


def is_prime(n):
    if n in cache:
        return True

    for i in cache:
        if n % i == 0:
            return False

    for i in [x for x in range(2, int(n/2)) if x not in cache]:
        if n % i == 0:
            return False
    cache.add(n)
    return True


def find_next_prime(n):
    if n == 2:
        return 3
    elif n == 3:
        return 5
    n = n + 1
    while True:
        if is_prime(n):
            return n
        else:
            n = n + 1


def primes():
    for i in cache:
        yield i

    n = 5
    while True:
        hot_new_prime = find_next_prime(n)
        yield hot_new_prime
        n = hot_new_prime


p = primes()
print([next(p) for _ in range(1, UPPERBOUND)][-1])
