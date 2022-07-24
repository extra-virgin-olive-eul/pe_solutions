#!/usr/bin/python3

'''
Program:     PE-P67_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20220723

Project Euler Problem 67:
	By starting at the top of the triangle below and moving to adjacent numbers on the row
	below, the maximum total from top to bottom is 23.

	   3
	  7 4
	 2 4 6
	8 5 9 3

	That is, 3 + 7 + 4 + 9 = 23.

	Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/
	Target As...'), a 15K text file containing a triangle with one-hundred rows.

	NOTE: This is a much more difficult version of Problem 18. It is not possible to try 
	every route to solve this problem, as there are 299 altogether! If you could check one
	trillion (1012) routes every second it would take over twenty billion years to check 
	them all. There is an efficient algorithm to solve it. ;o)
'''

def print_hl_path(input_triangle, line_map):
    # Output triangle with selected path
    output_red = '\033[31m'
    output_reset = '\033[00m'
    spacer = len(input_triangle[-1]) - 1

    for tri_line in input_triangle:
        out_list = f'{" " * (spacer - int(input_triangle.index(tri_line)))}'

        for item in range(0, len(tri_line)):
            if tri_line[item] < 10:     # Zero-pad single-digits
                print_item = f'0{tri_line[item]}'
            else:
                print_item = tri_line[item]

            # Output selected item in color
            if item == line_map[str(input_triangle.index(tri_line))]:
                out_list += f"{output_red}{print_item}{output_reset} "
            else:
                out_list += f'{print_item} '

        print(out_list)



def path_sum_naive_max(int_triangle):
    """
    Ultra-naive approach: Choose largest number from each pair of adjacents
    This does not necessarily work - the small example in this problem is a concidence
    (and how they get you).
    """

    line_choices = {'0': 0}

    # Start at the start
    path_sum = int_triangle[0][0]
    line_pos = 0
    left_pos = 0
    right_pos = 0

    for item in range(1, len(int_triangle)):
        left_pos = line_pos

        # Can't go past end of line
        if line_pos == len(int_triangle[item]):
            right_pos = line_pos
        else:
            right_pos = line_pos + 1

        # Find index in next line based on value of each position
        if int_triangle[item][left_pos] > int_triangle[item][right_pos]:
            line_pos = left_pos
        else:
            line_pos = right_pos

        line_choices[str(item)] = line_pos
        path_sum += max(int_triangle[item][left_pos], int_triangle[item][right_pos]) 

    return path_sum, line_choices
        


def bottom_up(int_triangle):
    # Start from two rows up from bottom to evaluate last two rows at start
    # Move up one row each time after that
    # Bottom row always gets replaced with highest sums to that point
    for item in range(len(int_triangle) - 2, -1, -1):
        new_row = []
        for pos in range(0, len(int_triangle[item]), 1):
            down_right = pos + 1
        
            # New row item will be the max of the two possible sums
            new_row.append(max(
                int_triangle[item][pos] + int_triangle[item + 1][pos],
                int_triangle[item][pos] + int_triangle[item + 1][down_right]
                )
            )
                
        int_triangle[item] = new_row

    return int_triangle[0][0]



# File containing inputs
tri_fname = "p067_triangle.txt"
tri_file = open(tri_fname, "r")

# Grab file contents into a list of lists of integers
input_triangle = []
for item in tri_file.readlines():
    input_triangle.append([int(x) for x in item.strip().split(' ')])
tri_file.close()

#max_path_sum, path_map = path_sum_naive_max(input_triangle)
#print_hl_path(input_triangle, path_map)
max_path_sum = bottom_up(input_triangle)

# Output max path sum results
print(f'Max path sum: {max_path_sum}')
