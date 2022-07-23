#!/usr/bin/python3

'''
Program:     PE-P18_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20220723

Project Euler Problem 18:
    By starting at the top of the triangle below and moving to adjacent numbers on the
    row below, the maximum total from top to bottom is 23.

        3
       7 4
      2 4 6
     8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                                     75
                                   95 64
                                 17 47 82
                               18 35 87 10
                             20 04 82 47 65
                           19 01 23 75 03 34
                         88 02 77 73 07 63 67
                       99 65 04 28 06 16 70 92
                     41 41 26 56 83 40 80 70 33
                   41 48 72 33 47 32 37 16 94 29
                 53 71 44 65 25 43 91 52 97 51 14
               70 11 33 28 77 73 17 78 39 68 17 57
             91 71 52 38 17 14 91 43 58 50 27 29 48
           63 66 04 68 89 53 67 30 73 16 69 87 40 31
         04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

	NOTE: As there are only 16384 routes, it is possible to solve this problem by trying
	every route. However, Problem 67, is the same challenge with a triangle containing
    one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

    vsx-gh NOTE: The bottom_up() function also works fine for Problem 67; no significant
    impact on system resources.

    TODO: Is it possible to track the path using the bottom-up approach?
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
tri_fname = "full_triangle.txt"
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
