def rotate(current: int, new: int, direction: str) -> int:
    if direction == "R":
        current += new
    elif direction == "L":
        current -= new
    else:
        raise NotImplementedError("Unknown Rotation")

    return current % 100


def puzzle(puzzle_input: list[str]) -> int:
    solution = 0
    rotation = 50
    for entry in puzzle_input:
        direction = entry[0]
        amount = int(entry[1:])

        rotation = rotate(rotation, amount, direction)
        if rotation == 0:
            solution += 1

    return solution
