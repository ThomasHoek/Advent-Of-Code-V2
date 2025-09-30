import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input.txt", "r")
boss = {}
boss["hp"] = int(puzzle_input.readline()[-4:].rstrip())
boss["dmg"] = int(puzzle_input.readline()[-2:].rstrip())
boss["arm"] = int(puzzle_input.readline()[-2:].rstrip())
hp = 100

weapon_lst = [[8, 4, 0],
              [10, 5, 0],
              [25, 6, 0],
              [40, 7, 0],
              [74, 8, 0]]

armour_lst = [[0, 0, 0],
              [13, 0, 1],
              [31, 0, 2],
              [53, 0, 3],
              [75, 0, 4],
              [102, 0, 5]]

ring_lst = [[0, 0, 0],
            [25, 1, 0],
            [50, 2, 0],
            [100, 3, 0],
            [20, 0, 1],
            [40, 0, 2],
            [80, 0, 3]]

max_cost = float(0)


def battle(weapon, armour, ring1, ring2, boss, max_cost):
    if (ring1 != ring2) or (ring1 == [0, 0, 0] and (ring1 == ring2)):
        cost, dmg, arm = [sum(x) for x in zip(weapon, armour,
                                              ring1, ring2)]
        if cost < max_cost:
            return max_cost

        boss_dmg = max((boss["dmg"] - arm), 1)
        player_dmg = max((dmg - boss["arm"]), 1)

        boss_turn = (hp // boss_dmg + bool(hp % boss_dmg))
        player_turn = (boss["hp"] // player_dmg +
                       bool(boss["hp"] % player_dmg))

        # player wins
        if player_turn > boss_turn:
            if cost > max_cost:
                return cost

    return max_cost


# 25 random iters to set a minimum.
for i in range(25):
    weapon = random.choice(weapon_lst)
    armour = random.choice(armour_lst)
    ring1 = random.choice(ring_lst)
    ring2 = random.choice(ring_lst)
    max_cost = battle(weapon, armour, ring1, ring2, boss, max_cost)

for weapon in weapon_lst:
    for armour in armour_lst:
        for ring1 in ring_lst:
            for ring2 in ring_lst:
                max_cost = battle(weapon, armour, ring1, ring2, boss, max_cost)
print(max_cost)
