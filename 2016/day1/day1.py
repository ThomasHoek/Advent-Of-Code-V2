from typing import Any, Literal


def tuple_xy_add(rot: int, amount: int, loc: tuple[int, int]) -> tuple[Literal[0, 1, 2, 3], tuple[int, int]]:
    if rot < 0:
        rot = 3
    rot = rot % 4

    match rot:
        case 0:
            loc = (loc[0] + amount, loc[1])
        case 1:
            loc = (loc[0], loc[1] + amount)
        case 2:
            loc = (loc[0] - amount, loc[1])
        case 3:
            loc = (loc[0], loc[1] - amount)
        case _:
            raise NotImplementedError

    return rot, loc


def puzzle(puzzle_input: Any) -> Any:
    loc: tuple[int, int] = (0, 0)

    rot: int = 0
    for line in puzzle_input:
        if line == '':
            continue

        rot = rot + 1 if line[0] == "L" else rot - 1
        rot, loc = tuple_xy_add(rot, amount=int(line[1:]), loc=loc)

    return sum(map(abs, loc))


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
        f: TextIOWrapper = open('out.txt', 'w')
        sys.stdout = f

    if clock:
        import time
        start: float = time.time()

    if final:
        puzzle_input: str = open(f"{dir_path}/input.txt", "r").readline()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input.split(", ")]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: str = open(f"{dir_path}/test.txt", "r").readline()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input.split(", ")]
        print(puzzle(puzzle_input_r))

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
