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
        assert puzzle(puzzle_input_r) == "1985"

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
