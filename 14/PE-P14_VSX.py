#!/usr/bin/env python3

'''
Program:     PE-P14_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171019

Project Euler Problem 14:
    The following iterative sequence is defined for the set of positive integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        
                    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) 
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

'''

import argparse

def calculate_collatz_num(input_int):
    if input_int % 2 == 0:
        return int(input_int / 2)
    
    return int(3 * input_int + 1)



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--upperbound',
                    required=True,
                    type=int,
                    help='Upper boundary for starter of Collatz sequence'
                    )
all_args = parser.parse_args()
upper_bound = all_args.upperbound

# Keep info on the tops
longest_chain_len = 0
longest_starter = 0
longest_list = []

# Might be a pattern shortcut, but I don't know it
for test_int in range(13, upper_bound):
    collatz_num = test_int
    collatz_list = []

    while collatz_num != 1:
        if collatz_num == 1:
            collatz_list.append(1)
            break
        collatz_list.append(collatz_num)
        collatz_num = calculate_collatz_num(collatz_num)

    if len(collatz_list) > longest_chain_len:
        longest_chain_len = len(collatz_list)
        longest_starter = test_int
        longest_list = collatz_list

print('Longest Collatz chain length for starter items under {} is '
        '{} at {} items.'.format(upper_bound, longest_starter, longest_chain_len))
#print(longest_list[0:20])     # Could be a long list. Be careful and limit print.

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
