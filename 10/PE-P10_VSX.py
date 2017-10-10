#!/usr/bin/env python3

'''
Program:     PE-P10_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171009

Project Euler Problem 10:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

'''

import math
import argparse

def test_prime(candidate):
    """ Tests if candidate is a prime number """
    candidate_sqrt = int(math.sqrt(candidate))
    range_end = 2

    # There is no "range" to test
    if candidate_sqrt < range_end:
        return True

    for div in range(range_end, candidate_sqrt + 1):
        if div == candidate_sqrt:
            if candidate % div == 0:
                return False
        elif candidate % div == 0:    # Another factor involved
            return False

    return True     # Passed all disqualification tests



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--rangeend',
                    required=True,
                    type=int,
                    help='Find sum of all primes below this input'
                    )
all_args = parser.parse_args()

# This is only ~1s faster than for loop in real-time (as tested on MacBook Air)
prime_sum = sum((test_item for test_item in range(2, all_args.rangeend) if test_prime(test_item)))
print(prime_sum)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
