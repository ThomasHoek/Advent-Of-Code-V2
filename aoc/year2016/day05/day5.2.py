import hashlib


def to_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def puzzle(puzzle_input: str) -> str:
    puzzle_input = puzzle_input.strip()
    code = list("________")
    i = 0
    while "_" in code:
        hash = to_hash(f"{puzzle_input}{i}")
        if hash.startswith("00000"):
            position = hash[5]
            value = hash[6]

            if position in "01234567" and code[int(position)] == "_":
                code[int(position)] = value

        i += 1

    return ''.join(code)
