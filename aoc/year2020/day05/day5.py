# [Done] exited with code=0 in 0.33 seconds
import math
import numpy as np


def partioning(first, second, letter):
    if letter == "F" or letter == "L":
        return first, math.floor(np.mean([first, second]))

    elif letter == "B" or letter == "R":
        return math.ceil(np.mean([first, second])), second


def puzzle(puzzle_input) -> int:
    highest_pass = 0
    for board_pass in puzzle_input:
        first_row = 0
        second_row = 127

        first_col = 0
        second_col = 7

        for i in range(len(board_pass)):
            if board_pass[i] == "B" or board_pass[i] == "F":
                first_row, second_row = partioning(first_row, second_row, board_pass[i])

            elif board_pass[i] == "L" or board_pass[i] == "R":
                first_col, second_col = partioning(first_col, second_col, board_pass[i])

        high_pass = first_row * 8 + first_col
        highest_pass = high_pass if high_pass > highest_pass else highest_pass

    return highest_pass
