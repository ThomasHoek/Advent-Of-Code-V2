import re
from collections import Counter
from typing import Any


def puzzle(puzzle_input: list[str]) -> Any:
    regexPattern = re.compile(pattern=r"(?P<encryption>[A-z-]*)(?P<numbers>[0-9]*)\[(?P<hash>.*)\]")

    correct_total = 0
    for room_code in puzzle_input:
        match = regexPattern.match(room_code)
        if match is None:
            assert False, f"Regex failed to match on input: {room_code}"

        encryption: str = match.group("encryption")
        encryption = encryption.replace("-", "")

        hash_str: str = match.group("hash")

        letter_count = Counter(encryption).items()

        # sorts on the counter first, breaks tie breakers with unicode value of letter
        sorted_count = sorted(letter_count, key=lambda x: (-x[1], x[0]))

        common_hash = "".join([first for (first, _) in sorted_count[:5]])
        if common_hash == hash_str:
            correct_total += int(match.group("numbers"))

    return correct_total
