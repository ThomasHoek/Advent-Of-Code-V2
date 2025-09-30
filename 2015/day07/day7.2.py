import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
store_dict = {}


def bit_not(n, numbits=16):
    return (1 << numbits) - 1 - n


while len(puzzle_input) > 0:
    for counter, line in enumerate(puzzle_input):
        try:
            line = line.rstrip()
            command, var = line.split(" -> ")
            if '44430' in line:
                command = '3176'

            if "AND" in command:
                com1, com2 = command.split(" AND ")
                if com1 == "1":
                    command = 1 & store_dict[com2]
                else:
                    command = store_dict[com1] & store_dict[com2]

            elif "OR" in command:
                com1, com2 = command.split(" OR ")
                command = store_dict[com1] | store_dict[com2]

            elif "LSHIFT" in command:
                com, amount = command.split(" LSHIFT ")
                command = store_dict[com] << int(amount)

            elif "RSHIFT" in command:
                com, amount = command.split(" RSHIFT ")
                command = store_dict[com] >> int(amount)

            elif "NOT" in command:
                com = command.split("NOT ")[1]
                command = bit_not(store_dict[com])

            try:
                int(command)
                store_dict[var] = int(command)
            except ValueError:
                store_dict[var] = store_dict[command]

            puzzle_input.pop(counter)

        except KeyError:
            pass

        except ValueError:
            pass

print(store_dict["a"])
