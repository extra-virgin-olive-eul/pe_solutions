import argparse
import os

"""
USAGE:
=====

    This script provides an optional '-f', '--file' flag to point to a
    text file containing a properly formatted numeric triangle.

        Example:
        -------
        $ python3 generalized.py --file /path/to/triangle.txt

    By default, it will look for a file named 'p067_triangle.txt' in the current
    working directory.


ALGORITHM:
=========

    I learned about this approach in the forum postings for problem 18.

    Original Algorithm:
    ==================

    Consider this four-level triangle:

    75
    95 64
    17 47 82
    18 35 87 10

    Starting at the second to last row ([17, 47, 82]) and proceeding upward toward
    the root, replace each value with: current value + max(left child, right child).

    So in the case of 17 (first value in second-to-last row), we'd replace 17 with: 
        17 + max(18, 35) = 52
        
    Do this all the way up to the root:
        Replace each value with the original value + max(left child, right child). 

    Once you reach the root, it's modified value will be the max sum through the triangle.


    Modified Version:
    ================

    The above is a plenty clever solution, but I also wanted to be able to recover the sequence
    as well, *not* just its sum.

    In order to facilitate this, I replaced each value in the tree with a dict consisting
    of keys for "value" and "running_total." ("value" is the original value of each node
    and "running_total" is set to 0 by default.)

    After the max path has been computed, I can retrace its steps by starting at the root
    of the tree and, at each successive level, choosing the 'value' with the highest accompanying
    'running' value.

    Note:
    ----
    The only sort of tricky thing to keep in mind is that the keys to check will differ in the
    case of the second-to-last row. 
"""

def read_triangle_text(path_to_file):
    """ 
    Convert the contents of the file given by `path_to_file`
    into a list of lists representing the integer tree.

    Each node will be an unnamed dict containing the value of the 
    node and its running_total (to be updated during `compute_max_sum_of_previous_level`).
    """
    tree = list()
    with open(path_to_file, 'r') as f:
        for line in f.readlines():
            tree.append([{'value': int(i), 'running_total': 0} for i in line.replace('\n', '').split(' ')])
    return tree


def compute_max_sum_of_previous_level(level, tree):
    row = tree[level]

    if row == tree[len(tree)-2]:
        key = 'value'
    else:
        key = 'running_total'

    for idx, element in enumerate(row):
        element['running_total'] = element['value'] + max(tree[level+1][idx][key], tree[level+1][idx+1][key])


def find_max_seq_sum(tree):
    n = len(tree)-2
    while n >= 0:
        compute_max_sum_of_previous_level(n, tree)
        n = n-1
    return tree[0][0]['running_total']


def find_max_sequence(tree, level=0, idx=0, max_seq=None):
    """ 
    Starting at the root, recursively traverse the tree by choosing
    the next child with the greatest value.

    Once we reach the bottom-most-level, return the sequence.
    """
    if max_seq is None:
        max_seq = [tree[0][0]['value']]

    if level == len(tree)-1:
        return max_seq
    else:
        left, right = tree[level+1][idx], tree[level+1][idx+1]

        if level == len(tree)-2:
            key = 'value'
        else:
            key = 'running_total'

        if left[key] > right[key]:
            max_seq.append(left['value'])
        else:
            max_seq.append(right['value'])
            idx = idx+1

        return find_max_sequence(tree, level=level+1, idx=idx, max_seq=max_seq)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
            required=False,
            type=str,
            help="Path to text file containing numeric triangle (optional)."
    )

    args = parser.parse_args()

    if not args.file:
        path_to_file = os.path.join(os.getcwd(), 'p067_triangle.txt')
    else:
        path_to_file = args.file

    tree = read_triangle_text(path_to_file)
    find_max_seq_sum(tree)

    print("Read in {}-level tree from {}.".format(len(tree), path_to_file))
    print("Max sequence sum: {}".format(tree[0][0]['running_total']))
    print("Sequence: {}".format(find_max_sequence(tree)))
