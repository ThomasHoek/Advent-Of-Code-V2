from typing import Any


def puzzle(puzzle_input: list[str]) -> Any:
    puzzle_format_str = [x.split(" ") for x in puzzle_input]
    puzzle_format = [[int(y) for y in x if y != ""] for x in puzzle_format_str]

    column_format: list[list[int]] = []
    for i in range(0, len(puzzle_format), 3):
        for j in range(3):
            column_format.append([
                puzzle_format[i][j],
                puzzle_format[i + 1][j],
                puzzle_format[i + 2][j]
                ])

    solution: int = 0

    for triangle in column_format:
        max_side: int = triangle.pop(triangle.index(max(triangle)))
        if max_side < sum(triangle):
            solution += 1

    return solution
