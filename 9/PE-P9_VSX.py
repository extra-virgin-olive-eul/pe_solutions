#!/usr/bin/env python3

'''
Program:     PE-P9_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171009

Project Euler Problem 9:
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a ** 2 + b ** 2 = c ** 2
    For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

'''

import math
import argparse
from operator import mul
import functools

# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sum',
                    required=True,
                    type=int,
                    help='Sum of a + b + c in Pythagorean triple you seek '\
                        '(may not exist)'
                    )
all_args = parser.parse_args()
triplets = []     # Hold found triplet(s)

# Don't need to go past the sum we're seeking
for a in range(1, all_args.sum):
    for b in range(a + 1, all_args.sum):
        c = math.sqrt(a ** 2 + b ** 2)
        if c % 1 == 0 and b < c and sum((a, b, c)) == all_args.sum:    # Check c is a natural number
            triplets.append((a, b, int(c)))

if len(triplets) > 0:
    for triplet in triplets:
        print('a, b, c: {}; product: {}'.format(triplet, functools.reduce(mul,triplet)))
else:
    print('No Pythagorean triplet for your input value.')

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
