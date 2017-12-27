"""

I think I just got lucky on this one.

joe@nor:~/pe_solutions/52$ (master) time python3 wild_goose_chase.py 
<stdout redacted>

real    0m2.768s
user    0m2.760s
sys     0m0.004s


My lazy way of checking for anagrams was to create a string rep for each 
int in question, effectively creating a very simple hash value.

Then I just initiated an upward brute force search. It seems to have
worked out in this case!
"""

def num_hash(n):
    """ 
    Give me an int, and I'll give you a (sorted) string rep of its digits. 

    If num_hash(n) == num_hash(m), then n and m are composed of precisely the same digits.

    Use this value to verify if two nums are numeric anagrams of one another!
    """
    n_hash = [e for e in str(n)]
    n_hash.sort()
    n_hash = ''.join([i for i in n_hash])
    return n_hash


def match(n):
    conds = [num_hash(n) == num_hash(n * 2),
             num_hash(n) == num_hash(n * 3),
             num_hash(n) == num_hash(n * 4),
             num_hash(n) == num_hash(n * 5),
             num_hash(n) == num_hash(n * 6)]

    return all(conds)


if __name__ == '__main__':
    n = 2
    while match(n) == False:
        n = n+1

    print(n)
