import numpy as np
import heapq
# import pandas as pd


class PriorityQueue(object):
    def __init__(self):
        self.heap: list[tuple[int, tuple[int, int, bool]]] = []
        self.set: set[tuple[int, int, bool]] = set()

    def add(self, d: tuple[int, int, bool], pri: int) -> None:
        if d not in self.set:
            heapq.heappush(self.heap, (pri, d))
            self.set.add(d)
        else:
            for counter, i in enumerate(self.heap):
                loop_prio, loop_d = i
                if loop_d == d:
                    self.heap.pop(counter)
                    heapq.heappush(self.heap, (min(loop_prio, pri), d))

    def pop(self) -> tuple[int, tuple[int, int, bool]]:
        pri, d = heapq.heappop(self.heap)
        self.set.remove(d)
        return pri, d

    def __repr__(self) -> str:
        return str(self.heap)

    def __len__(self):
        return len(self.heap)


def get_around(vertical: bool) -> list[tuple[int, int, bool]]:
    lst: list[tuple[int, int, bool]] = []
    for i in range(-3, 4):
        if i == 0:
            continue

        if vertical:
            lst.append((0, i, not vertical))
        else:
            lst.append((i, 0, not vertical))
    return lst


def t_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(sum, zip(a, b)))


def puzzle(puzzle_input: list[str]) -> int:
    puzzle_matrix = np.array([[int(x) for x in xs] for xs in puzzle_input], ndmin=2)
    grid_size = puzzle_matrix.shape

    value_matrix = puzzle_matrix.copy()
    value_matrix.fill(10000000)

    p_queue = PriorityQueue()
    p_queue.add((0, 0, True), 0)
    p_queue.add((0, 0, False), 0)

    visited_set: set[tuple[int, int, bool]] = set()
    while len(p_queue):
        num, info = p_queue.pop()
        results = get_around(info[-1])
        org_x, org_y, _ = info

        value_matrix[org_x][org_y] = min(num, value_matrix[org_x][org_y])
        visited_set.add(info)

        if org_x == (grid_size[0] - 1) and org_y == (grid_size[1] - 1):
            break

        for res in results:
            x, y = t_add(res[:2], info[:2])
            if x >= grid_size[0] or x < 0:
                continue
            if y >= grid_size[1] or y < 0:
                continue
            if (x, y, res[-1]) in visited_set:
                continue

            mat_res = 0
            if org_x == x:
                inter = org_y - y
                for i in range(0, abs(org_y - y)):
                    if inter > 0:
                        mat_res += puzzle_matrix[x][y + i]
                    else:
                        mat_res += puzzle_matrix[x][y - i]
            else:
                inter = org_x - x
                for i in range(0, abs(org_x - x)):
                    if inter > 0:
                        mat_res += puzzle_matrix[x + i][y]
                    else:
                        mat_res += puzzle_matrix[x - i][y]
            p_queue.add((x, y, res[-1]), mat_res + num)

    # df = pd.DataFrame(data=value_matrix.astype(float))
    # df.to_csv("outfile.csv", sep=",", header=False, float_format="%.2f", index=False)
    return value_matrix[grid_size[0] - 1][grid_size[1] - 1]


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
        assert puzzle(puzzle_input_r) == 102

    if clock:
        print("time: ", time.time() - start)  # type: ignore

    if file:
        sys.stdout = orig_stdout  # type: ignore
        f.close()  # type: ignore
