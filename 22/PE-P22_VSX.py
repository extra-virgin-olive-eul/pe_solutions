#!/usr/bin/python3

'''
Program:     PE-P22_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20220730

Project Euler Problem 22:
	Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
	over five-thousand first names, begin by sorting it into alphabetical order. Then
	working out the alphabetical value for each name, multiply this value by its
	alphabetical position in the list to obtain a name score.

	For example, when the list is sorted into alphabetical order, COLIN, which is worth
	3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a
	score of 938 × 53 = 49714.

	What is the total of all the name scores in the file?

Admittedly being super-lazy and not doing the sort myself.
'''

import string
import argparse

def calculate_name_score(name_input):
    name_score = 0
    for name_letter in list(name_input):
        name_score += alph_list.index(name_letter)

    return name_score

# Get inputs
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose',
                    required=False,
                    action='store_true',
                    help='Print verbose output',
                    )
all_args = parser.parse_args()
do_verbose = all_args.verbose

# Build easy alphabet for scoring - kludge zero-basing
alph_list = [''] + list(string.ascii_uppercase)

# File containing inputs
names_file = "p022_names.txt"
names_fhandle = open(names_file, "r")

# Grab file contents into a list of lists of integers
# 'Tis a tiny file, right? Right?!
all_names = [x.strip().replace('"','').split(',') for x in names_fhandle.readlines()]
names_fhandle.close()
all_names[0].sort()     # .sort() replaces original list. BEWARE!

# Again, prepend an empty value so multiplication doesn't fail (by 0, etc.)
all_names_pad = [''] + all_names[0]

total_score = 0
for person_name in all_names_pad[1:]:
    this_name_score = calculate_name_score(person_name) * all_names_pad.index(person_name)
    total_score += this_name_score

    # Output each person's score if you really want to
    if do_verbose:
        print(f'{person_name} score: {this_name_score}')

print(f'Total score for all names: {total_score}')
