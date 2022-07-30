#!/usr/bin/python3

'''
Program:     PE-P20_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20220723

Project Euler Problem 20:
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits
    in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
'''

import argparse

def find_factorial(fac_input):
    fac_output = 1

    # Clear-cut approach: Loop down from input to 1, multiply each time
    for item in range(fac_input, 1, -1):
        fac_output *= item

    return fac_output



def find_factorial_recursive(fac_input):
    fac_output = 1

    # Recurse function until we're down to 1
    while fac_input > 1:
        fac_output *= fac_input
        fac_input -= 1
        find_factorial_recursive(fac_input)

    return fac_output



def sum_factorial_digits(fac_product):
    # Too much casting! This doesn't feel Pythonic.
    digit_sum = 0
    digits_list = str(fac_product)

    for digit in digits_list:
        digit_sum += int(digit)

    return digit_sum

# Get inputs
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',
                    required=True,
                    type=int,
                    help='Number whose factorial you are calculating'
                    )
parser.add_argument('-r', '--recurse',
                    required=False,
                    action='store_true',
                    help='Use recursion to find factorial of input'
                    )
all_args = parser.parse_args()
find_fac_for = all_args.input
do_recursive = all_args.recurse

# Use recursive approach if specified; loop otherwise
if do_recursive:
    get_fac = find_factorial_recursive(find_fac_for)
else:
    get_fac = find_factorial(find_fac_for)

# Sum up the digits in the answer to the factorial
fac_sum = sum_factorial_digits(get_fac)

# Output results
print(f'{find_fac_for}!: {get_fac}')
print(f'Sum of digits in {find_fac_for}!: {fac_sum}')
