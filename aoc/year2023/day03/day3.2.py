from typing import Any
import numpy as np
from operator import add


max_size_r: int = 0
max_size_c: int = 0


def look_around(
    start: tuple[int, int], end: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    start_r, start_c = start
    end_r, end_c = end
    assert start_r == end_r  # same row

    left_top: tuple[int, int] = (start_r, start_c)
    right_bot: tuple[int, int] = (end_r, end_c)

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


def find_digit(row: list[int], index: int) -> int:
    digit_lst: list[str] = []

    # get numbers before and after index
    before: list[str] = list(np.flip(row)[len(row) - index :])
    after: list[str] = list(row[index:])

    # pop and add while it's digit
    while after[0].isdigit():
        digit_lst.append(after[0])
        after.pop(0)
        if after == []:
            break

    # reverse because list is inversed
    digit_lst.reverse()

    # pop and add while it's digit
    while before[0].isdigit():
        digit_lst.append(before[0])
        before.pop(0)
        if before == []:
            break

    # reverse to get normal num
    digit_lst.reverse()

    return int("".join(digit_lst))


def puzzle(puzzle_input: list[str]) -> Any:
    global max_size_r
    global max_size_c

    total = 0

    max_size_r = len(puzzle_input)
    max_size_c = len(puzzle_input[0])
    seperated: list[list[str]] = [list(n) for n in puzzle_input]

    # array used for slicing
    puzzle_arr = np.array(seperated, dtype=object)

    for r_index, row in enumerate(puzzle_input):
        for s_index, symbol in enumerate(row):
            if symbol == "*":
                # find top and bottom
                coord: tuple[int, int] = (r_index, s_index)

                # same coord for start and end, dumb but works.
                topidx, bot_idx = look_around(coord, coord)

                # slice in matrix
                around_arr = puzzle_arr[
                    topidx[0] : bot_idx[0] + 1, topidx[1] : bot_idx[1] + 1
                ]

                # potential bug: double digit
                # trying without
                digits_set: set[int] = set()

                # walk around matrix
                for iy, ix in np.ndindex(around_arr.shape):
                    # if digit found -> find full digit with sliding window.
                    if around_arr[iy, ix].isdigit():
                        digit = find_digit(
                            puzzle_arr[r_index + (iy - 1)], int(s_index + (ix - 1))
                        )

                        digits_set.add(digit)

                # final check of length
                if len(digits_set) == 2:
                    total += np.prod(list(digits_set))

    return total
