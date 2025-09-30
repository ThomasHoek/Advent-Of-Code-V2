# [Done] exited with code=0 in 0.043 seconds
input_file = open("input.txt", "r").readlines()

list_total = 1


def trees(increment, step):
    total = {".": 0, "#": 0}
    counter = 0
    for i in range(0, len(input_file), step):

        total[input_file[i][counter]] = total[input_file[i][counter]] + 1
        counter = (counter + increment) % len(input_file[i].rstrip())

    return total['#']


list_total *= trees(1, 1)  # Right 1, down 1.
list_total *= trees(3, 1)  # Right 3, down 1.
list_total *= trees(5, 1)  # Right 5, down 1.
list_total *= trees(7, 1)  # Right 7, down 1.
list_total *= trees(1, 2)  # Right 1, down 2.


print(list_total)
