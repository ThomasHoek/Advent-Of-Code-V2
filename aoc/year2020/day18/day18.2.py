

def reverse(string):
    return string[::-1]


def multiply(num1, num2):
    return num1 * num2


def add(num1, num2):
    return num1 + num2


def solve_parenthensies(equation, recursive=False):
    front_out_of_parenthensies = equation[: equation.index("(")]
    index_par = len(equation) - equation[::-1].index(")")
    back_out_of_parenthensies = equation[index_par:]
    parenthensies = equation[equation.index("(") : index_par]

    counter_equal = 0
    open_dict = {}
    close_dict = {}

    for i in range(len(parenthensies)):
        if parenthensies[i] == "(":
            open_dict[i] = counter_equal
            counter_equal += 1

        elif parenthensies[i] == ")":
            counter_equal -= 1
            close_dict[i] = counter_equal

    start = 0
    awnser_parenthensies = []
    for i in range(len(parenthensies)):
        if i in open_dict and open_dict[i] == 0:
            start = i

        if i in close_dict and close_dict[i] == 0:
            awnser_parenthensies.append(
                solve(parenthensies[start + 1 : i], recursive=True)
            )

    start = True
    counter = len(awnser_parenthensies) - 1
    parenthensies_replace = []
    for i in range(len(parenthensies) - 1, -1, -1):
        if i in close_dict and close_dict[i] == 0:
            start = False

        if start:
            parenthensies_replace.append(parenthensies[i])

        if i in open_dict and open_dict[i] == 0:
            start = True
            parenthensies_replace.append((str(awnser_parenthensies[counter])))
            counter -= 1
    return solve(
        front_out_of_parenthensies
        + "".join([str(i) for i in parenthensies_replace[::-1]])
        + back_out_of_parenthensies
    )


def solve_no_parenthensies(equation):
    equation_split = equation.split(" ")
    while len(equation_split) != 1:
        first_operator = next(
            (equation_split.index(x) for x in equation_split if x == "+"), None
        )
        if first_operator is None:
            first_operator = next(
                (equation_split.index(x) for x in equation_split if x == "*"), None
            )

        num1 = int(equation_split[first_operator - 1])
        num2 = int(equation_split[first_operator + 1])
        operator = equation_split[first_operator]

        if operator == "+":
            total = add(num1, num2)
        else:
            total = multiply(num1, num2)

        equation_split = (
            equation_split[: first_operator - 1]
            + [total]
            + equation_split[first_operator + 2 :]
        )

    return equation_split


def solve(equation, recursive=False):
    # print(equation)
    if equation.count("(") == 0:
        return [int(i) for i in solve_no_parenthensies(equation)][0]

    else:
        return solve_parenthensies(equation, recursive)

def puzzle(inputfile):
    solutions = []
    for equation in inputfile:
        solutions.append(int(solve(equation)))

    return sum(solutions)
