"""
This one needs serious work.

joe@nor:~/pe_solutions/44$ (master) time python3 pent_up.py 
Checking 3121251 combinations of 2500 pentagon numbers...
<stdout redacted>
<stdout redacted>

real    4m14.708s
user    4m14.344s
sys     0m0.108s

I was technically able to brute force a solution, but there's got
to be a much better way.

My approach was to: 
    * construct a list of the first 2500 pentagon numbers
    * determine the unique (unordered) possible pairings, and
    * see if each pair met the match criteria

At each sum test, new pentagon numbers might be generated if the sum of
p1 + p2 > max(pent_nums).
"""

def pentagon_number(i):
    return int((i*((3*i)-1))/2)


def first_n_pentagon_nums(n):
    return set([pentagon_number(i) for i in range(1, n+1)])


def pairwise(L):
    """
    Given a sequence [1,2,3,4...],
    return a list of all pairwise
    combinations (where order doesn't matter).

    [1,2,3,4] => [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    """
    if isinstance(L, set):
        L = list(L)
        L.sort()

    pairs = list()
    for idx, item in enumerate(L):
        for element in L[idx+1:]:
            if item != 1:
                pairs.append((item, element))
    return pairs


if __name__ == '__main__':
    pent_nums = first_n_pentagon_nums(2500)
    pairs = pairwise(pent_nums)


    def expand_pentagon_nums(until_at_least=None):
        max_pent_num_idx = len(pent_nums)
        current = pentagon_number(max_pent_num_idx)
        pent_nums.add(current)

        next_pent_num = current
        idx = max_pent_num_idx

        while next_pent_num < until_at_least:
            pent_nums.add(next_pent_num)
            next_pent_num = pentagon_number(idx)
            idx = idx+1

        # Just for good measure :)
        pent_nums.add(pentagon_number(idx+2))
  
    print('Checking {} combinations of {} pentagon numbers...'.format(len(pairs), len(pent_nums)))

    strange_bedfellows = list()    

    for pair in pairs:
        left, right = pair

        pair_sum = left + right
        pair_diff = right - left

        if pair_sum > max(pent_nums):
            expand_pentagon_nums(until_at_least=pair_sum)

        if (pair_sum in pent_nums) and (pair_diff in pent_nums):
            strange_bedfellows.append(pair)

    found_pair = strange_bedfellows[0]
    left, right = found_pair

    print("Found pair: {}".format(found_pair))
    print("D: {}".format(right-left))
