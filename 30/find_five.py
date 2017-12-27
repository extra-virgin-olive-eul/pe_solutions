"""
I guessed an upperbound of a million and happened to get lucky.

joe@nor:~/pe_solutions/30$ (master) time python3 find_five.py 
<stdout redacted>
<stdout redacted>

real    0m3.998s
user    0m3.988s
sys     0m0.004s

"""

def composed_of_powers(n, power=5):
    return n == sum([int(i)**power for i in str(n)])


if __name__ == '__main__':
    UPPERBOUND = 1000000

    found = list()

    n = UPPERBOUND
    while n > 1:
        if composed_of_powers(n):
            found.append(n)
        n -= 1

    print(found)
    print(sum(found))
