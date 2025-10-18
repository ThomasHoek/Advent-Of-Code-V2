import hashlib


def to_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def puzzle(puzzle_input: str) -> str:
    puzzle_input = puzzle_input.strip()
    code = ""
    i = 0
    while len(code) != 8:
        hash = to_hash(f"{puzzle_input}{i}")
        if hash.startswith("00000"):
            code += hash[5]
        i += 1

    return code
