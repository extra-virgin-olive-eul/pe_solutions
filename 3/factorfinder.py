from math import sqrt


BIGNUM = 600851475143


def is_prime(n):
    for i in [x for x in range(2, int(n/2))]:
        if n % i == 0:
            return False
    return True


def find_factors(n):
    return [i for i in range(1, int(sqrt(n))) if n % i == 0]


print(max(filter(lambda x: is_prime(x), find_factors(BIGNUM))))
