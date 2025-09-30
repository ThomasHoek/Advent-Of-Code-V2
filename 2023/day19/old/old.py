

@dataclass
class decision:
    equation: Callable[[int], bool] | bool
    result: Tree | str


class Tree:
    def __init__(self, name: str, split_str: str) -> None:
        self.name = name
        split_lst: list[str] = split_str.split(",")
        self.out = split_lst.pop(-1)

        self.x: decision = decision(False, "R")
        self.m: decision = decision(False, "R")
        self.a: decision = decision(False, "R")
        self.s: decision = decision(False, "R")

        def bigger(a: int, b: int) -> bool:
            return a < b

        def smaller(a: int, b: int) -> bool:
            return a > b

        for x in split_lst:
            equation, pointer = x.split(":")
            if ">" in equation:
                letter, end_num_str = equation.split(">")
                end_num = int(end_num_str)
                lambda_bool = partial(bigger, end_num)
            else:
                letter, end_num_str = equation.split("<")
                end_num = int(end_num_str)
                lambda_bool = partial(smaller, end_num)

            match letter:
                case "x":
                    self.x = decision(lambda_bool, pointer)
                case "m":
                    self.m = decision(lambda_bool, pointer)
                case "a":
                    self.a = decision(lambda_bool, pointer)
                case "s":
                    self.s = decision(lambda_bool, pointer)
                case _:
                    raise NotImplementedError(f"Tree letter error, unfound {letter}")

    def set_pointers(self, pointer_dict: dict[str, Tree]):
        if self.x.equation:
            if self.x.result == "R" or self.x.result == "A":
                pass
            else:
                self.x.result = pointer_dict[self.x.result]

        if self.m.equation:
            if self.m.result == "R" or self.m.result == "A":
                pass
            else:
                self.m.result = pointer_dict[self.m.result]

        if self.a.equation:
            if self.a.result == "R" or self.a.result == "A":
                pass
            else:
                self.a.result = pointer_dict[self.a.result]

        if self.s.equation:
            if self.s.result == "R" or self.s.result == "A":
                pass
            else:
                self.s.result = pointer_dict[self.s.result]

        if self.out == "R" or self.out == "A":
            pass
        else:
            self.out = pointer_dict[self.out]

    def solve(self, inp_x: int, inp_m: int, inp_a: int, inp_s: int) -> str:
        print(self.name, end="")

        def eval_equation(equation: Callable[[int], bool] | bool, eq_inp: int) -> bool:
            if isinstance(equation, bool):
                return equation

            return equation(eq_inp)

        if eval_equation(self.x.equation, inp_x):
            print("|X| ", end=" ")
            if isinstance(self.x.result, str):
                return self.x.result
            else:
                return self.x.result.solve(inp_x, inp_m, inp_a, inp_s)

        elif eval_equation(self.m.equation, inp_m):
            print("|M| ", end=" ")
            if isinstance(self.m.result, str):
                return self.m.result
            else:
                return self.m.result.solve(inp_x, inp_m, inp_a, inp_s)

        elif eval_equation(self.a.equation, inp_a):
            print("|A| ", end=" ")
            if isinstance(self.a.result, str):
                return self.a.result
            else:
                return self.a.result.solve(inp_x, inp_m, inp_a, inp_s)

        elif eval_equation(self.s.equation, inp_s):
            print("|S| ", end=" ")
            if isinstance(self.s.result, str):
                return self.s.result
            else:
                return self.s.result.solve(inp_x, inp_m, inp_a, inp_s)
        else:
            print("|O| ", end=" ")
            if isinstance(self.out, str):
                return self.out
            else:
                return self.out.solve(inp_x, inp_m, inp_a, inp_s)

    def __repr__(self) -> str:
        return f"TREE: {self.name}"
        # return f"{self.name} = (X: {self.x}, M:{self.m}, A:{self.a}, S:{self.s} | OUT:{self.out})"
