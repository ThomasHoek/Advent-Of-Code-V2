from aoc.modules.graph_helper import Graph

STRINT = str | int


def tryInt(x: str) -> STRINT:
    """Try to convert to an INT"""
    try:
        return int(x)
    except ValueError:
        return x


def parse_instructions(line: str) -> tuple[str, str, tuple[STRINT, ...]]:
    """Tries to parse the puzzle input into a tuple of:
    (COMMAND, TARGET KEY, (CHILDREN KEYS))
    """
    commands, target_exp = line.split(" -> ")
    command_list = commands.split(" ")
    command_amount = len(command_list)

    if command_amount == 1:
        exp_command: str = "SET"
    elif command_amount == 2:
        exp_command = command_list.pop(0)
    elif command_amount == 3:
        exp_command = command_list.pop(1)
    else:
        raise ValueError("Extra amount of values found")

    childTuple: tuple[STRINT, ...] = tuple(tryInt(x) for x in command_list)
    return (exp_command, target_exp, childTuple)


def build_graph(
    puzzle_input: list[str],
) -> tuple[Graph[str], dict[str, tuple[str, tuple[STRINT, ...]]]]:
    """Makes a DAG graph, which can be used for a topological sort to find the dependencies.
    Uses a side table with operations for solving up to target.

    Operations: (Target Node, (COMMAND, (CHILD VALUES)))"""
    graph = Graph[str]()
    operations: dict[str, tuple[str, tuple[STRINT, ...]]] = {}

    for line in puzzle_input:
        parsed_line = parse_instructions(line)

        # build the graph
        target_node = parsed_line[1]
        for dependency_node in parsed_line[2]:
            if isinstance(dependency_node, str):
                graph.add_edge(dependency_node, target_node)

        operations[target_node] = (parsed_line[0], parsed_line[2])

    return graph, operations


def apply_operation(operation: str, child_values: list[int]) -> int:
    """Apply one operation"""
    match operation:
        case "SET":
            return child_values[0]
        case "NOT":
            return (1 << 16) - 1 - child_values[0]
        case "AND":
            return child_values[0] & child_values[1]
        case "OR":
            return child_values[0] | child_values[1]
        case "LSHIFT":
            return child_values[0] << child_values[1]
        case "RSHIFT":
            return child_values[0] >> child_values[1]
        case _:
            raise ValueError(f"Unknown operation found: {operation}")


def evaluate(
    graph: Graph[str],
    operations: dict[str, tuple[str, tuple[STRINT, ...]]],
    target: str,
) -> dict[str, int]:
    """Evaluate the wires needed for target using a dependency graph."""
    values: dict[str, int] = {}

    def value_if_string(value: STRINT) -> int:
        if isinstance(value, str):
            return values[value]
        return value

    dependency_list = graph.dependency_order(target)

    for next_to_solve_wire in dependency_list:
        operation, child_values_all = operations[next_to_solve_wire]
        child_values = [
            value_if_string(
                x,
            )
            for x in child_values_all
        ]

        values[next_to_solve_wire] = apply_operation(operation, child_values)
    return values


def puzzle(puzzle_input: list[str]):
    graph, operations = build_graph(puzzle_input)

    target = "a"
    values = evaluate(graph, operations, target)
    return values[target]
