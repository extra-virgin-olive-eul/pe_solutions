import argparse
from itertools import product
import os

"""
My approach here is very similar to the approach I took in 15 [https://projecteuler.net/problem=15]

A given path through the tree can be represented by a string of L's and R's: 
    L denoting the next element in the sequence is down and to the left
    R denoting the next element in the sequence is down and to the right

Python's itertools library has a nice product function that will generate the strings I need.
(https://docs.python.org/3.6/library/itertools.html?highlight=product#itertools.product)

If I give `generate_possible_paths` a four-level tree, it will give back a collection of sequence
tuples representing each possible route through the tree (always starting at the top).

Example:
=======

tree = read_triangle_text('mini_triangle.txt')
for p in generate_possible_paths(tree):
    print(p)

    ('L', 'L', 'L')
    ('L', 'L', 'R')
    ('L', 'R', 'L')
    ('L', 'R', 'R')
    ('R', 'L', 'L')
    ('R', 'L', 'R')
    ('R', 'R', 'L')
    ('R', 'R', 'R')

`path_through_tree` takes a sequence (of L's / R's) and returns a list of ints corresponding
to those locations in the tree.

Since we can generate all possible paths _and_ resolve each path to a sequence of ints, 
we just need to find the max of the sums of the sequences.
    
Hence:

    all_possible_path_sums = [sum(path_through_tree(tree, seq)) for seq in generate_possible_paths(tree)]
    print(max(all_possible_path_sums))

"""


def generate_possible_paths(tree):
    return product('LR', repeat=len(tree)-1)


def read_triangle_text(path_to_file):
    """ 
    Convert the contents of the file given by `path_to_file`
    into a list of lists representing the integer tree.
    """
    tree = list()
    with open(path_to_file, 'r') as f:
        for line in f.readlines():
            tree.append(line.replace('\n', '').split(' '))
    return tree


def path_through_tree(tree, path_str):
    """
    :tree: a list of lists where each list is a level of a tree containing ints (00-99).

    For example, here's the tree produced by 'mini_triangle.txt':

    [['75'], 
     ['95', '64'], 
     ['17', '47', '82'], 
     ['18', '35', '87', '10']]

    :path_str: a string consisting of 'L's and 'R's such that each 'L' or 'R' represents
    which direction to traverse the tree. We always start at the root ['75'] and move
    downward.
    
    :return: a list of ints found at each point in the top-down path.

    Example:
    =======
        A path_str of 'LLR' for the example tree above would result in: [75, 95, 17, 35] 
    """
    level, idx = 0, 0
    sequence = [int(tree[level][idx])]
    for direction in path_str:
        level = level + 1
        if direction == 'R':
            idx = idx + 1
        sequence.append(int(tree[level][idx]))
    return sequence


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
            required=False,
            type=str,
            help="Path to text file containing numeric triangle (optional)."
    )

    args = parser.parse_args()

    if not args.file:
        path_to_file = os.path.join(os.getcwd(), 'full_triangle.txt')
    else:
        path_to_file = read_triangle_text(args.file)

    tree = read_triangle_text(path_to_file)

    all_possible_path_sums = [sum(path_through_tree(tree, seq)) for seq in generate_possible_paths(tree)]
    print(max(all_possible_path_sums))
