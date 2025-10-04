#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height


def puzzle(puzzle_input: str):
    pos: int = 0
    count = 0
    for count, next_floor in enumerate(puzzle_input, start=1):
        if next_floor == "(":
            pos += 1
        else:
            pos -= 1

        if pos == -1:
            break

    return count
