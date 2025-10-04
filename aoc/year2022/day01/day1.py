import os

def puzzle(inputfile) -> int:
    """Return the highest total calories carried by an elf.

    inputfile: list of raw lines (strings) — like reading input.txt and keeping blank separators.
    """
    puzzle_input = [
        int(x.rstrip()) if x.rstrip().isdigit() else x.rstrip() for x in inputfile
    ]

    highest = 0
    elf_carry = 0
    for i in puzzle_input:
        if isinstance(i, str):
            highest = max(highest, elf_carry)
            elf_carry = 0
        else:
            elf_carry += i

    # remainder
    highest = max(highest, elf_carry)
    return highest
