import numpy as np
import math


def puzzle(puzzle_input: list[str]) -> int:
    puzzle_idx = 0
    puzzle_split: list[list[bool]] = [[]]
    for line in puzzle_input:
        if line == "":
            puzzle_split.append([])
            puzzle_idx += 1
        else:
            to_bin_list = line.replace("#", "1").replace(".", "0")
            puzzle_split[puzzle_idx].append([int(x) for x in to_bin_list])

    total = 0
    for grid in puzzle_split:
        np_grid = np.matrix(grid)

        rot = False
        biggest_num = (0, False)
        while True:
            grid_len = len(np_grid)
            for i in range(1, math.ceil(grid_len / 2)):
                #  create the up and down matrix
                up_matrix = np_grid[:i] == np.flipud(np_grid[i : i + i])
                down_matrix = np_grid[-i:] == np.flipud(np_grid[-i * 2 : -i])

                # count false in it
                up_false = up_matrix.size - np.count_nonzero(a=up_matrix)
                down_false = down_matrix.size - np.count_nonzero(down_matrix)

                # if False is 1, store and find highest | This is prob not needed.
                if up_false == 1:
                    add_num = len(np_grid[:i])
                    if add_num > biggest_num[0]:
                        biggest_num = (add_num, rot)

                elif down_false == 1:
                    add_num = grid_len - len(np_grid[-i:])

                    if add_num > biggest_num[0]:
                        biggest_num = (add_num, rot)

            # need to rotate 270
            np_grid = np.rot90(np_grid, k=3)
            if rot:
                break
            else:
                rot = True

        if biggest_num[1]:
            total += biggest_num[0]
        else:
            total += biggest_num[0] * 100
    return total
