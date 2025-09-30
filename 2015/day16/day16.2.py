import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()
puzzle_input = [x.rstrip() for x in puzzle_input]


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

        indices = [x.start() for x in re.finditer(" ",  inp_str)][::2]
        self.name = inp_str[:indices[0]]
        self.parsed = inp_str
        self.indices = indices + [len(inp_str)]

    def check(self):

        for i in range(len(self.indices) - 1):
            _, name, var = self.parsed[self.indices[i]:
                                       self.indices[i+1]].split(" ")

            var = int(var)
            if name == "children" and self.children != var:
                return False

            elif name == "cats" and self.cats >= var:
                return False

            elif name == "samoyeds" and self.samoyeds != var:
                return False

            elif name == "pomeranians" and self.pomeranians <= var:
                return False

            elif name == "akitas" and self.akitas != var:
                return False

            elif name == "vizslas" and self.vizslas != var:
                return False

            elif name == "goldfish" and self.goldfish <= var:
                return False

            elif name == "trees" and self.trees >= var:
                return False

            elif name == "cars" and self.cars != var:
                return False

            elif name == "perfumes" and self.perfumes != var:
                return False
        return True


for line in puzzle_input:
    a = aunt(line)
    booltest = a.check()
    if booltest:
        print(a.name)
