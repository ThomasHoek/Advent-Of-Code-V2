from typing import Any
import math
import numpy as np

# lowest N ever found, test but couldn't get to work
min_n: float = float("inf")


# TODO: it would be better to implement the triple check instead of the bool check.
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
    fourth_sum = int(sum(puzzle_input_int) / 4)
    new_set_4: set[tuple[int]] = get_all_perms(subset=puzzle_input_int, target=fourth_sum)

    # get shortest only
    short_lst_4: list[list[int]] = list()
    max_len_4: int = len(min(new_set_4, key=len))
    for val in new_set_4:
        if len(val) == max_len_4:
            short_lst_4.append(list(val))

    # sort by QE
    sort_lst_4: list[list[int]] = sorted(short_lst_4, key=lambda x: math.prod(x))
    # for highest QE 4
    for i_4 in sort_lst_4:
        remainder_4: list[int] = [x for x in puzzle_input_int if x not in i_4]

        new_set_3: set[tuple[int]] = get_all_perms(
            subset=remainder_4, target=fourth_sum
        )

        # get shortest only
        sort_lst_3: list[list[int]] = list()
        max_len_3: int = len(min(new_set_3, key=len))
        for val in new_set_3:
            if len(val) == max_len_3:
                sort_lst_3.append(list(val))

        # for highest QE 3
        for i_3 in sort_lst_3:
            remainder_3: list[int] = [x for x in puzzle_input_int if x not in i_3]
            if check_group_sum(remainder_3, len(remainder_3), fourth_sum):
                return math.prod(i_4)

