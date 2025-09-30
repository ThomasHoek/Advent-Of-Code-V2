from typing import Any


def puzzle(puzzle_input: list[str]) -> Any:
    
    puzzle_format_str = [x.split(" ") for x in puzzle_input]
    puzzle_format = [[int(y) for y in x if y != ""] for x in puzzle_format_str]

    solution: int = 0

    for triangle in puzzle_format:
        max_side: int = triangle.pop(triangle.index(max(triangle)))
        if max_side < sum(triangle):
            solution += 1

    return solution