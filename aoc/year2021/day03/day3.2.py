import numpy as np
import os

def puzzle(puzzle_input):
    puzzle_input = [list(map(int, str(x.rstrip()))) for x in puzzle_input]
    matrix = np.asarray(puzzle_input)
    opposite = {"0": "1", "1": "0"}


    def get_highest_bit_index(matrix, i: int, high_low: bool) -> bool:
        """Find if the highest bit of an index is 0 or 1.

        Args:
            matrix (np.array()): numpy Matrix
            i (int): index
            high_low (bool): Bool for highest or lowest value

        Returns:
            bool: highest found bit
        """
        bit = 1
        if sum(matrix[i]) < (0.5 * len(matrix[i])):
            # if less 1 then half of the row
            bit = 0

        if high_low:  # reverse it
            return int(opposite[str(bit)])
        return bit


    def rating_machine(matrix, high_low=0) -> bin:
        """binary number after doing a setup explained below

        Args:
            matrix (np.array()): numpy matrix
            high_low (bool, optional): Bool for highest or lowest. Defaults to 0.

        Returns:
            bin: binary number
        """

        index = 0
        while len(matrix) > 1:  # until a single number left
            newmatrix = []
            matrixmirror = matrix.T  # diagonal mirror
            bit = get_highest_bit_index(matrixmirror, index, high_low)

            for row in matrix:
                if row[index] == bit:
                    newmatrix.append(row)

            matrix = np.array(newmatrix)
            index += 1

        return "".join(str(x) for x in newmatrix[0])


    oxygen = int(rating_machine(matrix, 0), 2)
    co2 = int(rating_machine(matrix, 1), 2)
    return oxygen * co2
