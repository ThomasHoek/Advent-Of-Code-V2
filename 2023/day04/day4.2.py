from typing import Any
import re
from collections import defaultdict


def puzzle(puzzle_input: Any) -> Any:
    counter_dict = defaultdict(int = 1)
    counter_dict[1] = 1
    counter_dict.default_factory = lambda: 1

    re_filter = re.compile(r"([\d| ]+) \| ([\d| ]+)")

    for number, line in enumerate(puzzle_input, start=1):

        tuple_groups = re_filter.search(line).groups()
        win_num, self_num = (set([int(x) for x in re.split(r'\s+', xs) if x]) for xs in tuple_groups)

        amount = len(win_num.intersection(self_num))
        if amount != 0:
            for i in range(number + 1, number + amount + 1):
                counter_dict[i] += 1 * counter_dict[number]
        else:
            # create if not already exist
            counter_dict[number]

    return sum(counter_dict.values()) - 1


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
        assert puzzle(puzzle_input_r) == 30

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
