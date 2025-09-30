from __future__ import annotations
from typing import Any, Generator
import itertools
from copy import deepcopy


def split_list(lst: list[Any], val: Any) -> list[list[Any]]:
    """From Github and modified. -T"""
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


letterdict: dict[str, int] = {"x": 0, "m": 1, "a": 2, "s": 3}


def workflow_solve(wf_dict: dict[str, str], inp_str: str,
                   info: list[list[int]]) -> Generator[list[list[int]], None, None]:
    if inp_str == "A":
        yield info
        return
    elif inp_str == "R":
        return

    current = wf_dict[inp_str]
    for line in current.split(","):
        if ":" in line:
            equation, final = line.split(":")
            if ">" in equation:
                letter, number_str = equation.split(">")
                number = int(number_str)
                letter_num = letterdict[letter]
                min_info, max_info = info[letter_num]

                # if True
                # [0, 4000] ->  > 2000 -> [2001 , 4000]
                # [3000, 4000] ->  > 2000 -> | True but keep 3000.
                # [0, 1000] ->  > 2000 -> nothing | max under
                if max_info > number:
                    info_c = deepcopy(info)
                    info_c[letter_num] = [max(min_info, number + 1), max_info]
                    yield from workflow_solve(wf_dict, final, info_c)

                # add reverse.
                # [0, 4000] ->  NOT > 2000 -> [0 , 2001]
                # [3000, 4000] ->  NOT  > 2000 | impossible.
                # [0, 1000] ->  NOT  > 2000 keep 1000. [0, 1000]
                info[letter_num] = [min_info, min(max_info, number)]

            else:
                letter, number_str = equation.split("<")
                number = int(number_str)
                letter_num = letterdict[letter]
                min_info, max_info = info[letter_num]

                # if True
                # [0, 4000] ->  < 2000 -> [0 , 1999]
                # [3000, 4000] ->  < 2000 -> |nothing keep 3000
                # [0, 1000] ->  < 2000 -> nothing | keep 1000
                if max_info > number:
                    info_c = deepcopy(info)
                    info_c[letter_num] = [min_info, min(max_info, number - 1)]
                    yield from workflow_solve(wf_dict, final, info_c)

                # add reverse.
                # [0, 4000] ->  NOT < 2000 -> [2000, 4000]
                # [3000, 4000] ->  NOT < 2000 |
                # [0, 1000] ->  NOT < 2000 | impossible.
                info[letter_num] = [max(min_info, number), max_info]

        else:
            yield from workflow_solve(wf_dict, line, info)
    return


def puzzle(puzzle_input: list[str]) -> int:
    workflow, _ = split_list(puzzle_input, "")
    workflow_dict: dict[str, str] = {}
    for line in workflow:
        name, split_str = line[:-1].split(r"{")
        workflow_dict[name] = split_str

    total = 0
    info: list[list[int]] = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    for range_lst in workflow_solve(workflow_dict, "in", info):
        subtotal = 1
        for min_range, max_range in range_lst:
            subtotal *= int(max_range) - int(min_range) + 1
        total += subtotal

    return total


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
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 167409079868000

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
