import numpy as np


def puzzle(puzzle_input: list[str]) -> int:
    total = 0
    for line in puzzle_input:
        num_lst: list[int] = [int(x) for x in line.split(" ")]
        num_arr = np.array(num_lst)

        # get all last numbers and calculate the difference until sum is 0
        last_lst: list[int] = [num_arr[0]]
        while sum(num_arr) != 0:
            num_arr = np.diff(num_arr)
            last_lst.append(num_arr[0])

        # reverse the list, cummulative difference.
        last_lst.reverse()
        for i in range(len(last_lst) - 1):
            last_lst[i + 1] = last_lst[i + 1] - last_lst[i]

        total += last_lst[-1]
    return total

