class flipflop:
    def __init__(self, name) -> None:
        # low
        self.name = name
        self.pulse = -1
        self.cycle = 1

    def activate(self, pulse: float, _: str) -> float:
        """Returns if signal is transferred"""

        # ignore high pulse
        if pulse == 1:
            # zero = ignore
            return 0

        # low pulse -> flip
        self.pulse *= -1
        return self.pulse

    def solve_cycle(self, child: "flipflop") -> bool:
        self.cycle = child.cycle
        return True

    def __add__(self, other: float) -> float:
        if self.pulse == 1:
            return other + 1
        else:
            return other

    def __radd__(self, other: float) -> float:
        return self.__add__(other)

    def __repr__(self) -> str:
        return f"FF({self.pulse})"


class conjunction:
    def __init__(self, name) -> None:
        self.name = name
        self.receive_dict: dict[str, float] = {}
        self.cycle = 0

    def add_kids(self, child_lst):
        for i in child_lst:
            self.receive_dict[i] = -1

    def activate(self, pulse: float, parent: str) -> float:
        # print("PULSE: ", pulse)
        self.receive_dict[parent] = pulse

        if all([x == 1 for x in self.receive_dict.values()]):
            # print(self.name, "ALL ONs")
            return -1
        else:
            return 1

    def solve_cycle(self, children) -> bool:
        for child in children:
            if child.cycle == 0:
                return False

        self.cycle = 1
        for child in children:
            self.cycle *= child.cycle
        return True

    def __add__(self, other: float) -> float:
        if any([x == 1 for x in self.receive_dict.values()]):
            return other + 1
        else:
            return other

    def __radd__(self, other: float) -> float:
        return self.__add__(other)

    def __repr__(self) -> str:
        return f"CO({self.receive_dict.values()})"


class broadcaster:
    def __init__(self, name) -> None:
        self.name = name
        self.cycle = 1
        pass

    def activate(self, pulse: float, _: str) -> float:
        return pulse

    def __add__(self, other: float) -> float:
        return other

    def __radd__(self, other: float) -> float:
        return self.__add__(other)

    def __repr__(self) -> str:
        return "BR"
