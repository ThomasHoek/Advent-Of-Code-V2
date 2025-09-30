from typing import Any, Literal


def tuple_xy_add(
    rot: int, amount: int, loc: tuple[int, int]
) -> tuple[Literal[0, 1, 2, 3], tuple[int, int]]:
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
    for line in puzzle_input.split(", "):
        if line == "":
            continue

        rot = rot + 1 if line[0] == "L" else rot - 1
        rot, loc = tuple_xy_add(rot, amount=int(line[1:]), loc=loc)

    return sum(map(abs, loc))
