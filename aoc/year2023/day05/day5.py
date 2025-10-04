from typing import Any
import itertools
import re
from functools import partial


def split_list(lst: list[Any], val: Any) -> list[list[Any]]:
    """From Github and modified. -T"""
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


def list_to_tuple(lst: list[Any]) -> list[tuple[int, int, int]]:
    tuple_lst: list[tuple[int, int, int]] = []

    for x in lst:
        numbers: list[int] = re.findall(r"[0-9]+", x)
        if numbers != []:
            tuple_lst.append((int(numbers[0]), int(numbers[1]), int(numbers[2])))

    tuple_lst = sorted(tuple_lst, key=lambda tup: tup[1])
    return tuple_lst


def range_to_solution(boundaries: list[tuple[int, int, int]], number: int) -> int:
    for destination, source, add in boundaries:
        if number >= source and number < (source + add):
            return destination + (number - source)
    return number


def puzzle(puzzle_input: list[str]) -> Any:
    section_lst: list[list[Any]] = split_list(puzzle_input, "")

    seeds: list[int] = [int(x) for x in re.findall(r"[0-9]+", section_lst[0][0])]

    # Haskell inspred
    s2s = partial(range_to_solution, list_to_tuple(section_lst[1]))
    s2f = partial(range_to_solution, list_to_tuple(section_lst[2]))
    f2w = partial(range_to_solution, list_to_tuple(section_lst[3]))
    w2l = partial(range_to_solution, list_to_tuple(section_lst[4]))
    l2t = partial(range_to_solution, list_to_tuple(section_lst[5]))
    t2h = partial(range_to_solution, list_to_tuple(section_lst[6]))
    h2l = partial(range_to_solution, list_to_tuple(section_lst[7]))

    return min([h2l(t2h(l2t(w2l(f2w(s2f(s2s(x))))))) for x in seeds])
