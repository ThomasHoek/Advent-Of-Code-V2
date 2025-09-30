from typing import Any
import numpy as np

input: int = 29000000

# np array
big_matrix: Any = np.zeros(int(input/10))  # type: ignore
for i in range(1, int(input/10)):
    big_matrix[i - 1::i] += i * 10

print(np.where(big_matrix >= input)[0][0] + 1)
