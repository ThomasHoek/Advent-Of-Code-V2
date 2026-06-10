def rotate(current: int, new: int, direction: str) -> tuple[int, int]:
    if direction == "R":
        new_current = current + new

        # right hand turns, no need to check for crossed from neg to pos
        total = new_current // 100
        total += new_current == 0

    elif direction == "L":
        new_current = current - new

        total = 0
        # crossed or landed on zero
        # left hand turn means it can cross without modulo notice
        if new_current == 0 or (current > 0 and new_current < 0):
            total += 1

        # count how often we loop. Do times -1 to prevent extra +1 with counting.
        # -110 // 100 = -2
        #  110 // 100 =  1
        if new_current < 0:
            total += (new_current * -1) // 100

    else:
        raise NotImplementedError("Unknown Rotation")

    return new_current % 100, total


def puzzle(puzzle_input: list[str]) -> int:
    solution = 0
    rotation = 50
    for entry in puzzle_input:
        direction = entry[0]
        amount = int(entry[1:])

        rotation, total = rotate(rotation, amount, direction)
        solution += total

    return solution
