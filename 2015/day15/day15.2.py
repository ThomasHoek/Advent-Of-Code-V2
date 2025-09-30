import os
import copy
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]


def parse_string(inp: list) -> list:
    lst = []
    for ingredient in inp:
        _, rest = ingredient.split(":")
        lst.append([int(x.split(" ")[-1]) for x in rest.split(",")])

    numpy_array = np.array(lst)
    transpose = numpy_array.T
    transpose_list = transpose.tolist()
    return transpose_list


# NEXCOM algoritm
def NEXCOM(N: int, K: int, R=[], MTC=False) -> list:
    """NEXCOM Next composition of n into K parts

    Algorithm defined by combinational algororithms.
    From: https://www2.math.upenn.edu/~wilf/website/CombAlgDownld.html
    page 51.

    Parameters
    ----------
    N : int
        Number whose compositions are desired
    K : int
        Number of parts of desired composition
    R : list
        R(i) is the Ith part of the output comopsition (I=1,K)
    MTC : bool
        True if this is not the last composition
        False if the current output is the last
    """
    R = [0] * K
    T = copy.deepcopy(N)
    H = 0

    while True:
        if MTC:  # Step through the array lowering left to right.
            if T > 1:
                H = -1
            H += 1
            T = R[H]  # H + 1?
            R[H] = 0
            R[0] = T - 1
            R[H + 1] += 1

        else:  # Set the array to N, 0, 0
            R[0] = copy.deepcopy(N)
            T = copy.deepcopy(N)
            H = 0
            if K != 1:
                for i in range(2, K):
                    R[i] = 0

        MTC = R[K - 1] != N
        yield R

        if not MTC:
            break


def mix_lists(ingredients, combinations):
    highest_num = float("inf") * -1
    for index, comb in enumerate(combinations):
        mult_comb = 1
        for ingredient in ingredients[:-1]:
            num = sum([x * y for x, y in zip(ingredient, comb)])
            mult_comb *= 0 if num < 0 else num

        cal = sum([x * y for x, y in zip(ingredients[-1], comb)])
        if mult_comb > highest_num and cal == 500:
            highest_num = copy.deepcopy(mult_comb)

    return highest_num


score = mix_lists(parse_string(puzzle_input), NEXCOM(100, len(puzzle_input)))
print(score)
