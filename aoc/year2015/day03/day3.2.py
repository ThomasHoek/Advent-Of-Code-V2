from aoc.modules.grid_movement import Point2D, grid_helper

# ^: north
# v: south
# <: west
# >: east
# Question: how many atleast 1.

movement_dict: dict[str, Point2D] = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}


def puzzle(puzzle_input: str):
    unique_coords_s1: set[Point2D] = set()
    loc1: Point2D = (0, 0)
    unique_coords_s1.add(loc1)

    unique_coords_s2: set[Point2D] = set()
    loc2: Point2D = (0, 0)
    unique_coords_s2.add(loc2)

    for count, command in enumerate(puzzle_input, 0):
        if count % 2 == 0:
            loc1 = grid_helper.move_by_key_custom(loc1, command, movement_dict)
            unique_coords_s1.add(loc1)
        else:
            loc2 = grid_helper.move_by_key_custom(loc2, command, movement_dict)
            unique_coords_s2.add(loc2)

    return len(unique_coords_s1.union(unique_coords_s2))
