# [Done] exited with code=0 in 0.259 seconds
import copy


def puzzle(input_file) -> int:
    bag_list = []
    new_bags = ["shiny gold"]


    while True:
        previous_bag = copy.deepcopy(bag_list)
        for line in input_file:
            for nbag in new_bags:
                if nbag in line:
                    if nbag == " ".join(line.split(" ")[:2]):
                        pass

                    else:
                        bag_list.append(" ".join(line.split(" ")[:2]))

        if previous_bag == bag_list:
            break

        else:
            new_bags = set(bag_list) - set(previous_bag)


    return len(set(bag_list))
