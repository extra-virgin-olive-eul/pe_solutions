"""
I noticed you can think about the path through a given grid as a string.

Looking at the 2x2 example, the first path shown consists of four moves: 
2 right, 2 down. This path can be represented by the string: RRDD. 

All the possible paths through the 2x2 look like:

    DDRR
    DRDR
    DRRD
    RDDR
    RDRD
    RRDD

A path through a larger grid can be represented by a proportionally longer 
string.

3x3? DDDRRR
4x4? DDDDRRRR 
etc ...

In order to find all the possible paths, find the number of permutations 
of the string!
"""

from math import factorial

def possible_grid_paths(n):
    """ 
    n: the height (or width) of the square grid.
    """
    n = n * 2
    return factorial(n)/(factorial(n/2)*factorial(n/2))
