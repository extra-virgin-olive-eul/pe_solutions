#!/usr/bin/env python3

'''
Program:    PE-P1_VSX.py
Author:     vsx-gh (https://github.com/vsx-gh)
Created:    20170927

Project Euler Problem 1:
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

'''

import argparse

def find_sum_iteration(range_start, range_end, *args):
    """ Find sum of multiples using iteration """
    num_sum = 0

    for item in range(range_start, range_end):
        for div in args:
            if item % div == 0:
                num_sum += item
                break    # Any match, not all

    return num_sum



def find_multiple(int_in, *args):
    """ Return input number if a multiple of any item in *args """
    for div in args:
        if int_in% div == 0:
            return int_in 
    return 0



def find_sum_generation(range_start, range_end, *args):
    """ Return sum of multiples in number range, generator approach """
    for item in range(range_start, range_end):
        if find_multiple(item, *args):
            yield item



# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--method',
                    required=True,
                    type=int,
                    choices=[1, 2, 3],
                    help='Method of solving problem: \
                    1) Iteration \
                    2) Functions and generators \
                    3) Comprehension/golf \
                    '
                    )
parser.add_argument('-s', '--start',
                    required=True,
                    type=int,
                    help='Range start'
                    )
parser.add_argument('-e', '--end',
                    required=True,
                    type=int,
                    help='Range end'
                    )
parser.add_argument('args',
                    type=int,
                    nargs=argparse.REMAINDER,
                    )
all_args = parser.parse_args()
solve_method = all_args.method

# Perform operation based on method chosen
if solve_method == 1:
    print(find_sum_iteration(all_args.start, all_args.end, *all_args.args))
elif solve_method == 2:
    print(sum(find_sum_generation(all_args.start, all_args.end, *all_args.args)))
elif solve_method == 3:
    print(sum((item for item in range(all_args.start, all_args.end) if any(item % div == 0 for div in all_args.args))))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
