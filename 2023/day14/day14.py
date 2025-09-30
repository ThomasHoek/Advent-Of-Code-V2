import numpy as np


def find_up_idx(np_arr, loc: int) -> int:
    """
    find_up_idx returns index of last empty spot.

    Args:
        np_arr (np.array): numpy array of designated column
        loc (int): current rock we want to move north

    Returns:
        int: new rock location
    """
    if loc == 0:
        return loc
    else:
        i = 0
        for i in range(loc - 1, -1, -1):
            if np_arr[i] == ".":
                continue
            else:
                return i + 1
        return i


def puzzle(puzzle_input: list[str]) -> int:
    total = 0
    grid_input: list[list[str]] = []
    for i in range(len(puzzle_input)):
        grid_input.append(list(puzzle_input[i]))

    np_grid = np.array(grid_input)
    up_grid = np_grid.copy()

    grid_size = np_grid.shape
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            if np_grid[row][col] == "O":
                out_idx = find_up_idx(up_grid[:, col], row)
                total += (grid_size[1] - out_idx)
                up_grid[row][col] = "."
                up_grid[out_idx][col] = "O"
    return total


if __name__ == "__main__":
    import sys
    import os
    from io import TextIOWrapper
    from typing import TextIO

    try:
        final: bool = "final" in sys.argv
        file: bool = "file" in sys.argv
        clock: bool = "time" in sys.argv

    except IndexError:
        final = False
        file = False
        clock = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open("out.txt", "w")
        sys.stdout = f

    if clock:
        import time

        start: float = time.time()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 136

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
