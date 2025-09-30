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
        print(x, y)
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

    print(solution)
    return "".join(solution)


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
        final: bool = False
        file: bool = False
        clock: bool = False

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
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        assert puzzle(puzzle_input_r) == "5DB3"

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
