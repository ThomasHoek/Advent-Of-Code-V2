import os

dir_path: str = os.path.dirname(os.path.realpath(__file__))
puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()


def double_double_string(inp: str) -> bool:
    while len(inp) > 3:
        if inp.count(inp[len(inp) - 2:]) >= 2:
            return True
        inp = inp[:-1]
    return False


def check_double_letter(inp: str) -> bool:
    for i in range(len(inp) - 2):
        if inp[i] == inp[i+2]:
            return True
    return False


nice = 0
naughty = 0
for line in puzzle_input:
    if double_double_string(line) and check_double_letter(line):
        nice += 1
    else:
        naughty += 1
print(nice, naughty)
