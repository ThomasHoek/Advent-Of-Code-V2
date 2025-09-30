from typing import Any
import itertools
import re
from collections import defaultdict


class KeyDict(defaultdict):
    # https://stackoverflow.com/a/6229111
    def __missing__(self, key):
        return key


def split_list(lst: list[Any], val: Any) -> list[list[Any]]:
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


def list_to_dict(lst: list[Any]) -> dict[int, int]:
    hash_dict: dict[int, int] = KeyDict()

    for x in lst:
        numbers = re.findall(r"[0-9]+", x)
        if numbers != []:
            destination, source, add_num = [int(x) for x in numbers]
            for i in range(0, add_num):
                hash_dict[source + i] = destination + i

    return hash_dict


def puzzle(puzzle_input: list[str]) -> Any:
    section_lst = split_list(puzzle_input, "")

    seeds = [int(x) for x in re.findall(r"[0-9]+", section_lst[0][0])]
    s2s = list_to_dict(section_lst[1])
    s2f = list_to_dict(section_lst[2])
    f2w = list_to_dict(section_lst[3])
    w2l = list_to_dict(section_lst[4])
    l2t = list_to_dict(section_lst[5])
    t2h = list_to_dict(section_lst[6])
    h2l = list_to_dict(section_lst[7])

    return min([h2l[t2h[l2t[w2l[f2w[s2f[s2s[x]]]]]]] for x in seeds])


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
        assert puzzle(puzzle_input_r) == 35

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
