from copy import deepcopy
from itertools import combinations
from math import sqrt

"""
Took a weird kind of informed brute search here.

I knew the answer had to involve four-digit primes, so I generated a
list of those in the first step of `__main__`.

I also knew the answer had to consist of three numbers that were permutations
of one another (anagrams, lexically speaking). I took my list of four digit
primes, and calculated a crude hash value for each.

I then used that list of keys to build an inverted index so I could get all the
possible permutations.

After that, it was a matter of running through each `len(permutations) choose 3`
combination and seeing if the difference between the first and the second term is
equal to the difference between the second and the third term (`seq_is_legit`).

(I'm certain there's a clearer way to explain this all. However, this is all I can
really muster for now :))
"""

def is_prime(n):
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


def seeking_ever_upward(start):
    next_num = start + 1
    while True:
        if is_prime(next_num):
            return next_num
        else:
            next_num = next_num + 1 
        

def primes_under_10k():
    primes_under_10k = [2,3,5,7,11]
    while primes_under_10k[-1] < 10000:
        primes_under_10k.append(seeking_ever_upward(primes_under_10k[-1]))
    return primes_under_10k


def get_int_hash(i):
    seq = [int(e) for e in str(i)]
    seq.sort()
    return ''.join([str(elem) for elem in seq])


def build_primes_hash_table(primes):
    table = dict()
    for p in primes:
        table[p] = get_int_hash(p)
    return table


def build_inverted_index(keys, hash_table):
    inverted_index = dict()
    for k in keys:
        primes_list = list()
        for i, v in hash_table.items():
            if v == k:
                primes_list.append(i)
        inverted_index[k] = primes_list
    return inverted_index


def seq_is_legit(seq):
    if len(seq) != 3:
        raise Exception("3-item sequences only!")

    shadow_seq = list(deepcopy(seq))
    shadow_seq.sort()

    if shadow_seq[1]-shadow_seq[0] == shadow_seq[2]-shadow_seq[1]:
        return True
    return False


def find_seq_triplet(list_of_perms):
    c = combinations(list_of_perms, 3)
    for combo in c:
        if seq_is_legit(combo):
            return combo
    return False


if __name__ == '__main__':
    four_digit_primes = list(filter(lambda x: x > 999 and x < 10000, primes_under_10k()))
    primes_hash_table = build_primes_hash_table(four_digit_primes)

    keys = list()
    for k, v in primes_hash_table.items():
        keys.append(v)

    ii = build_inverted_index(keys, primes_hash_table)

    for k, v in ii.items():
        found_seq_triplet = find_seq_triplet(v)
        if found_seq_triplet:
            found_seq_triplet = list(found_seq_triplet)
            found_seq_triplet.sort()
            print(found_seq_triplet)
