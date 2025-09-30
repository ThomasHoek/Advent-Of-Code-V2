def hex_to_bit(hexstr: str) -> str:
    byte_hex = bytes.fromhex(hexstr)
    return byte_hex.decode("Latin-1")


def puzzle(puzzle_input: list[str]) -> int:
    total_length = 0
    total_string = 0

    for line in puzzle_input:
        total_length += len(line)
        index_pointer = 0

        line = line[1:-1]

        while True:
            index_pointer += line[index_pointer:].find("\\")
            backslash_com = line[index_pointer : index_pointer + 2]
            if backslash_com == "\\x":
                try:
                    substr = line[index_pointer + 2 : index_pointer + 4]
                    new_str = hex_to_bit(str(substr))
                    line = line.replace(line[index_pointer : index_pointer + 4], new_str, 1)
                except ValueError:
                    index_pointer += 1

            elif backslash_com == "\\\\":
                substr = line[index_pointer : index_pointer + 2]
                line = line.replace(substr, "\\", 1)

            elif backslash_com == '\\"':
                substr = line[index_pointer : index_pointer + 2]
                line = line.replace(substr, '"', 1)

            else:
                index_pointer += 1

            if line[index_pointer:].find("\\") == -1:
                break

            index_pointer += 1
        total_string += len(line)

    return total_length - total_string
