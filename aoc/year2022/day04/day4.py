import os


def puzzle(puzzle_input):
    puzzle_input = [x.rstrip() for x in puzzle_input]

    counter = 0
    for first, second in [x.split(",") for x in puzzle_input]:
        first_max, first_max = [int(x) for x in first.split("-")]
        second_min, second_max = [int(x) for x in second.split("-")]

        # first engulfs second
        if (first_max <= second_min) and (first_max >= second_max):
            counter += 1

        elif (first_max >= second_min) and (first_max <= second_max):
            counter += 1

    return counter
