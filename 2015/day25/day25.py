from typing import Any
import numpy as np


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


def puzzle(start_num: int, x_loc: int, y_loc: int) -> int:

    arr_size: int = get_arr_size(x_loc, y_loc)
    # print(arr_size)
    lst = np.zeros(arr_size)  # type: ignore

    lst[0] = start_num
    for i in range(1, arr_size):
        lst[i] = lst[i - 1] * 252533 % 33554393

    return int(lst[-1])


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
        final: bool = False
        file: bool = False
        clock: bool = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open('out.txt', 'w')
        sys.stdout = f

    if clock:
        import time
        start: float = time.time()

    if final:
        puzzle_input: int = int(open(f"{dir_path}/input.txt", "r").readline())
        print(puzzle(puzzle_input, 2981, 3075))

    else:
        puzzle_input: int = int(open(f"{dir_path}/input.txt", "r").readline())
        # assert puzzle(puzzle_input, 1, 1) == 1
        # assert puzzle(puzzle_input, 2, 1) == 2
        # assert puzzle(puzzle_input, 1, 2) == 3
        # assert puzzle(puzzle_input, 2, 2) == 5
        # assert puzzle(puzzle_input, 6, 1) == 16
        # assert puzzle(puzzle_input, 1, 6) == 21
        # assert puzzle(puzzle_input, 2, 5) == 20
        # assert puzzle(puzzle_input, 5, 2) == 17

        assert puzzle(puzzle_input, 6, 6) == 27995004
        assert puzzle(puzzle_input, 1, 1) == 20151125
        assert puzzle(puzzle_input, 2, 1) == 31916031
        assert puzzle(puzzle_input, 1, 2) == 18749137
        assert puzzle(puzzle_input, 2, 2) == 21629792
        assert puzzle(puzzle_input, 6, 1) == 33071741
        assert puzzle(puzzle_input, 1, 6) == 33511524
        assert puzzle(puzzle_input, 6, 6) == 27995004

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
