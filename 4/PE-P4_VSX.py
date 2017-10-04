#!/usr/bin/env python3

'''
Program:      PE-P4_VSX.py
Author:       vsx-gh (https://github.com/vsx-gh)
Created:      20171003

Project Euler Problem 4:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

'''

import argparse

def is_palindrome(candidate):
    """ Determines whether candidate is a palindrome (same forward as reverse) """
    if str(candidate) == str(candidate)[::-1]:
        return True

    return False



def find_largest_palindrome(num_digits):
    """ Finds the largest palindrome from two numbers of length num_digits """
    largest_palindrome = 0
    start_num = 10 ** num_digits - 1
    end_num = 10 ** (num_digits - 1) - 1

    for factor_1 in range(start_num, end_num, -1):
        for factor_2 in range(start_num, end_num, -1):
            if factor_1 < factor_2:
                continue

            producto = factor_1 * factor_2     # "product" not a reserved word?

            if is_palindrome(producto):
                if producto > largest_palindrome:
                    largest_palindrome = producto
                    largest_f1 = factor_1
                    largest_f2 = factor_2
    
    return largest_f1, largest_f2, largest_palindrome



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--numdigits',
                    required=True,
                    type=int,
                    help='N-digit number for which you want to find palindrome'
                    )
all_args = parser.parse_args()
input_digits = all_args.numdigits

# Perform the check
prod_1, prod_2, prod_product = find_largest_palindrome(input_digits)
print('Largest palindrome product of two {}-digit integers is {}, provided by '
        '{} x {}.'.format(input_digits, prod_product, prod_1, prod_2))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
