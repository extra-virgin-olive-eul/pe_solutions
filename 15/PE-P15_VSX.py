#!/usr/bin/env python3

'''
Program:     PE-P15_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171109

Project Euler Problem 15:
    Starting in the top left corner of a 2×2 grid, and only being able to 
    move to the right and down, there are exactly 6 routes to the bottom 
    right corner.

    <There is a nifty diagram here.>

    How many such routes are there through a 20×20 grid?
'''

import argparse
import math

# Get lattice length
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--llen',
                    required=True,
                    type=int,
                    help='Lattice length'
                    )
all_args = parser.parse_args()
lattice_l = all_args.llen

# This problem can be solved using Pascal's triangle!
# Starting rows 
p_tri = [[1], [1, 1]]

# For lattice turned on its side, number of rows is twice the length of
# a side plus one. It helps to think of it as the number of "dots" or
# items _between_ squares of the lattice
for item in range(2, 2 * lattice_l + 1):
    row = [1]
    
    for member in range(1, len(p_tri[item - 1])):
        row_item = p_tri[item - 1][member - 1] + p_tri[item - 1][member]
        row.append(row_item)

    row.append(1)
    p_tri.append(row)

'''
for row in p_tri:
    print(row)
'''

# "Point" of the rotated lattice/cube is center of last row of the triangle
max_paths = p_tri[-1][int(len(p_tri[-1]) / 2)]
print('Maximum number of paths (only right and down) for {} x {} lattice '
        'is {}'.format(lattice_l, lattice_l, max_paths))

# Can also use binomial coefficients
path_num = int(math.factorial(lattice_l * 2) / math.factorial(lattice_l) ** 2)
print('Maximum number of paths (only right and down) for {} x {} lattice '
        'is {}'.format(lattice_l, lattice_l, path_num))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
