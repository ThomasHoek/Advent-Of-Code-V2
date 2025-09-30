#  ( -> go up one floor
#  ) -> go down one floor
#  infinite height


def puzzle(puzzle_input: str):
    up: int = puzzle_input.count("(")
    down: int = puzzle_input.count(")")
    return up - down
