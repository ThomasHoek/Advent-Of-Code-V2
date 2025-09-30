from typing import Any


def puzzle(puzzle_input: list[str]) -> Any:
    solution: list[str] = []
    x: int
    y: int
    x, y = 1, 1
    for line in puzzle_input:
        for letter in line:
            match letter:
                case "L":
                    x = max(0, x - 1)
                case "R":
                    x = min(2, x + 1)
                case "U":
                    y = max(0, y - 1)
                case "D":
                    y = min(2, y + 1)
                case _:
                    pass
        solution.append(str(3 * y + x + 1))

    return "".join(solution)
