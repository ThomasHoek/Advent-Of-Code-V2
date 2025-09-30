# L = length
# W = Width
# H = Height
# Want to order EXACTLY as much as they need
# Find the surface: 2*l*w + 2*w*h + 2*h*l
# Question: Total square feet

def formula(length: int, width: int, height: int) -> int:
    """Calculate the square feet and added paper"""
    smallest = min(length * width, width * height, height * length)
    return 2 * length * width + 2 * width * height + 2 * height * length + smallest


def puzzle(puzzle_input: list[str]):
    total = 0
    for line in puzzle_input:
        length, width, height = map(int, line.split("x"))
        total += formula(length, width, height)
    return total
