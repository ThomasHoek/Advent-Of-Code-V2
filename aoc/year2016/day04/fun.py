import re
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
    return decrypted_name.strip()


def puzzle(puzzle_input: list[str]) -> Any:
    regexPattern = re.compile(pattern=r"(?P<encryption>[A-z-]*)(?P<numbers>[0-9]*)\[(?P<hash>.*)\]")

    decoded_list: list[str] = []
    for room_code in puzzle_input:
        match = regexPattern.match(room_code)
        if match is None:
            assert False, f"Regex failed to match on input: {room_code}"
        decoded_list.append(decode_room_name(match))

    with open("aoc/year2016/day04/full_decode.txt", "w+") as f:
        for item in decoded_list:
            f.write(f"{item}\n")
    return 'Success'


if __name__ == "__main__":
    with open("aoc/year2016/day04/input.txt") as f:
        puzzle_input = [line.strip() for line in f.readlines()]
    print(puzzle(puzzle_input))
