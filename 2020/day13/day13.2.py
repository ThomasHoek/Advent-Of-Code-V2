import numpy as np

inputfile = open("input.txt", "r")
inputfile.readline()
busses = inputfile.readline().rstrip().split(",")


def chinese_remainder(remainder, mod_number, total):

    b = remainder
    ni = int(total / mod_number)

    xi = pow(ni, -1, mod_number)

    return b * ni * xi


remainder_lst = []
total = np.prod([int(i) if i != "x" else 1 for i in busses])
counter = -1
for number in busses:
    counter += 1
    if number != "x":

        remainder_lst.append(chinese_remainder(counter, int(number), total))


print(total - sum(remainder_lst) % total)
