from typing import Any


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
