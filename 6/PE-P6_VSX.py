#!/usr/bin/env python3

'''
Program:     PE-P6_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171004

Project Euler Problem 6:
    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

There is a really good derived proof for a more efficient approach to
this problem in the Overview document you receive after submitting a
correct answer. I am not implementing that here, since it's not mine.

'''

import argparse

# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--begin',
                    required=True,
                    type=int,
                    help='Start of range'
                    )
parser.add_argument('-e', '--end',
                    required=True,
                    type=int,
                    help='End of range'
                    )
all_args = parser.parse_args()

# Do the math(s?)
sum_squares = sum((item ** 2 for item in range(all_args.begin, all_args.end + 1)))
squared_sum = sum(item for item in range(all_args.begin, all_args.end + 1)) ** 2
sq_diff = squared_sum - sum_squares

print('Difference of sum of squares and the square of the sum for {} and {} '
        'is {}.'.format(all_args.begin, all_args.end, sq_diff))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
