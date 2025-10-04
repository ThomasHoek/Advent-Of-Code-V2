import re



class aunt:
    children = 3
    cats = 7
    samoyeds = 2
    pomeranians = 3
    akitas = 0
    vizslas = 0
    goldfish = 5
    trees = 3
    cars = 2
    perfumes = 1

    def __init__(self, inp_str: str):
        inp_str = inp_str.replace(":", "")
        inp_str = inp_str.replace("Sue ", "")
        inp_str = inp_str.replace(",", "")

        indices = [x.start() for x in re.finditer(" ", inp_str)][::2]
        self.name = inp_str[: indices[0]]
        self.parsed = inp_str
        self.indices = indices + [len(inp_str)]

    def check(self):
        for i in range(len(self.indices) - 1):
            _, name, var = self.parsed[self.indices[i] : self.indices[i + 1]].split(" ")
            var = int(var)
            match name:
                case "children":
                    if self.children != var:
                        return False
                case "cats":
                    if self.cats != var:
                        return False
                case "samoyeds":
                    if self.samoyeds != var:
                        return False
                case "pomeranians":
                    if self.pomeranians != var:
                        return False
                case "akitas":
                    if self.akitas != var:
                        return False
                case "vizslas":
                    if self.vizslas != var:
                        return False
                case "goldfish":
                    if self.goldfish != var:
                        return False
                case "trees":
                    if self.trees != var:
                        return False
                case "cars":
                    if self.cars != var:
                        return False
                case "perfumes":
                    if self.perfumes != var:
                        return False
                case _:
                    raise NotImplementedError(f"Unknown attribute {name}")
        return True

def puzzle(puzzle_input: list[str]) -> None:
    for line in puzzle_input:
        a = aunt(line)
        booltest = a.check()
        if booltest:
            return a.name
