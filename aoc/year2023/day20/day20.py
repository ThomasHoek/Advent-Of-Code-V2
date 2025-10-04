from __future__ import annotations
from collections import Counter


from aoc.year2023.day20.day20_modules import broadcaster, flipflop, conjunction


def puzzle(puzzle_input: list[str]) -> int:
    total = 0

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

    counter = 0
    high_low_count: Counter[float] = Counter()

    # RUN SIMULATION
    while True:
        queue: list[tuple[str, str, float]] = []

        counter += 1
        high_low_count[-1] += 1
        # to broadcast button
        for child in broad_children:
            queue.append(("broadcaster", child, -1.0))

        # iterate until QUEUE is empty
        for parent_str, child_str, signal in queue:
            high_low_count[signal] += 1

            # if output, ignore since cant send signal
            if child_str not in order_dict:
                continue

            children_found, self = order_dict[child_str]
            out = self.activate(signal, parent_str)

            # ignore signal if not high or low
            if out == 0:
                continue

            # send to children and add to queue
            for child_found_str in children_found:
                queue.append((child_str, child_found_str, out))

        # 1000 button presses
        if counter == 1000:
            break

    total = high_low_count[-1] * high_low_count[1]
    return total