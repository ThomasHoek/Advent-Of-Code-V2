from typing import Any


def puzzle(puzzle_input: Any) -> Any:
    pass


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
        f: TextIOWrapper = open('out.txt', 'w')
        sys.stdout = f

    if clock:
        import time
        start: float = time.time()

    if final:
        puzzle_input: list[str] = open(f"{dir_path}/input.txt",
                                       "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        print(puzzle(puzzle_input_r))

    else:
        puzzle_input: list[str] = open(f"{dir_path}/test.txt", "r").readlines()
        # puzzle_input_r: list[str] = [x.rstrip() for x in puzzle_input]
        puzzle_input_r: list[int] = [int(x.rstrip()) for x in puzzle_input]
        puzzle(puzzle_input_r)
        # assert puzzle(puzzle_input_r) == NotImplemented

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
