from typing import Any
from extra import print_final


def trace(inp_char: str) -> int:
    # if a diagonal trace crosses or not.
    match inp_char:
        case "S":
            return 0

        case "|":
            return 1

        case "-":
            return 1

        case "L":
            return 1

        case "J":
            return 0

        case "7":
            return 1

        case "F":
            return 0

        case ".":
            return 0

        case _:
            raise NotImplementedError("Error")


def move(inp_char: str) -> list[Any]:
    match inp_char:
        case "S":
            return [(1, 0, 1), (-1, 0, 1), (0, -1, 1), (0, 1, 1)]

        case "|":
            return [(1, 0, 1), (-1, 0, 1)]

        case "-":
            return [(0, 1, 1), (0, -1, 1)]

        case "L":
            return [(-1, 0, 1), (0, 1, 1)]

        case "J":
            return [(-1, 0, 1), (0, -1, 1)]

        case "7":
            return [(1, 0, 1), (0, -1, 1)]

        case "F":
            return [(1, 0, 1), (0, 1, 1)]

        case ".":
            return [(0, 0, 0)]

        case _:
            raise NotImplementedError("Error")


def puzzle(puzzle_input: list[str]) -> int:
    row_idx = 0
    col_idx = 0

    for row_idx, line in enumerate(puzzle_input):
        if "S" in line:
            col_idx = line.index("S")
            break
    start: tuple[int, int, int] = (row_idx, col_idx, 0)

    old_set: set[tuple[int, int]] = set()
    BFS_list = [start]
    All_BFS_list = [start]

    while len(BFS_list) != 0:
        current = BFS_list[0]
        old_set.add(current[:-1])

        for new in move(inp_char=puzzle_input[current[0]][current[1]]):
            res = tuple(map(sum, zip(new, current)))

            rebound = [x[:-1] for x in move(puzzle_input[res[0]][res[1]])]
            rebound_remap: list[tuple[Any | int, ...]] = [
                tuple(map(sum, zip(res, x))) for x in rebound
            ]

            if current[:-1] in rebound_remap:
                if res[:-1] not in old_set and res[0] >= 0 and res[1] >= 0:
                    old_set.add(res[:-1])
                    BFS_list.append(res)
                    All_BFS_list.append(res[:-1])
        BFS_list.pop(0)

    # diagonal ray trace
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    total = 0

    k = 0
    while k <= (width + height + 2):
        col = 0
        in_out = 0
        while col <= k:
            row = k - col
            if row < height and col < width:
                # diagonal trace

                if (row, col) in old_set:
                    in_out += trace(puzzle_input[row][col])
                elif in_out % 2:
                    total += 1
            col += 1
        k += 1

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
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 8

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
