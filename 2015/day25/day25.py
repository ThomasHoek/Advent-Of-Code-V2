import numpy as np
import re


def get_arr_size(x_loc: int, y_loc: int) -> int:
    loc = 1

    x_cur = 1
    if x_loc > 1:
        for add_x in range(1, x_loc):
            loc += add_x
            x_cur += 1

    if y_loc > 1:
        for add_y in range(1, y_loc):
            loc += x_cur + add_y

    return loc


def puzzle(puzzle_input) -> int:
    x_loc_str, y_loc_str = re.findall(r"row (\d+), column (\d+)", str(puzzle_input))[0]
    x_loc = int(x_loc_str)
    y_loc = int(y_loc_str)
    arr_size: int = get_arr_size(x_loc, y_loc)
    # print(arr_size)
    lst = np.zeros(arr_size)  # type: ignore

    lst[0] = 20151125
    for i in range(1, arr_size):
        lst[i] = lst[i - 1] * 252533 % 33554393

    return int(lst[-1])
