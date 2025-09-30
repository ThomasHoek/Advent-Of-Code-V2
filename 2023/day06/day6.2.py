from typing import Any
import re
import math
from numpy import prod

def abc_formula(time: int, dist: int) -> tuple[float, float]:
    """
    abc_formula transform into ABC form

    x * (time - x) = dist
    -x^2 - x *time - dist = 0

    Args:
        time (int): B argument
        dist (int): C argument
    """
    a: int = 1
    b: int = -time
    c: float = dist + 0.0000000000001
    # add mini to prevent ints

    d: float = b**2 - 4 * a * c

    low: float = (-b - math.sqrt(d)) / (2 * a)
    up: float = (-b + math.sqrt(d)) / (2 * a)
    return low, up


def puzzle(puzzle_input: list[str]) -> Any:
    time_r, dist_r = (re.findall(r"[\d]+", x) for x in puzzle_input)
    time_int = int(''.join(time_r))
    dist_int = int(''.join(dist_r))

    low, high = abc_formula(time_int, dist_int)
    return math.ceil(high) - math.ceil(low)


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
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        # puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 71503

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
