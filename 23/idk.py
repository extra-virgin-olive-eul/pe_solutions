"""
A slow solution.

joe@nor:~/pe_solutions/23$ (master) time python3 idk.py
<stdout redacted>

real    0m54.164s
user    0m53.312s
sys     0m0.808s

1.) Find all the abundant nums (under 28123) in `abundant_nums`
2.) Calculate all possible abundant sums in `abundant_sums`
3.) Collect all N in 1-28123 *not* in ab_sums
4.) Sums all ints found in step 3

"""
def factors(n):
    factors = list()
    for i in range(1, int((n/2.0)+1)):
        if n % i == 0:
            factors.append(i)
    return factors


def is_abundant(n):
    return sum(factors(n)) > n


def abundant_nums(upper_bound=28123):
    r = list(range(12, upper_bound))
    return [n for n in r if is_abundant(n) == True]


def abundant_sums(L):
    combinations = list()
    for idx, item in enumerate(L):
        for element in L[idx+1:]:                                                  
            combinations.append(item+item)
            combinations.append(item+element)
    c = list(set(combinations))
    c.sort()
    return c


if __name__ == '__main__':
    ab_nums = abundant_nums()
    ab_sums = abundant_sums(ab_nums)

    pariahs = list()

    n = 28123
    while n > 0:
        if n not in ab_sums:
            pariahs.append(n)
        n = n-1

    print(sum(pariahs))
