# L = length
# W = Width
# H = Height
# Want to order EXACTLY as much as they need
# Find the surface: 2*l*w + 2*w*h + 2*h*l
# Question: Total square feet
import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: list[str] = open(f"{dir_path}/../input.txt", "r").readlines()


def formula(L: int, W: int, H: int) -> int:
    """Calculate the square feet and added paper

    Args:
        L (int): Length
        W (int): Width
        H (int): Height
    """
    lst: list[int] = [L, W, H]
    lst.sort()
    return lst[0] * 2 + lst[1] * 2 + L*W*H


total = 0
for line in puzzle_input:
    l, w, h = map(int, line.split("x"))
    total += formula(l, w, h)
print(total)
