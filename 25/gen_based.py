"""
I actually got to use the fibonacci_generator from PE2 here.
No modification required!
"""


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


fg = fibonacci_generator()


idx, fibval = 0, 0
while len(str(fibval)) < 1000:
    fibval = next(fg)
    idx = idx + 1


print(idx)
