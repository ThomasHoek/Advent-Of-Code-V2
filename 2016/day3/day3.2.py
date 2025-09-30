from typing import Any


def puzzle(puzzle_input: list[list[int]]) -> Any:
    solution: int = 0

    for triangle in puzzle_input:
        max_side: int = triangle.pop(triangle.index(max(triangle)))
        if max_side < sum(triangle):
            solution += 1

    return solution


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
        puzzle_input_r: list[list[int]] = []
        for _ in range(len(puzzle_input)):
            puzzle_input_r.append([])

        int_row: list[int]
        for counter, row in enumerate(puzzle_input):
            int_row = [int(i) for i in row.split()]
            three_step: int = (counter // 3) * 3
            puzzle_input_r[three_step].append(int_row[0])
            puzzle_input_r[three_step + 1].append(int_row[1])
            puzzle_input_r[three_step + 2].append(int_row[2])
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test2.txt", "r").readlines()
        puzzle_input_r: list[list[int]] = []
        for _ in range(len(puzzle_input)):
            puzzle_input_r.append([])

        int_row: list[int]
        for counter, row in enumerate(puzzle_input):
            int_row = [int(i) for i in row.split()]
            three_step: int = (counter // 3) * 3
            puzzle_input_r[three_step].append(int_row[0])
            puzzle_input_r[three_step + 1].append(int_row[1])
            puzzle_input_r[three_step + 2].append(int_row[2])
        assert puzzle(puzzle_input_r) == 6

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
