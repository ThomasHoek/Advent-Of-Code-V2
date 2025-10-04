import numpy as np



def chinese_remainder(remainder, mod_number, total):
    b = remainder
    ni = int(total / mod_number)

    xi = pow(ni, -1, mod_number)

    return b * ni * xi


def puzzle(input_file) -> int:
    _ = input_file[0]
    busses = input_file[1].rstrip().split(",")
        
    remainder_lst = []
    total = np.prod([int(i) if i != "x" else 1 for i in busses])
    counter = -1
    for number in busses:
        counter += 1
        if number != "x":
            remainder_lst.append(chinese_remainder(counter, int(number), total))

    return total - sum(remainder_lst) % total
