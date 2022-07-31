#!/usr/bin/python3

'''
Program:     PE-P21_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20220718

Project Euler Problem 21:
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
    divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each
    of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 
    110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so
    d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
'''

import argparse

def find_divisors(num_input):
    ''' Find all divisors of num_input and return sum '''
    divs = []
    for item in range(1, num_input):
        if item in divs:
            continue

        # If no remainder, add items to list
        if num_input % item == 0:
            if item != 1:     # Problem excludes initial num_input
                divs.append(int(num_input / item))
            divs.append(item)

    # Divisor sets containing only [1] need no further evaluation
    if len(divs) > 1:
        return sum(divs)
    else:
        return 0

# Get inputs 
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--limit',
                    required=True,
                    type=int,
                    help='Limit to which to calculate sum of amicables'
                    )
parser.add_argument('-d', '--debug',
                    required=False,
                    action='store_true',
                    help='Print amicables list'
                    )
all_args = parser.parse_args()
ami_limit = all_args.limit
is_debug_mode = all_args.debug

amicables = []

# Could prolly binary tree or otherwise split this sucker, but it's loops for now
for ami_candidate in range(1, ami_limit):
    if ami_candidate in amicables:
        continue

    div_sum = find_divisors(ami_candidate)

    if div_sum == 0:
        continue

    # Find divisors (and sum) of the original input's divisor sum; if equal, they're amicables!
    if find_divisors(div_sum) == ami_candidate and div_sum != ami_candidate:
        for amicable in (div_sum, ami_candidate):
            if amicable not in amicables:
                amicables.append(amicable)

# Output the list of amicables if desired
if is_debug_mode:
    print(f"Amicables list under {ami_limit}: {amicables}")

# Output sum of all amicables under limit
print(f"Sum of all amicables under {ami_limit}: {sum(amicables)}")
