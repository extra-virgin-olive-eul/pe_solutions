#!/usr/bin/env python3

'''
Program:     PE-P16_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171114

Project Euler Problem 16:
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
'''
import argparse

# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--intbase',
                    required=True,
                    type=int,
                    help='Base number you want to use'
                    )
parser.add_argument('-e', '--inputexp',
                    required=True,
                    type=int,
                    help='Exponent to apply to the base'
                    )
all_args = parser.parse_args()
int_base = all_args.intbase
input_exp = all_args.inputexp

# Some error handling
if int_base < 0 or input_exp < 0:
    print('Please input positive values. Exiting.')
    quit()

# Sum generator seems like a good choice
total_sum = sum((int(item) for item in str(int_base ** input_exp)))
print('Total sum of digits in {}^{} is {}'.format(int_base, input_exp, total_sum))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
