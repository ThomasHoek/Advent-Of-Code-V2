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


def get_score(np_grid) -> int:
    flipped_grid = np.flipud(np_grid)

    total = 0
    for counter, row in enumerate(flipped_grid, start=1):
        total += sum([x == "O" for x in row]) * counter

    return total


def cycle(np_grid):  # -> NDArray[str]:
    for _ in range(4):
        up_grid = np_grid.copy()

        grid_size: tuple[int, int] = np_grid.shape
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                if np_grid[row][col] == "O":
                    out_idx = find_up_idx(up_grid[:, col], row)
                    up_grid[row][col] = "."
                    up_grid[out_idx][col] = "O"

        np_grid = np.rot90(up_grid, k=3)
    return np_grid


def puzzle(puzzle_input: list[str]) -> int:
    grid_input: list[list[str]] = []
    for i in range(len(puzzle_input)):
        grid_input.append(list(puzzle_input[i]))

    np_grid = np.array(grid_input)

    search_lst: list[str] = []
    cycle_dict: dict[str, int] = {}
    counter = 0

    cycle_counter = 0
    cycle_start = ""
    while True:
        np_grid = cycle(np_grid)
        grid_str: str = np_grid.tobytes().decode("utf-8")

        # apply until repeat
        if grid_str in search_lst:
            np_grid2 = cycle(np_grid)
            grid_str2: str = np_grid2.tobytes().decode("utf-8")

            # see if next also repeats
            if grid_str2 in search_lst:

                # start counting how big cycle is
                if cycle_counter == 0:
                    cycle_dict[grid_str] = get_score(np_grid)
                    cycle_start = grid_str
                    cycle_counter += 1

                # if counting is started
                else:
                    if cycle_start == grid_str:
                        break
                    cycle_counter += 1
                    cycle_dict[grid_str] = get_score(np_grid)

        else:
            if cycle_counter:
                cycle_counter += 1
            else:
                search_lst.append(grid_str)

        counter += 1

    # remove remove counter + 1, modulo cucle counter
    mod_val = (1000000000 - 1 - counter) % cycle_counter

    return list(cycle_dict.values())[mod_val]


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
        assert puzzle(puzzle_input_r) == 64

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
