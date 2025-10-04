import numpy as np


def t_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


direction_dict = {"D": (0, 1), "R": (1, 0), "U": (0, -1), "L": (-1, 0)}


def PolyArea(x: int, y: int):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def puzzle(puzzle_input: list[str]) -> int:
    # start: tuple[int, int, str] = (0, 0, "S")
    current: tuple[int, int] = (-3, -3)
    border_lst: list[tuple[int, int]] = [current]
    circum = 0

    for line in puzzle_input:
        dir, amount, rgb = line.split(" ")
        circum += int(amount)
        dir_tup = tuple([int(amount) * x for x in direction_dict[dir]])

        x, y = t_add(dir_tup, border_lst[-1])
        border_lst.append((x, y))

    area = PolyArea(*zip(*border_lst))

    total = area + circum / 2 + 1

    return int(total)
