#!/usr/bin/env python3

'''
Program:     PE-P5_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171003

Project Euler Problem 5:
    2520 is the smallest number that can be divided by each of the numbers 
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all 
    of the numbers from 1 to 20?

'''

import argparse

def test_divisors(range_start, range_end, test_int):
    """ Determines whether test_int divisible by integers 20 to 1 """
    for div in range(range_start, range_end, -1):    # If these pass, 10 to 1 will as well
        if test_int % div != 0:
            return False

    return True



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--begin',
                    required=True,
                    type=int,
                    help='Start of range to check'
                    )
parser.add_argument('-e', '--end',
                    required=True,
                    type=int,
                    help='End of range to check'
                    )
all_args = parser.parse_args()

# Set initial conditions
candidate = all_args.end
int_found = False
answer = 0

while int_found == False:
    int_found = test_divisors(all_args.end, all_args.begin, candidate)
    if int_found == True:
        answer = candidate
    else:
        candidate += all_args.end     # Answer will always be a multiple of range end

print('Smallest number divisible by each number in range 1 - 20 is {}.'.format(answer))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
