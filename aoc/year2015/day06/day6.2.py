# Solution can be done using numpy
import re

import numpy as np

from aoc.modules.text_parser import parse

type matrixT = np.ndarray

TOGGLE_PATTERN: re.Pattern[str] = re.compile(r"toggle (\d+),(\d+) through (\d+),(\d+)")
TURN_PATTERN: re.Pattern[str] = re.compile(r"turn (on|off) (\d+),(\d+) through (\d+),(\d+)")


# turn on 0,0 through 999,999
def turn(
    matrix: matrixT, command: str, start_x: int, start_y: int, end_x: int, end_y: int
) -> matrixT:
    region = matrix[start_x : end_x + 1, start_y : end_y + 1]
    if command == "on":
        region += 1
    else:
        np.maximum(region - 1, 0, out=region)
    return matrix


def toggle(matrix: matrixT, start_x: int, start_y: int, end_x: int, end_y: int):
    matrix[start_x : end_x + 1, start_y : end_y + 1] += 2
    return matrix


def puzzle(puzzle_input: list[str]):
    matrix = np.zeros((1000, 1000))

    for line in puzzle_input:
        if "toggle" in line:
            start_x, start_y, end_x, end_y = parse(TOGGLE_PATTERN, line)
            matrix = toggle(matrix, int(start_x), int(start_y), int(end_x), int(end_y))
        else:
            command, start_x, start_y, end_x, end_y = parse(TURN_PATTERN, line)
            matrix = turn(matrix, command, int(start_x), int(start_y), int(end_x), int(end_y))

    return matrix.sum()
