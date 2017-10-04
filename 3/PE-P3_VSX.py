#!/usr/bin/env python3

'''
Program:      PE-P3_VSX.py
Author:       vsx-gh (https://github.com/vsx-gh)
Created:      20171002

Project Euler Problem 2:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

This program approaches the problem from the perspective that the only tests
needed to find both the factors of an input and to test whether a factor is
prime is to test the range 2..sqrt(input). For example, the factors of 24 are:

    1 x 24
    2 x 12
    3 x 8
    4 x 6
    6 x 4
    8 x 3
    12 x 2
    24 x 1

The breakover point where we start to repeat happens after "4 x 6". If we test
up to and including sqrt(24) (which is 4 and some change), we will grab the 
test for 4 and 6 will come along with it. This divide-and-conquer strategy 
eliminates a big chunk of the search space and avoids a brute-force approach.

Since a number is not prime if it has any factors besides itself and 1, we are
once again just looking for factors; so, we can use the same test range.

Prime tests are almost an entire field unto themselves, so there is probably
room for improvement here. But I decided not to get any fancier than I did here.

I hope I hope I hope this program does not have any serious flaws. I have tested
with several inputs, including the problem input, and my answer was accepted.
I'm still open to suggestions for improvements.

'''

import argparse
import math

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



def find_largest_pf(input_item):
    """ Finds largest prime factor of input_item """
    largest_pf = 1

    for item in range(1, int(math.sqrt(input_item)) + 1):
        if input_item % item == 0:     # Item is a factor of input_item
            div = int(input_item / item)     # Python 3 will return float
            if test_prime(div):
                largest_pf = div
            elif test_prime(item):
                largest_pf = item
 
    return largest_pf



def find_factors(input_item):
    """ Finds all factors of input_item """
    factors = []

    for item in range(1, int(math.sqrt(input_item)) + 1):
        if input_item % item == 0:
            factors.append(item)
            factors.append(int(input_item / item))

    return sorted(factors, reverse=True)



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',
                    required=True,
                    type=int,
                    help='Input integer to test'
                    )
all_args = parser.parse_args()
input_int = all_args.input

# Run tests
print('All factors of {}: {}.'.format(input_int, find_factors(input_int)))
print('Largest prime factor of {} is {}.'.format(input_int, find_largest_pf(input_int)))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
