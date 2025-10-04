import numpy as np


direction_dict: dict[str, dict[str, list[str]]] = {
    "\\": {"N": ["W"], "E": ["S"], "S": ["E"], "W": ["N"]},
    r"/": {"N": ["E"], "E": ["N"], "S": ["W"], "W": ["S"]},
    r"|": {"N": ["N"], "E": ["N", "S"], "W": ["N", "S"], "S": ["S"]},
    r"-": {"N": ["W", "E"], "E": ["E"], "W": ["W"], "S": ["W", "E"]},
    r".": {"N": ["N"], "E": ["E"], "S": ["S"], "W": ["W"]},
}

direction_move: dict[str, tuple[int, int]] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}


def t_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


def puzzle(puzzle_input: list[str]) -> int:
    puzzle_matrix = np.array([list(x) for x in puzzle_input], ndmin=2)

    grid_size = puzzle_matrix.shape

    total = 0
    stored: list[tuple[int, int, str]]

    # cardinal direction
    for i in [0, 1, 2, 3]:
        # test range 0 to grid_max
        for j in range(0, grid_size[i % 2]):
            if i == 1:
                # east
                stored = [(j, 0, "E")]
            elif i == 2:
                # south
                stored = [(0, j, "S")]
            elif i == 3:
                # north
                stored = [(grid_size[i % 2] - 1, j, "N")]
            else:
                # west
                stored = [(j, grid_size[i % 2] - 1, "W")]

            visited: set[tuple[int, int, str]] = set()

            # if stored -> add all new directions
            for x, y, direction in stored:
                # border check
                if x >= grid_size[0] or x < 0:
                    continue
                if y >= grid_size[1] or y < 0:
                    continue

                self_val = puzzle_matrix[x][y]
                # if X, Y in same direction seen before -> skip.
                if (x, y, direction) in visited and self_val != ".":
                    continue

                new_dirs: list[str] = direction_dict[self_val][direction]
                visited.add((x, y, direction))

                for k in new_dirs:
                    new_plus: tuple[int, int] = direction_move[k]
                    n_x, n_y = t_add(new_plus, (x, y))
                    stored.append((n_x, n_y, k))

            coord_set = set((x, y) for x, y, _ in visited)
            total = max(len(coord_set), total)
    return total

