from aoc.modules.grid_movement import Point2D, grid_helper

# ^: north
# v: south
# <: west
# >: east
# Question: how many atleast 1.

movement_dict: dict[str, Point2D] = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}


def puzzle(puzzle_input: str):
    unique_coords: set[Point2D] = set()
    loc: Point2D = (0, 0)
    unique_coords.add(loc)

    for command in puzzle_input:
        loc = grid_helper.move_by_key_custom(loc, command, direction_mapping=movement_dict)
        unique_coords.add(loc)

    return len(unique_coords)
