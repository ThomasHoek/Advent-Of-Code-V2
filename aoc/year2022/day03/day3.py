import os
from math import floor


def puzzle(puzzle_input) -> int:
    puzzle_input = [x.rstrip() for x in puzzle_input]

    total = 0
    for line in puzzle_input:
        letter = list(
            set(line[: floor(len(line) / 2)]).intersection(
                set(line[floor(len(line) / 2) :])
            )
        )[0]

        if letter.isupper():
            total += (ord(letter) - 64) + 26
        else:
            total += (ord(letter) - 97) + 1

    return total
