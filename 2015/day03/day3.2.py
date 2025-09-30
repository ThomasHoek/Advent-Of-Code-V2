# ^: north
# v: south
# <: west
# >: east
# Question: how many atleast 1.
import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: str = open(f"{dir_path}/input.txt", "r").readline()


# location tuple: (North/south, east/west)
def new_location(direction: str, current_loc: tuple[int, int]) -> tuple[int, int]:
    """Get new location

    Args:
        direction (str): cardinal direction
        current_loc (tuple[int, int]): current location | xy datatype prob better

    Returns:
        tuple: new location
    """
    def add_tuple(tp1: tuple[int, int], tp2: tuple[int, int]) -> tuple[int, int]:
        return tuple(map(sum, zip(tp1, tp2)))

    return {
        '^': add_tuple(current_loc, (1, 0)),
        '>': add_tuple(current_loc, (0, 1)),
        'v': add_tuple(current_loc, (-1, 0)),
        '<': add_tuple(current_loc, (0, -1)),
    }[direction]


unique_coords_s1: set[tuple[int, int]] = set()
loc1: tuple[int, int] = (0, 0)
unique_coords_s1.add(loc1)

unique_coords_s2: set[tuple[int, int]] = set()
loc2: tuple[int, int] = (0, 0)
unique_coords_s2.add(loc2)

for count, command in enumerate(puzzle_input, 0):

    if count % 2 == 0:
        loc1 = new_location(command, loc1)
        unique_coords_s1.add(loc1)
    else:
        loc2 = new_location(command, loc2)
        unique_coords_s2.add(loc2)

print(len(set.union(unique_coords_s1, unique_coords_s2)))
