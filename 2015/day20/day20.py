from typing import Any
import numpy as np


def puzzle(puzzle_input: str) -> int:
    input: int = int(puzzle_input)

    # np array
    big_matrix: Any = np.zeros(int(input / 10))  # type: ignore
    for i in range(1, int(input / 10)):
        big_matrix[i - 1 :: i] += i * 10

    return np.where(big_matrix >= input)[0][0] + 1
