import os

def calc_win(x, y):
    # rock
    if x == "A":
        # paper
        if y == "Y":
            return 6
        # scissor
        elif y == "Z":
            return 0
        return 3

    # paper
    if x == "B":
        # scissor
        if y == "Z":
            return 6
        # rock
        elif y == "X":
            return 0
        return 3

    # scissor
    if x == "C":
        # rock
        if y == "X":
            return 6
        # scissor
        elif y == "Y":
            return 0
        return 3


def puzzle(puzzle_input):
    puzzle_input = [x.rstrip().split(" ") for x in puzzle_input]

    point_dict = {"X": 1, "Y": 2, "Z": 3}

    total_points = 0
    for first, second in puzzle_input:
        total_points += point_dict[second]
        total_points += calc_win(first, second)

    return total_points
