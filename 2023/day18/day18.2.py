import numpy as np


def t_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


direction_dict = {"D": (0, 1), "R": (1, 0), "U": (0, -1), "L": (-1, 0)}
rgb_dict = {"0": "R", "1": "D", "2": "L", "3": "U"}


def PolyArea(x: int, y: int):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def puzzle(puzzle_input: list[str]) -> int:
    # start: tuple[int, int, str] = (0, 0, "S")
    current: tuple[int, int] = (-3, -3)
    border_lst: list[tuple[int, int]] = [current]
    circum = 0

    for line in puzzle_input:
        _, _, rgb = line.split(" ")
        rgb = rgb[2:-1]
        amount = int(rgb[:-1], 16)
        dir = rgb_dict[rgb[-1]]

        circum += int(amount)
        dir_tup = tuple([int(amount) * x for x in direction_dict[dir]])

        x, y = t_add(dir_tup, border_lst[-1])
        border_lst.append((x, y))

    area = PolyArea(*zip(*border_lst))

    total = area + circum / 2 + 1
    return int(total)


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
        assert puzzle(puzzle_input_r) == 952408144115

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
