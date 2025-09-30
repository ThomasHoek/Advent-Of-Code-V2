# imports

# code solution
def puzzle(puzzle_input):
    pass

# helper functions
if __name__ == "__main__":
    import sys
    import os

    try:  # if any of these words found in arguments
        final = "final" in sys.argv  # runs final tset
        file = "file" in sys.argv   # writes all output/print to file
        clock = "time" in sys.argv  # gives time as output

    except IndexError:  # if no sys argv provided
        final = False
        file = False
        clock = False

    # get current path
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # change all IO to file out.txt
    if file:
        orig_stdout = sys.stdout
        f = open('out.txt', 'w')
        sys.stdout = f

    # imports clock functionality
    if clock:
        import time
        start = time.time()

    # runs the final case
    if final:
        # reads file
        puzzle_input = open(f"{dir_path}/input.txt", "r").readlines()

        # removes \n at end
        puzzle_input_r = [x.rstrip() for x in puzzle_input]

        print(puzzle(puzzle_input_r))

    # runs test cases
    else:
        # reads test cases by default for debugging
        puzzle_input = open(f"{dir_path}/test.txt", "r").readlines()

        # removes \n at end
        puzzle_input_r = [x.rstrip() for x in puzzle_input]

        # replace NotImplemented with expected puzzle output to see if result is correct
        assert puzzle(puzzle_input) == NotImplemented

    if clock:
        print("time: ", time.time() - start)

    if file:
        sys.stdout = orig_stdout
        f.close()
