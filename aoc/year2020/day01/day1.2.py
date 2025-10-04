# [Done] exited with code=0 in 6.059 seconds
import math
import numpy as np


def puzzle(puzzle_input)-> int:
    task_input = [int(word.rstrip()) for word in puzzle_input if word != ""]
    task_input.sort()
    combined_numbers = []


    for j in task_input:
        for i in task_input:
            first_number = 0
            first_number_list = []

            second_number = len(task_input) - 1
            second_number_list = []

            while True:
                num_lst = np.mean([first_number, second_number])
                output = j + i + task_input[math.floor(num_lst)]

                if output == 2020:
                    combined_numbers.append([j, i, task_input[math.floor(num_lst)]])
                    break

                elif output > 2020:  # bigger then
                    second_number = math.floor(num_lst)
                    second_number_list.append(second_number)
                    if second_number_list.count(second_number) > 3:
                        break

                elif output < 2020:
                    first_number = math.ceil(num_lst)
                    first_number_list.append(first_number)
                    if first_number_list.count(first_number) > 3:
                        break

                if first_number == second_number:
                    break


    combined_numbers = [
        [lst[0] + lst[1] + lst[2], lst[0] * lst[1] * lst[2]] for lst in combined_numbers
    ]

    combined_numbers_max = [lst[-1] for lst in combined_numbers]
    return max(combined_numbers_max)
