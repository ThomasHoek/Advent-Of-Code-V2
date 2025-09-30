# Solution can be done using numpy
import numpy as np

type matrixT = np.ndarray


# turn on 0,0 through 999,999
def turn(matrix: matrixT, command: str, start: tuple[int, int], end: tuple[int, int]):
    start_x, start_y = start
    end_x, end_y = end

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if command == "on":
                matrix[x][y] += 1
            else:
                matrix[x][y] = max(0, matrix[x][y] - 1)
    return matrix


def toggle(matrix: matrixT, start: tuple[int, int], end: tuple[int, int]):
    start_x, start_y = start
    end_x, end_y = end

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            matrix[x][y] += 2
    return matrix


def puzzle(puzzle_input: list[str]) -> int:
    matrix = np.zeros((1000, 1000))

    for line in puzzle_input:
        if "toggle" in line:
            line = line.replace("toggle ", "")
            start, end = line.split(" through ")
            start = tuple(map(int, start.split(",")))
            end = tuple(map(int, end.split(",")))
            matrix = toggle(matrix, start, end)

        else:
            line = line.replace("turn ", "")
            line = line.replace(" through ", " ")
            command, start, end = line.split(" ")
            start = tuple(map(int, start.split(",")))
            end = tuple(map(int, end.split(",")))
            matrix = turn(matrix, command, start, end)

    return matrix.sum()
