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
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 2

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
