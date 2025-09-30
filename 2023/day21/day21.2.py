from typing import Any
import copy
import numpy as np


def to_file(mat):
    with open(f'{dir_path}/outfile.txt', 'a') as f:
        for line in mat:
            np.savetxt(f, line, fmt='%-7.2f')
        f.write("\n")
        

def get_neighbours(matrix: np.ndarray, x: int, y: int, max_x: int, max_y: int) -> list[tuple[int, int]]:
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
    clean_matrix[puzzle_input_list == "."] = 0

    clean_matrix2 = copy.deepcopy(clean_matrix)
    clean_matrix[puzzle_input_list == "S"] = 1
    clean_matrix2[puzzle_input_list == "s"] = 0

    row_tb = np.concatenate((clean_matrix2, clean_matrix2, clean_matrix2, clean_matrix2, clean_matrix2))
    row_m = np.concatenate((clean_matrix2, clean_matrix2, clean_matrix, clean_matrix2, clean_matrix2))
    big_matrix = np.concatenate((row_tb, row_tb, row_m, row_tb, row_tb), axis=1)

    np.set_printoptions(threshold=np.inf)

    max_x, max_y = big_matrix.shape
    for _ in range(count):
        update_matrix = copy.deepcopy(big_matrix)
        update_matrix[update_matrix == 1] = 0

        flip_set: set[tuple[int, int]] = set()
        # iterate
        for x in range(0, max_x):
            for y in range(0, max_y):
                if big_matrix[x, y] == 1:
                    neighbours: list[tuple[int, int]] = get_neighbours(big_matrix, x, y, max_x, max_y)
                    flip_set.update(neighbours)
        # add new
        for (i, j) in flip_set:
            update_matrix[i, j] = 1
        big_matrix = update_matrix
        print("PRINT")
        to_file(update_matrix)

    return 5
    # clean_matrix[np.isnan(clean_matrix)] = 0
    # return np.sum(np.concatenate(clean_matrix))


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
        assert puzzle(puzzle_input_r, 25)

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
