from typing import Any


def puzzle(puzzle_input: list[str]) -> Any:
    solution: list[str] = []
    x: int
    y: int
    x, y = 0, 2
    for line in puzzle_input:
        for letter in line:
            match letter:
                case "L":
                    if y == 0 or y == 4:
                        x = 2
                    elif y == 1 or y == 3:
                        x = max(1, x - 1)
                    else:
                        x = max(0, x - 1)
                case "R":
                    if y == 0 or y == 4:
                        x = 2
                    elif y == 1 or y == 3:
                        x = min(3, x + 1)
                    else:
                        x = min(4, x + 1)

                case "U":
                    if x == 0 or x == 4:
                        y = 2
                    elif x == 1 or x == 3:
                        y = max(1, y - 1)
                    else:
                        y = max(0, y - 1)
                case "D":
                    if x == 0 or x == 4:
                        y = 2
                    elif x == 1 or x == 3:
                        y = min(3, y + 1)
                    else:
                        y = min(4, y + 1)
                case _:
                    pass

        if y == 0:
            solution.append("1")
        if y == 1:
            solution.append(["2", "3", "4"][x - 1])
        if y == 2:
            solution.append(["5", "6", "7", "8", "9"][x])
        if y == 3:
            solution.append(["A", "B", "C"][x - 1])
        if y == 4:
            solution.append("D")

    return "".join(solution)
