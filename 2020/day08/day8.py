# [Done] exited with code=0 in 0.216 seconds
input_file = open("input.txt", "r").readlines()

acc = 0
highest_line = 0
next_line = 0

previous_lines = []

while True:
    highest_line = next_line if next_line > highest_line else highest_line

    if next_line in previous_lines:
        break

    previous_lines.append(next_line)
    command, number = input_file[next_line].split(" ")

    if command == "acc":
        if "+" in number:
            acc += int(number.replace("+", ""))

        elif "-" in number:
            acc -= int(number.replace("-", ""))
        next_line += 1

    elif command == "jmp":
        if number == "-438":
            print("TEST")
            next_line += 1

        else:
            if "+" in number:
                next_line += int(number.replace("+", ""))

            elif "-" in number:
                next_line -= int(number.replace("-", ""))

    else:
        next_line += 1

print(acc)
