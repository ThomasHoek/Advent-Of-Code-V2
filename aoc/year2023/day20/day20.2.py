from __future__ import annotations
from math import lcm


from aoc.year2023.day20.day20_modules import broadcaster, flipflop, conjunction

day20_mods = broadcaster | flipflop | conjunction


def puzzle(puzzle_input: list[str]) -> int:
    # Load up dict with children.
    con_lst: list[str] = []
    parent_dict: dict[str, list[str]] = {}
    order_dict: dict[str, tuple[list[str], broadcaster | flipflop | conjunction]] = {}
    for line in puzzle_input:
        parent, children = line.split(" -> ")
        children_lst = children.split(", ")

        if parent == "broadcaster":
            order_dict["broadcaster"] = (children_lst, broadcaster("broadcaster"))
        else:
            # add parents so we can warm up conjunctions
            for x in children_lst:
                if x not in parent_dict:
                    parent_dict[x] = []
                parent_dict[x].append(parent[1:])

            if parent[0] == "%":
                order_dict[parent[1:]] = (children_lst, flipflop(parent[1:]))
            elif parent[0] == "&":
                con_lst.append(parent[1:])
                order_dict[parent[1:]] = (children_lst, conjunction(parent[1:]))
            else:
                raise NotImplementedError(f"Unknown symbol: {parent}")

    # for every conjunction, add all children.
    # delayed add since can't add child that isn't created yet
    for x in con_lst:
        _, cur_con = order_dict[x]
        assert isinstance(cur_con, conjunction)
        cur_con.add_kids(parent_dict[x])

    # broadcast
    broad_children, _ = order_dict["broadcaster"]

    # calculate LCM
    kh_dict: dict[str, int] = {}

    # RUN SIMULATION
    counter = 0
    while True:
        queue: list[tuple[str, str, float]] = []

        counter += 1
        # to broadcast button
        for child in broad_children:
            queue.append(("broadcaster", child, -1.0))

        # iterate until QUEUE is empty

        for parent_str, child_str, signal in queue:
            # if output, ignore since cant send signal
            if child_str not in order_dict:
                continue

            children_found, self = order_dict[child_str]
            out = self.activate(signal, parent_str)

            # ignore signal if not high or low
            if out == 0:
                continue

            # add to LCM if signal is high
            if self.name == "kh" and signal == 1:
                kh_dict[parent_str] = counter

            # send to children and add to queue
            for child_found_str in children_found:
                queue.append((child_str, child_found_str, out))

        if len(kh_dict) == 4:
            break

    return lcm(*list(kh_dict.values()))
