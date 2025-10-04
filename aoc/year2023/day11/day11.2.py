import numpy as np


def get_dist(
    a: tuple[int, int], b: tuple[int, int], empty_idx: tuple[list[int], list[int]]
) -> int:
    """Manhattan distance"""
    expand = 1000000
    hor_expand = sum(
        [
            expand - 1 if i > min(a[0], b[0]) and i < max(a[0], b[0]) else 0
            for i in empty_idx[0]
        ]
    )
    horizontal = abs(a[0] - b[0]) + hor_expand

    ver_expand = sum(
        [
            expand - 1 if i > min(a[1], b[1]) and i < max(a[1], b[1]) else 0
            for i in empty_idx[1]
        ]
    )
    vertical = abs(a[1] - b[1]) + ver_expand
    return horizontal + vertical


def puzzle(puzzle_input: list[str]) -> int:
    np_puzzle = np.array([list(x) for x in puzzle_input])
    expanded_puzzle = np_puzzle.copy()

    # store empty rows, and math with them later
    empty_idx: tuple[list[int], list[int]] = ([], [])
    for i in range(2):
        for row_idx, row in enumerate(np_puzzle):
            if not any([x == "#" for x in row]):
                empty_idx[i].append(row_idx)

        np_puzzle = np_puzzle.T
        expanded_puzzle = expanded_puzzle.T

    # find all "#" and store the coordinate
    coord_lst: list[tuple[int, int]] = []
    row_len, col_len = expanded_puzzle.shape
    for row in range(row_len):
        for col in range(col_len):
            if expanded_puzzle[row][col] == "#":
                coord_lst.append((row, col))

    # iterate list and combine every point
    total = 0
    length_coords = len(coord_lst)
    for first_idx in range(length_coords):
        for second_idx in range(first_idx + 1, length_coords):
            total += get_dist(coord_lst[first_idx], coord_lst[second_idx], empty_idx)
    return total
