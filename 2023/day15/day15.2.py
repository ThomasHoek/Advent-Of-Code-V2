from copy import deepcopy


def get_hash(inp_str: str) -> int:
    sub_total = 0
    for char in list(inp_str):
        sub_total += ord(char)
        sub_total *= 17
        sub_total = sub_total % 256
    return sub_total


class box_class:
    def __init__(self, number: int) -> None:
        self.boxnum = number
        self.items: list[str] = []
        self.numbers: list[int] = []

    def add(self, hashcode: str, num: int):
        if hashcode in self.items:
            hash_index = self.items.index(hashcode)
            self.numbers[hash_index] = num
        else:
            self.items.append(hashcode)
            self.numbers.append(num)

    def remove(self, hashcode: str):
        if hashcode in self.items:
            hash_index = self.items.index(hashcode)
            del self.items[hash_index]
            del self.numbers[hash_index]

    def score(self) -> int:
        total = 0
        for counter, i in enumerate(self.numbers, start=1):
            total += (self.boxnum + 1) * counter * i
        return total

    def __repr__(self) -> str:
        return " ".join("".join(str(x)) for x in zip(self.items, self.numbers))


def puzzle(puzzle_input: list[str]) -> int:
    assert len(puzzle_input) == 1

    box_dict: dict[int, box_class] = {}
    for i in range(256):
        box_dict[i] = deepcopy(box_class(i))

    hash_dict: dict[str, int] = {}
    for hash_code in puzzle_input[0].split(","):
        if "=" in hash_code:
            hash_str, num = hash_code.split("=")

            box_num = get_hash(hash_str)
            if hash_str not in hash_dict:
                hash_dict[hash_str] = box_num

            # add overlap check
            box_dict[int(box_num)].add(hash_str, int(num))

        else:
            hash_str = hash_code[:-1]
            if hash_str in hash_dict:
                box_num = hash_dict[hash_str]
                box_dict[int(box_num)].remove(hash_str)

    total = 0
    for i in range(256):
        total += box_dict[i].score()
    return total


if __name__ == "__main__":
    import sys
    import os
    from io import TextIOWrapper
    from typing import TextIO

    try:
        final: bool = "final" in sys.argv
        file: bool = "file" in sys.argv
        clock: bool = "time" in sys.argv

    except IndexError:
        final = False
        file = False
        clock = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    if file:
        orig_stdout: TextIO = sys.stdout
        f: TextIOWrapper = open("out.txt", "w")
        sys.stdout = f

    if clock:
        import time

        start: float = time.time()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[str] = [str(x.rstrip()) for x in puzzle_input]
        assert puzzle(puzzle_input_r) == 145

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
