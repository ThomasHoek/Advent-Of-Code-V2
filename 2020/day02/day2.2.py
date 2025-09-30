# [Done] exited with code=0 in 0.049 seconds

input_file = open("input.txt", "r").readlines()
input_file = [word.rstrip().split(" ") for word in input_file]


def XNOR(a, b, c):
    return bool((a == c or b == c) and (a != b))


correct = 0
for lst in range(len(input_file)):
    minimaal, maximaal = list(map(int, input_file[lst][0].split("-")))
    letter = input_file[lst][1].replace(":", "")
    woord = input_file[lst][-1]

    if XNOR(woord[minimaal - 1], woord[maximaal - 1], letter):
        correct += 1

print(correct)
