#!/usr/bin/env python3

'''
Program:     PE-P17_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171114

Project Euler Problem 17:
   If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
   then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

   If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
   in words, how many letters would be used?


   NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
   forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
   20 letters. The use of "and" when writing out numbers is in compliance with 
   British usage.
'''

import argparse
import math

def process_hundreds(input_int):
    """ Converts integer (< 1000) to lexical equivalent """

    out_str = ""
    items_dict = {}     # {'100': <number of hundreds>}, etc.
    dec_list = [100, 10, 1]
    num_left = input_int
    
    # Find out how many of each place we have
    for item in dec_list:
        if int(num_left / item) == 0:
            items_dict[str(item)] = 0
        else:
            items_dict[str(item)] = int(num_left / item)
            num_left = num_left % item

    # Interaction of tens and ones has big effect on lexical display
    tens_ones = items_dict['10'] * 10 + items_dict['1'] * 1
    if tens_ones < 20 and tens_ones > 0:     # 1 - 19
        add_to = num_dict[str(tens_ones)]
    elif tens_ones >= 20 and tens_ones % 10 == 0:    # 20, 30, 40, etc.
        add_to = num_dict[str(items_dict['10'] * 10)]
    elif tens_ones >= 20 and tens_ones % 10 != 0:    # 21, 36, 44, etc.
        add_to = num_dict[str(items_dict['10'] * 10)] + '-' \
                + num_dict[str(items_dict['1'] * 1)]
    else:
        add_to = ''

    # Given British English requirements of the assignment, this block is needed
    # Otherwise hundreds can be processed like anything else non-tens and non-ones
    if items_dict['100'] > 0:
        out_str = out_str + num_dict[str(items_dict['100'])] + ' ' \
                + num_dict['100']
        if tens_ones > 0:
            if lang_type == 'be':
                out_str = out_str + ' and ' + add_to
            else:
                out_str = out_str + ' ' + add_to
    else:
        out_str += add_to

    return out_str



def get_lexical(input_num):
    """ Converts any input_num to words. Let's get lexical. """

    # Find starting divisor
    order_mag = int(10 ** (len(str(input_num)) - 1))
    num_as_str = ""
    remainder = input_num 

    # Proceed by thousands; each set will be processed as a group < 1000
    # and then we step down
    while order_mag >= 1000:
        if int(math.log10(order_mag)) % 3 != 0:
            order_mag = int(order_mag / 10)
            continue

        # This is how many of current term we have, i.e., 359 millions
        # Go off and process 359, then tack on the place term's name
        proc_term = int(remainder / order_mag)
        add_num = process_hundreds(proc_term) + ' ' \
                + num_dict[str(order_mag)] + ' '
        num_as_str += add_num

        # What's left over goes to next round with 1/1000th order of magnitude
        remainder = remainder % order_mag
        order_mag = int(order_mag / 1000)

    num_as_str += process_hundreds(remainder)

    return num_as_str



# Should be all the conversions we need; build the rest from these
num_dict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
            '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
            '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
            '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty',
            '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', 
            '80': 'eighty', '90': 'ninety', '100': 'hundred', '1000': 'thousand',
            '1000000': 'million', '1000000000': 'billion', 
            '1000000000000': 'trillion', '1000000000000000': 'quadrillion'}

# Get inputs 
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputint',
                    required=True,
                    type=int,
                    help='Input integer to calculate'
                    )
parser.add_argument('-s', '--startint',
                    required=True,
                    type=int,
                    help='Starting point for integer range'
                    )
# This was an awesome idea from Caroline
parser.add_argument('-e', '--english',
                    required=True,
                    choices=['ae', 'be'],
                    help='English variant to use (American or British)'
                    )
all_args = parser.parse_args()
process_int = all_args.inputint
range_start = all_args.startint
lang_type = all_args.english

# Error check
if range_start > process_int:
    print('Error: Start of range larger than end. Try again.')
    quit()

char_total = 0

# Build some words from numbers in range
for elem in range(range_start, process_int + 1):
    stringy_int = get_lexical(elem) 
    num_chars = len(stringy_int.strip().replace('-', '').replace(' ', ''))
    char_total += num_chars
    print(stringy_int)

# Total characters in 1..process_int
print('Spelling out numbers using {} between {} and {} is {}'.format(
        lang_type.upper(), range_start, process_int, char_total))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
