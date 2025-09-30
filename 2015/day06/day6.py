# Solution can be done using numpy
import numpy as np
import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()

matrix = np.zeros((1000, 1000))


# turn on 0,0 through 999,999
def turn(matrix, command: str, start: tuple, end: tuple):
    start_x, start_y = start
    end_x, end_y = end

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            matrix[x][y] = 1 if command == "on" else 0

    return matrix


def toggle(matrix, start: tuple, end: tuple):
    start_x, start_y = start
    end_x, end_y = end

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            matrix[x][y] = not matrix[x][y]
    return matrix


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
        turn(command, start, end)

print(matrix.sum())
