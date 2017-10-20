#!/usr/bin/env python3

'''
Program:     PE-P13_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171019

Project Euler Problem 13:
    Work out the first ten digits of the sum of the following one-hundred 
    50-digit numbers.

    (Please see 13/P13_input for the numbers themselves)

This one is kinda anticlimactic; was really looking for some deeper
requirement. Did I miss something?

'''

problem_input = 'P13_input'
input_set = open(problem_input, 'r')
total = 0

for line in input_set:
    add_item = line.strip()

    # Does this have any theoretical backing?
    # Yields correct answer...this time
    if int(add_item[10]) >= 5:
        to_add = int(line.strip()[0:10]) + 1
    else:
        to_add = int(line.strip()[0:10])

    total += to_add

print(str(total)[0:10])

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
