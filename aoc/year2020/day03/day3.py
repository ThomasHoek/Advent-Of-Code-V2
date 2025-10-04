# [Done] exited with code=0 in 0.038 seconds

def puzzle(puzzle_input) -> int:
    total = {".": 0, "#": 0}
    counter = 0
    for i in range(len(puzzle_input)):
        total[puzzle_input[i][counter]] = total[puzzle_input[i][counter]] + 1
        counter = (counter + 3) % len(puzzle_input[i].rstrip())


    return total["#"]
