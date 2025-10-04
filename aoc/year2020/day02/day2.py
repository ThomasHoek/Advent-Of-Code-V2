# [Done] exited with code=0 in 0.067 seconds


def puzzle(puzzle_input) -> int:
    input_file = [word.rstrip().split(" ") for word in puzzle_input]
    
    correct = 0
    for lst in range(len(input_file)):
        minimaal, maximaal = list(map(int, input_file[lst][0].split("-")))
        letter = input_file[lst][1].replace(":", "")
        woord = input_file[lst][-1]

        if woord.count(letter) >= minimaal and woord.count(letter) <= maximaal:
            correct += 1

    return correct
