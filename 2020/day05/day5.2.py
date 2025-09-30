# [Done] exited with code=0 in 0.297 seconds
import math
import numpy as np

input_file = open("input.txt", "r").readlines()


def partioning(first, second, letter):
    if letter == "F" or letter == "L":
        return first, math.floor(np.mean([first, second]))

    elif letter == "B" or letter == "R":
        return math.ceil(np.mean([first, second])), second


total_list = []
for board_pass in input_file:
    first_row = 0
    second_row = 127

    first_col = 0
    second_col = 7

    for i in range(len(board_pass)):
        if board_pass[i] == "B" or board_pass[i] == "F":
            first_row, second_row = partioning(first_row,
                                               second_row,
                                               board_pass[i])

        elif board_pass[i] == "L" or board_pass[i] == "R":
            first_col, second_col = partioning(first_col,
                                               second_col,
                                               board_pass[i])

    total_list.append(first_row * 8 + first_col)

lst = set(list(range(1, max(total_list))))

total_list.sort()
total_list = set(total_list)
print(lst - total_list)
