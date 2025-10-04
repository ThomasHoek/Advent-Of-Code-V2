import os


def puzzle(puzzle_input) -> int:
    puzzle_input = [x.rstrip() for x in puzzle_input]
    bin_size = 3
    puzzle_input = [
        puzzle_input[i : i + bin_size] for i in range(0, len(puzzle_input), bin_size)
    ]

    total = 0
    for line1, line2, line3 in puzzle_input:
        letter = list(set(line1).intersection(set(line2).intersection(set(line3))))[0]

        if letter.isupper():
            total += (ord(letter) - 64) + 26
        else:
            total += (ord(letter) - 97) + 1

    return total
