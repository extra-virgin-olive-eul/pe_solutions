''' I dig takewhile :) '''

from itertools import takewhile


UPPERBOUND = 4000000


def fibonacci_generator():
    a, b = None, None
    while True:
        if a is None and b is None:
            yield 1
            a, b = 0, 1
        else:
            yield a + b
            c = a + b
            a = b; b = c


fib_gen = fibonacci_generator()
applicable_fib_nums = takewhile(lambda n: n < UPPERBOUND, (x for x in fib_gen))
print(sum([i for i in applicable_fib_nums if i % 2== 0]))
