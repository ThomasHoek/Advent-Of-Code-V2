import re
from collections import Counter
from typing import Any


def ceasar_cipher(text: str, shift: int) -> str:
    new_str = ""
    for char in text:
        if char == "-":
            new_str += " "
        else:
            # calculate negative
            negative_shift = ord(char) - ord("a") + shift
            # wrap using 26 back to positive
            wrapped = negative_shift % 26
            # shift back to ascii
            shifted = wrapped + ord("a")

            new_str += chr(shifted)
    return new_str


def decode_room_name(match: re.Match[str]) -> str:
    shift = int(match.group("numbers"))
    decrypted_name = ceasar_cipher(match.group("encryption"), shift)
    if "northpole" in decrypted_name:
        return str(shift)
    return ""


def puzzle(puzzle_input: list[str]) -> Any:
    regexPattern = re.compile(pattern=r"(?P<encryption>[A-z-]*)(?P<numbers>[0-9]*)\[(?P<hash>.*)\]")

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
            if (response := decode_room_name(match)) != "":
                return response
    return -1
