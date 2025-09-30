
import random

def battle(hp, weapon, armour, ring1, ring2, boss, max_cost):
    if (ring1 != ring2) or (ring1 == [0, 0, 0] and (ring1 == ring2)):
        cost, dmg, arm = [sum(x) for x in zip(weapon, armour, ring1, ring2)]
        if cost < max_cost:
            return max_cost

        boss_dmg = max((boss["dmg"] - arm), 1)
        player_dmg = max((dmg - boss["arm"]), 1)

        boss_turn = hp // boss_dmg + bool(hp % boss_dmg)
        player_turn = boss["hp"] // player_dmg + bool(boss["hp"] % player_dmg)

        # player wins
        if player_turn > boss_turn:
            if cost > max_cost:
                return cost

    return max_cost


def puzzle(puzzle_input):
    boss = {}
    boss["hp"] = int(puzzle_input[0].split()[2])
    boss["dmg"] = int(puzzle_input[1].split()[1])
    boss["arm"] = int(puzzle_input[2].split()[1])
    hp = 100

    weapon_lst = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]

    armour_lst = [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]

    ring_lst = [
        [0, 0, 0],
        [25, 1, 0],
        [50, 2, 0],
        [100, 3, 0],
        [20, 0, 1],
        [40, 0, 2],
        [80, 0, 3],
    ]

    max_cost = float(0)
    for weapon in weapon_lst:
        for armour in armour_lst:
            for ring1 in ring_lst:
                for ring2 in ring_lst:
                    max_cost = battle(hp, weapon, armour, ring1, ring2, boss, max_cost)
    return max_cost
