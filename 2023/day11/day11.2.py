import numpy as np


def get_dist(a: tuple[int, int], b: tuple[int, int],
             empty_idx: tuple[list[int], list[int]]) -> int:
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
            total += get_dist(coord_lst[first_idx], coord_lst[second_idx])
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
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))
        # assert puzzle(puzzle_input_r) == 374

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
