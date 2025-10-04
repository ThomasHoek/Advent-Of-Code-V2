import os

def puzzle(puzzle_input_r) -> int:
    puzzle_input: list[int | str] = [
        int(x.rstrip()) if x.rstrip().isdigit() else x.rstrip() for x in puzzle_input_r
    ]

    highest = [0, 0, 0]
    elf_carry: int = 0
    for i in puzzle_input:
        if isinstance(i, str):
            if highest[0] < elf_carry:
                highest = highest[1:] + [elf_carry]
                highest.sort()
            elf_carry = 0
        else:
            elf_carry += i

    # remainder
    if highest[0] < elf_carry:
        highest = highest[1:] + [elf_carry]

    return sum(highest)
