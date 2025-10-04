from typing import Any


def puzzle(puzzle_input: Any) -> Any:
    """
    decode_line decodes a line and returns which line to read next

    Args:
        str (str): input string
        a (int): current a
        b (int): current b


    Returns:
        tuple[int, int, int]: next line, a, b
    """
    str_amount: str
    amount: int
    jump_info: str
    register: str
    command: str
    other: str | int
    line_index = 0
    register_dict: dict[str, float] = {"a": 0, "b": 0}

    while True:
        # print("--------")
        # print(line_index, len(puzzle_input))
        # print(puzzle_input[line_index])

        if "," in puzzle_input[line_index]:
            jump_info, str_amount = puzzle_input[line_index].split(",")
            amount = (
                int(str_amount[1:]) if "+" in str_amount else -1 * int(str_amount[1:])
            )

            command, register = jump_info.split(" ")
            # print(command, register, amount)

            if "o" in command:
                if register_dict[register] == 1:
                    line_index += amount
                else:
                    line_index += 1

            elif "e" in command:
                if register_dict[register] % 2 == 0:
                    line_index += amount
                else:
                    line_index += 1
            else:
                # should never reach
                raise NotImplementedError

        else:
            command, other = puzzle_input[line_index].split(" ")
            # print(command, other)
            match command:
                case "hlf":
                    register_dict[other] /= 2
                    line_index += 1

                case "tpl":
                    register_dict[other] *= 3
                    line_index += 1

                case "inc":
                    register_dict[other] += 1
                    line_index += 1

                case "jmp":
                    line_index += int(other)

                case _:
                    # should not appear
                    raise NotImplementedError

        if line_index >= len(puzzle_input):
            break
        # print(register_dict)
    return register_dict
