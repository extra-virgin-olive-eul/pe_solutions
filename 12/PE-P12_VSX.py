#!/usr/bin/env python3

'''
Program:     PE-P12_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171019

Project Euler Problem 12:
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The 
    first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:
    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.
    What is the value of the first triangle number to have over five hundred divisors?
'''

import math
import argparse

def find_factors(input_item, min_divisors):
    """
    Finds all factors of input_item
    :param input_item:
    :param min_divisors
    :return: list containing factors for input item if len > min_divisors
    """

    factors = []

    for item in range(1, int(math.sqrt(input_item)) + 1):
        if input_item % item == 0:
            factors.append(item)
            factors.append(int(input_item / item))

    if len(factors) > min_divisors:
        return sorted(factors)
    
    return []



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--numdivisors',
                    required=True,
                    type=int,
                    help='Minimum number of divisors answer must have'
                    )
all_args = parser.parse_args()
num_divisors = all_args.numdivisors

# Test items
factor_set = []
test_int = 0
triangle_num = 0

# Function will return empty list unless number divisors reached
while len(factor_set) == 0:
    test_int += 1
    triangle_num = sum(range(0, test_int + 1))
    factor_set = find_factors(triangle_num, num_divisors)

print('First triangle number with over {} divisors is {}'.format(num_divisors, triangle_num))
#print(factor_set)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
