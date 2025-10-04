# [Done] exited with code=0 in 0.305 seconds

import copy
from aoc.year2020.day09.day9 import puzzle as part1Puzzle


def puzzle(input_file) -> int:
    invalid = part1Puzzle(input_file)
    input_file = [int(word.rstrip()) for word in input_file]

    for i in range(len(input_file)):
        total_lst = [input_file[i]]
        i_counter = copy.deepcopy(i)

        while sum(total_lst) <= invalid:
            try:
                i_counter += 1
                total_lst.append(input_file[i_counter])

            except IndexError:
                break

            if sum(total_lst) == invalid:
                return min(total_lst) + max(total_lst)

    return -1
