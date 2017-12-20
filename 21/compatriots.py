"""
Another slow-ish one where I wasn't really seeing the trick of it.

joe@nor:~/pe_solutions/21$ (master) time python3 compatriots.py 
<stdout redacted>

real    0m22.787s
user    0m22.572s
sys     0m0.212s
"""


def factors(n):
    factors = list()
    for i in range(1, int((n/2.0)+1)):
        if n % i == 0:
            factors.append(i)
    return factors


def build_factors_table(start=0, end=30000):
    table = {}
    for i in range(start, end+1):
        table[i] = factors(i)
    return table


def has_amicable_compatriot(n, factors_table):
    factors_sum = sum(factors_table[n])

    if sum(factors_table[factors_sum]) == n and (n != factors_sum):
        return [n, factors_sum]
    else:
        return False


if __name__ == '__main__':
    factors_table = build_factors_table()

    amicable_nums = set()

    for i in range(1, 10001):
        compatriots = has_amicable_compatriot(i, factors_table)
        if compatriots:
            [amicable_nums.add(n) for n in compatriots]

    print(sum(list(amicable_nums)))
