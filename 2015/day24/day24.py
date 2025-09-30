from typing import Any
import math
import numpy as np

# lowest N ever found, test but couldn't get to work
min_n: float = float("inf")


def check_group_sum(set: list[int], n: int, sum: int) -> bool:
    subset: np.ndarray = np.zeros((n + 1, sum + 1))  # type: ignore

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = 1

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]
            if j >= set[i - 1]:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - set[i - 1]]

    return subset[n][sum]


def get_all_perms(
    subset: list[int],
    target: int,
    perm_set: set[tuple[int]] = set(),
    partial: list[int] = [],
    partial_sum: int = 0,
) -> set[tuple[int]]:
    """
    get_perms Gets all the permutations of an input list

    Uses recursion to generate the powerset, which gets checked against the target condition

    Args:
        subset (list[int]): The initial input list
        target (int): Target integer you want the permutations to match
        perm_set (set[tuple[int]], optional): set of every found permutation. Defaults to set().
        partial (list[int], optional): helper variable, keeps track of leftovers. Defaults to [].
        partial_sum (int, optional): helper variable, keeps track of sum leftover. Defaults to 0.

    Returns:
        set[tuple[int]]: Set of every possible found permutation
    """

    # if equal
    if partial_sum == target:
        perm_set.add(tuple(partial))
        return perm_set

    # smaller than 0, a b c
    if partial_sum >= target:
        return perm_set

    # generate powerset
    for i in range(len(subset)):
        # go to next number [skip numbers]
        subset_n: int = subset[i]

        # slice to get sub list
        remaining: list[int] = subset[i + 1 :]

        # recursive call with sublist and shorter input
        perm_set = get_all_perms(
            subset=remaining,
            target=target,
            perm_set=perm_set,
            partial=partial + [subset_n],
            partial_sum=partial_sum + subset_n,
        )
    return perm_set


def puzzle(puzzle_input: list[int]) -> Any:
    puzzle_input_int: list[int] = [int(p) for p in puzzle_input]

    if len(puzzle_input_int) < 3:
        raise AttributeError

    if sum(puzzle_input_int) % 3 == 0:
        puzzle_input_int.reverse()

        third_sum = int(sum(puzzle_input_int) / 3)
        new_set: set[tuple[int]] = get_all_perms(subset=puzzle_input_int, target=third_sum)

        # get shortest only
        short_lst: list[list[int]] = list()
        max_len: int = len(min(new_set, key=len))
        for val in new_set:
            if len(val) == max_len:
                short_lst.append(list(val))

        # sort by QE
        sort_lst: list[list[int]] = sorted(short_lst, key=lambda x: math.prod(x))
        # for highest QE
        for i in sort_lst:
            remainder: list[int] = [x for x in puzzle_input_int if x not in i]
            if check_group_sum(remainder, len(remainder), third_sum):
                return math.prod(i)
