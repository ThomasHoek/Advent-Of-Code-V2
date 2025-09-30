# [Done] exited with code=0 in 0.248 seconds

input_file = open("input.txt", "r").readlines()
acc = 0
next_line = 0


def function_game_console(next_line=0, acc=0):

    previous_lines = []
    jmp_nop_numbers = []

    while next_line != len(input_file):
        if next_line in previous_lines:
            return jmp_nop_numbers

        previous_lines.append(next_line)
        command, number = input_file[next_line].rstrip().split(" ")

        if command == "acc":
            if "+" in number:
                acc += int(number.replace("+", ""))

            elif "-" in number:
                acc -= int(number.replace("-", ""))

            next_line += 1

        elif command == "jmp":
            jmp_nop_numbers.append([next_line, acc])
            if "+" in number:
                next_line += int(number.replace("+", ""))

            elif "-" in number:
                next_line -= int(number.replace("-", ""))

        elif command == "nop":
            jmp_nop_numbers.append([next_line, acc])
            next_line += 1

        else:
            pass

    return acc


wrong_lst = function_game_console()

for line in wrong_lst:
    command, number = input_file[line[0]].rstrip().split(" ")
    if command == "jmp":  # simple skip
        awnsers = function_game_console(next_line=line[0] + 1, acc=line[1])

    elif command == "nop":  # act as if its a jmp
        if "+" in number:
            awnsers = function_game_console(
                next_line=line[0] + int(number.replace("+", "")), acc=line[1]
            )

        elif "-" in number:
            awnsers = function_game_console(
                next_line=line[0] - int(number.replace("-", "")), acc=line[1]
            )

    if type(awnsers) == int:
        print(input_file[line[0]], awnsers)
