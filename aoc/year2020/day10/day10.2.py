from functools import reduce


def printTribRec(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1  # 0 should not be used
    else:
        return printTribRec(n - 1) + printTribRec(n - 2) + printTribRec(n - 3)


def puzzle(input_file) -> int:
    input_file = [int(word.rstrip()) for word in input_file]


    input_file.append(0)
    input_file.sort()

    repeat = [1]

    for i in range(len(input_file) - 1):
        diff = input_file[i + 1] - input_file[i]
        if diff == 1:
            repeat[-1] = repeat[-1] + 1
        else:
            repeat.append(1)


    repeat = [printTribRec(x + 2) for x in repeat if x != 0 and x != 1 and x != 2]
    return reduce((lambda x, y: x * y), repeat)
