from typing import Any
import copy
import numpy as np


def get_neighbours(matrix: np.ndarray[Any], x: int, y: int, max_x: int, max_y: int):
    return [
        (i, j)
        for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        if 0 <= i < max_x and 0 <= j < max_y and not np.isnan(matrix[i, j])
    ]


def puzzle(puzzle_input: list[str], count=64) -> int:
    puzzle_input_list = [list(row) for row in puzzle_input]
    puzzle_input_list = np.matrix(puzzle_input_list)

    # make matrix
    clean_matrix = np.zeros_like(puzzle_input_list, dtype=float)
    clean_matrix[puzzle_input_list == "#"] = np.nan
    border_matrix = copy.deepcopy(clean_matrix)

    clean_matrix[puzzle_input_list == "."] = 0
    clean_matrix[puzzle_input_list == "S"] = 1

    for _ in range(count):
        max_x, max_y = clean_matrix.shape
        update_matrix = copy.deepcopy(border_matrix)

        # iterate
        for x in range(0, max_x):
            for y in range(0, max_y):
                if clean_matrix[x, y] == 1:
                    neighbours = get_neighbours(clean_matrix, x, y, max_x, max_y)
                    if neighbours:
                        for i, j in neighbours:
                            update_matrix[i, j] = 1
        clean_matrix = update_matrix

    clean_matrix[np.isnan(clean_matrix)] = 0
    return np.sum(np.concatenate(clean_matrix))
