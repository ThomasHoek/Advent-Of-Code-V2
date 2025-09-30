from typing import Any, Literal


def tuple_xy_add(
    rot: int, amount: int, loc: tuple[int, int]
) -> tuple[Literal[0, 1, 2, 3], tuple[int, int], list[tuple[int, int]]]:
    if rot < 0:
        rot = 3
    rot = rot % 4

    between_list: list[tuple[int, int]] = []
    match rot:
        case 0:
            for i in range(amount):
                between_list.append((loc[0] + i, loc[1]))

            loc = (loc[0] + amount, loc[1])
        case 1:
            for i in range(amount):
                between_list.append((loc[0], loc[1] + i))
            loc = (loc[0], loc[1] + amount)
        case 2:
            for i in range(amount):
                between_list.append((loc[0] - i, loc[1]))
            loc = (loc[0] - amount, loc[1])
        case 3:
            for i in range(amount):
                between_list.append((loc[0], loc[1] - i))
            loc = (loc[0], loc[1] - amount)
        case _:
            raise NotImplementedError

    return rot, loc, between_list


def puzzle(puzzle_input: Any) -> Any:
    loc: tuple[int, int] = (0, 0)
    boolmap: dict[str, bool] = dict()
    between_list: list[tuple[int, int]] = []
    rot: int = 0
    
    for line in puzzle_input.split(", "):
        if line == "":
            continue

        rot = rot + 1 if line[0] == "L" else rot - 1
        rot, loc, between_list = tuple_xy_add(rot, amount=int(line[1:]), loc=loc)

        for between_loc in between_list:
            loc_str: str = "_".join(map(str, between_loc))
            if loc_str in boolmap:
                return sum(map(abs, between_loc))
            else:
                boolmap[loc_str] = True
