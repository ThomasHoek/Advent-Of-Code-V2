import numpy as np


def get_dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Manhattan distanc"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def puzzle(puzzle_input: list[str]) -> int:
    np_puzzle = np.array([list(x) for x in puzzle_input])
    expanded_puzzle = np_puzzle.copy()

    # add rows, transpose, add cols, transpose back to org
    for _ in range(2):
        add_num = 0
        for row_idx, row in enumerate(np_puzzle):
            if not any([x == "#" for x in row]):
                new_row = row_idx + add_num
                expanded_puzzle = np.insert(
                    expanded_puzzle, new_row, expanded_puzzle[new_row], axis=0
                )
                add_num += 1

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
            total += get_dist(coord_lst[first_idx], coord_lst[second_idx])

    return total
