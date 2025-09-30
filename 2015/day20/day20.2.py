import numpy as np


input: int = 29000000

big_matrix = np.zeros(int(input/10))  # type: ignore
for i in range(1, int(input/10)):
    big_matrix[i - 1:i*50:i] += i * 11


print(np.where(big_matrix >= input)[0] + 1)
