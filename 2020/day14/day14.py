inputfile = [i.rstrip() for i in open("input.txt", "r")]

mem_dict = {}


def get_binary(inp):
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string
    return "{0:b}".format(inp)


def binary_calc(imp, mask):
    new_binary = ""
    imp = "0" * (len(mask) - len(imp)) + imp
    for i in range(len(imp)):
        if mask[i] == "X":
            new_binary += imp[i]
        else:
            new_binary += mask[i]
    return int(new_binary, 2)


mask = 0
for line in inputfile:
    if "mask" in line:
        mask = line.split("=")[1]

    else:
        num, decimal = line.split("=")
        num = int(num[4:-2])
        binary = get_binary(int(decimal))

        mem_dict[num] = binary_calc(binary, mask)

print(sum(mem_dict.values()))
