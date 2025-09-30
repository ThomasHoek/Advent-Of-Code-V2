from typing import Any
import numpy as np
from operator import add
import re

max_size_r = 0
max_size_c = 0


def look_around(start: tuple[int, int],
                end: tuple[int, int]) -> tuple[tuple[int, int],
                                               tuple[int, int]]:
    start_r, start_c = start
    end_r, end_c = end
    assert start_r == end_r  # same row

    left_top = (start_r, start_c)
    right_bot = (end_r, end_c)

    # top row
    if start_r != 0:
        left_top = tuple(map(add, left_top, (-1, 0)))

    # bottom row
    if start_r != max_size_r:
        right_bot = tuple(map(add, right_bot, (1, 0)))

    # left side
    if start_c != 0:
        left_top = tuple(map(add, left_top, (0, -1)))

    # right side
    if start_c != max_size_c:
        right_bot = tuple(map(add, right_bot, (0, 1)))

    return left_top, right_bot


def puzzle(puzzle_input: Any) -> Any:
    global max_size_r
    global max_size_c

    total = 0

    max_size_r = len(puzzle_input)
    max_size_c = len(puzzle_input[0])
    seperated = [list(n) for n in puzzle_input]
    puzzle_arr = np.array(seperated, dtype=object)

    start_idx: tuple[int, int] = (0, 0)
    end_idx: tuple[int, int] = (0, 0)
    for r_index, row in enumerate(puzzle_input):
        digit_bool = False
        for s_index, symbol in enumerate(row):
            if symbol.isdigit() and not digit_bool:
                digit_bool = True
                start_idx = (r_index, s_index)

            elif digit_bool and (not symbol.isdigit() or (s_index + 1) == len(row)):
                digit_bool = False
                end_idx = (r_index, s_index)
                # find top and bottom
                topidx, bot_idx = look_around(start_idx, end_idx)

                # get digit
                if symbol.isdigit():
                    digit = int("".join(puzzle_arr[start_idx[0],
                                                   start_idx[1]: end_idx[1] + 1]))
                else:
                    digit = int("".join(puzzle_arr[start_idx[0],
                                                   start_idx[1]: end_idx[1]]))

                # slice in matrix'
                around_arr = puzzle_arr[
                    topidx[0]: bot_idx[0] + 1,
                    topidx[1]: bot_idx[1]
                ]

                # convert to string
                around_str = "".join(str(s) for s in around_arr.flatten())

                # use regex to remove . and numbers
                around_str = re.sub(r'\d|\.', '', around_str)

                if len(around_str):
                    total += digit
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
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 4361

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore

