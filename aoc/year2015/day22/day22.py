from copy import deepcopy

convert_dict: dict[int, str] = {
    0: "Magic",
    1: "Drain",
    2: "Shield",
    3: "Poison",
    4: "Recharge",
}


class battle_info:
    def __init__(
        self, player: dict[str, int], boss: dict[str, int], debug: bool = False
    ) -> None:
        self.turns: list[int] = []
        self.spent_mana: float = 0
        self.shield: int = 0
        self.poison: int = 0
        self.recharge: int = 0

        self.player: dict[str, int] = player
        self.boss: dict[str, int] = boss
        self.debug: bool = debug

    def start_turn(self) -> None:
        if self.shield >= 1:
            self.shield -= 1

        if self.poison >= 1:
            self.poison -= 1
            self.boss["hp"] -= 3

        if self.recharge >= 1:
            self.recharge -= 1
            self.player["mana"] += 101

        if self.debug:
            print(f"boss: {self.boss}.")
            print(f"player: {self.player}.")

    def action_check(self, cast: int) -> bool:
        match cast:
            case 2:  # shield
                return bool(self.shield)

            case 3:  # Poison
                return bool(self.poison)

            case 4:  # recharge
                return bool(self.recharge)

            case _:
                return False

    def action(self, cast: int) -> None:
        match cast:
            case 0:  # magic missile
                cost = 53
                self.boss["hp"] -= 4

            case 1:  # drain
                cost = 73
                self.boss["hp"] -= 2
                self.player["hp"] += 2

            case 2:  # shield
                cost = 113
                self.shield = 6

            case 3:  # Poison
                cost = 173
                self.poison = 6

            case 4:  # recharge
                cost = 229
                self.recharge = 5

            case _:
                raise NotImplementedError

        self.turns.append(cast)
        self.spent_mana += cost
        self.player["mana"] -= cost

    def boss_turn(self) -> None:
        if self.shield:
            self.player["hp"] -= max(self.boss["dmg"] - 7, 1)
        else:
            self.player["hp"] -= self.boss["dmg"]

    def win_lose_check(self, min_spent: float) -> tuple[bool, float]:
        # lose
        if self.player["mana"] < 0:
            if self.debug:
                print(f"player mana < 0, {self.player['mana']}  < 0 ")
            return True, min_spent

        # lose
        if self.player["hp"] <= 0:
            if self.debug:
                print(f"player hp <= 0, {self.player['hp']}  <= 0 ")
            return True, min_spent

        # lose
        if self.spent_mana > min_spent:
            if self.debug:
                print(f"spend > min, {self.spent_mana} > {min_spent} ")
            return True, min_spent

        # win
        if self.boss["hp"] <= 0:
            if self.debug:
                print(f"bosshp <= 0, {self.boss['hp']}  <= 0 ")
            return True, self.spent_mana

        return False, min_spent


def start_p_turn(simulation: battle_info, min_spent: float) -> float:
    win_lose: bool
    mana_val: float

    simulation.start_turn()
    win_lose, mana_val = simulation.win_lose_check(min_spent)
    if win_lose:
        return mana_val

    # ====== start is over, your turn =====
    for i in range(0, 5):
        if not simulation.action_check(i):
            min_spent = min(action_turn(deepcopy(simulation), min_spent, i), min_spent)
    return min_spent


def action_turn(simulation: battle_info, min_spent: float, action: int) -> float:
    win_lose: bool
    mana_val: float
    simulation.action(action)

    win_lose, mana_val = simulation.win_lose_check(min_spent)
    if win_lose:
        return mana_val

    # ======  your turn is over, boss turn =====
    simulation.start_turn()
    win_lose, mana_val = simulation.win_lose_check(min_spent)
    if win_lose:
        return mana_val

    # BOSS DAMAGE
    simulation.boss_turn()
    win_lose, mana_val = simulation.win_lose_check(min_spent)
    if win_lose:
        return mana_val

    # ====== boss turn is over  =====

    min_spent = min(start_p_turn(deepcopy(simulation), min_spent), min_spent)
    return min_spent


def puzzle(puzzle_input: list[str]) -> float:
    boss = {}
    boss["hp"] = int(puzzle_input[0].split(":")[-1])
    boss["dmg"] = int(puzzle_input[1].split(":")[-1])

    player: dict[str, int] = {"hp": 50, "mana": 500}

    simulation = battle_info(player, boss, debug=False)
    return start_p_turn(simulation, min_spent=float("inf"))