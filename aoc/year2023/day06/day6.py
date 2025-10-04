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
    time_int = tuple(map(int, time_r))
    dist_int = tuple(map(int, dist_r))
    time_dist = list(zip(time_int, dist_int))

    total: list[int] = []
    for time, dist in time_dist:
        low, high = abc_formula(time, dist)
        total.append(math.ceil(high) - math.ceil(low))

    return prod(total)
