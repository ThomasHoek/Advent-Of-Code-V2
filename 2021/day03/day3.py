import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [list(map(int, str(x.rstrip()))) for x in puzzle_input]

matrix = np.asarray(puzzle_input)
matrixmirror = matrix.T
# diagonal mirror

new_number = ''
for i in range(len(matrixmirror)):
    if sum(matrixmirror[i]) > (0.5 * len(matrixmirror[i])):
        new_number += '1'
    else:
        new_number += '0'

gamma = int(new_number, 2)

opposite = {'0': '1', '1': '0'}
epsilon = int(''.join([opposite[c] for c in new_number]), 2)
print(gamma * epsilon)
