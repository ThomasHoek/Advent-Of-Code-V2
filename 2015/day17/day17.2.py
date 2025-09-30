import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]


# Sum of Subsets by backtracking.
def SumOfSub(s=0, k=0, r=0, x=[]):
    """SumOfSub Give all sum [k] of Sub

    Find all subsets that sum to m

    Parameters
    ----------
    s : int, optional
        sum of numbers selected now, by default 0
    k : int, optional
        Choice of number K to be made, by default 1
    r : list, optional
        sum of numbers that are remaining, by default []
    """
    global m
    global w

    x[k] = 1
    if (s + w[k]) == m:
        yield x[0:k+1]

    elif (s + w[k] + w[k+1]) <= m:
        yield from SumOfSub(s + w[k], k + 1, r - w[k], x)

    if ((s + r - w[k]) >= m and (s + w[k + 1]) <= m):
        x[k] = 0
        yield from SumOfSub(s, k+1, r - w[k], x)


m = 150
w = [int(x) for x in puzzle_input]
w.sort()
x = [0] * len(w)

dict_sum = {}
counter = 0
for i in SumOfSub(r=sum(w), x=x):
    try:
        dict_sum[sum(i)] += 1
    except KeyError:
        dict_sum[sum(i)] = 1
    counter += 1

print(dict_sum[min(dict_sum.keys())])
