#!/usr/bin/env python3

'''
Program:     PE-P11_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171009

Project Euler Problem 11:
    In the 20×20 grid below, four numbers along a diagonal line have 
    been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same 
    direction (up, down, left, right, or diagonally) in the 20×20 grid?

Great discussion on terminal colors in Python at:
https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
I opted for ANSI escape sequences.

Basic test set construction. I used list comprehension after laying these out.
---
Horizontal:
test_items = (int_matr[ypos][pos], int_matr[ypos][pos + 1],
                int_matr[ypos][pos + 2], int_matr[ypos][pos + 3])

Vertical:
test_items = (int_matr[pos][xpos], int_matr[pos + 1][xpos],
                int_matr[pos + 2][xpos], int_matr[pos + 3][xpos])

NW-SE diagonal:
test_items = (int_matr[pos][xpos], int_matr[pos + 1][xpos + 1],
                int_matr[pos + 2][xpos + 2], int_matr[pos + 3][xpos + 3])

NE-SW diagonal:
test_items = (int_matr[pos][xpos], int_matr[pos + 1][xpos - 1],
                int_matr[pos + 2][xpos - 2], int_matr[pos + 3][xpos - 3])

'''

from functools import reduce
from operator import mul
import argparse

def get_product(input_set):
    # Booooooo globals (actually useful here)
    global largest_product
    global winning_combo
    test_items = [int_matr[item[0]][item[1]] for item in input_set]
    producto = 0 if 0 in test_items else reduce(mul, test_items)
    if producto > largest_product:
        largest_product = producto
        winning_combo = input_set



# Number set from Project Euler; not truly a matrix, but vars refer
# to it that way. Refactor!
test_matr = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 '\
            '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 '\
            '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 '\
            '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 '\
            '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 '\
            '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 '\
            '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 '\
            '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 '\
            '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 '\
            '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 '\
            '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 '\
            '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 '\
            '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 '\
            '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 '\
            '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 '\
            '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 '\
            '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 '\
            '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 '\
            '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 '\
            '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 '.split()
            
# Get some inputs
parser = argparse.ArgumentParser()
parser.add_argument('-x', '--xdim',
                    required=True,
                    type=int,
                    help='X (horizontal) dimension of number group'
                    )
parser.add_argument('-y', '--ydim',
                    required=True,
                    type=int,
                    help='Y (vertical) dimension of number group'
                    )
parser.add_argument('-s', '--groupsize',
                    required=True,
                    type=int,
                    help='Group size (number of ints) to check'
                    )
all_args = parser.parse_args()
matr_x = all_args.xdim
matr_y = all_args.ydim
group_size = all_args.groupsize

# Can't do much if dimensions don't match input set
if matr_x * matr_y != len(test_matr):
    print('Input dimensions do not equal number set dimensions. Please try again.')
    quit()

# Building an integer set
int_matr = []
numset_pos = 0

# Finding largest subset and product
largest_product = 0
winning_combo = []
winning_str_pos = []

# Format help
text_red = '\033[91m'
fmt_end = '\033[0m'
text_bold = '\033[1m'

# Create set in defined proportions, i.e., 20x20
while numset_pos < matr_x * matr_y:
    int_matr.append([int(item) for item in test_matr[numset_pos:matr_x + numset_pos]])
    numset_pos += matr_x
    

# Number set processing START
# All horizontal combinations
for ypos in range(0, matr_y):
    for pos in range(0, matr_x):
        try:
            matr_positions = [[ypos, item] for item in range(pos, pos + group_size)]
            get_product(matr_positions)
        except:
            continue

# All vertical combinations
for xpos in range(0, matr_x):
    for pos in range(0, matr_y):
        try:
            matr_positions = [[item, xpos] for item in range(pos, pos + group_size)]
            get_product(matr_positions)
        except:
            continue

# NW-SE diag
for xpos in range(0, matr_x):
    for pos in range(0, matr_y):
        try:
            matr_positions = [[item, xpos + item] for item in range(pos, pos + group_size)]
            get_product(matr_positions)
        except:
            continue

# NE-SW diag
for xpos in range(matr_x - 1, 2, -1):     # Avoid wrap-around (negative index)
    for pos in range(0, matr_y):
        try:
            matr_positions = [[item, xpos - item] for item in range(pos, pos + group_size) if xpos - item >= 0]
            get_product(matr_positions)
        except:
            continue


# Prepare answers for print/output
# Get positions of winning group members in string
for item in winning_combo:
    winning_str_pos.append(item[0] * matr_x + item[1])

# Output original number set with "winning" numbers colored
for item in range(0, len(test_matr)):
    if item in winning_str_pos:
        output_item = text_red + text_bold + test_matr[item] + fmt_end + ' '
    else:
        output_item = test_matr[item] + ' '

    if item > 0 and item % matr_x == matr_x - 1:
        output_item += '\n'

    print(output_item, end="")    # Neat trick I learned just now

# Aaaaaand results
print('\nLargest product is {}.'.format(largest_product))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
