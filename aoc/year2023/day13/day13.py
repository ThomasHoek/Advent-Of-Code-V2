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
        found = True
        np_grid = np.matrix(grid)

        rot = False
        while found:
            grid_len = len(np_grid)
            for i in range(1, math.ceil(grid_len / 2)):
                # get two matrix slices and flip the second. Use ALL to see if all True.
                if (np_grid[:i] == np.flipud(np_grid[i : i + i])).all():
                    found = False

                    add_num = len(np_grid[:i])
                    if rot:
                        total += add_num

                    else:
                        total += add_num * 100

                elif (np_grid[-i:] == np.flipud(np_grid[-i * 2 : -i])).all():
                    found = False
                    add_num = grid_len - len(np_grid[-i:])

                    if rot:
                        total += add_num

                    else:
                        total += add_num * 100
            # need to rotate 270
            np_grid = np.rot90(np_grid, k=3)
            rot = True
    return total
