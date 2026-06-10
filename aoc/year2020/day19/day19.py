import re


def has_numbers(inputString: str) -> bool:
    return any(char.isdigit() for char in inputString)


def find_all_terminal_keys(node_dict: dict[str, str]) -> list[tuple[str, str]]:
    return [(k, v) for k, v in node_dict.items() if not has_numbers(v)]


def handle_validated(validate_list: list[str]) -> list[str]:

    replace_dict: dict[str, str] = {}
    for line in validate_list:
        key, value = line.split(": ")
        replace_dict[key] = " " + value.strip().replace(" ", "  ") + " "

    while len(replace_dict.keys()) != 1:
        terminal_nodes = find_all_terminal_keys(replace_dict)
        for replace_key, replace_value in terminal_nodes:
            del replace_dict[str(replace_key)]
            for k, v in replace_dict.items():
                if replace_value.startswith(' "'):
                    replace_dict[k] = v.replace(
                        f" {replace_key} ", f" {replace_value.replace('"', '')} "
                    )
                else:
                    replace_dict[k] = v.replace(f" {replace_key} ", f" (?:{replace_value}) ")
    solution = replace_dict["0"]
    solution = solution.replace(" ", "")

    return solution


def puzzle(puzzle_input: list[str]) -> int:

    seperator = next(c for c, line in enumerate(puzzle_input) if line == "")
    validated = puzzle_input[:seperator]
    messages = puzzle_input[seperator + 1 :]

    validatedRegex = handle_validated(validated)
    print(validatedRegex)
    valRegex = re.compile(pattern=f"^{validatedRegex}$")

    count = 0
    for m in messages:
        if valRegex.findall(m):
            count += 1

    print(count)


# 478
# That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. [Return to Day 19]
