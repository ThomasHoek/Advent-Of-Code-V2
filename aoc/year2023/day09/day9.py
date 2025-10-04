import numpy as np


def puzzle(puzzle_input: list[str]) -> int:
    total = 0
    for line in puzzle_input:
        num_lst: list[int] = [int(x) for x in line.split(" ")]
        num_arr = np.array(num_lst)

        last_lst: list[int] = [num_arr[-1]]

        # calc difference, take last num and sum the list.
        while sum(num_arr) != 0:
            num_arr = np.diff(num_arr)
            last_lst.append(num_arr[-1])
            # print(num_arr)
        total += sum(last_lst)
    return total
