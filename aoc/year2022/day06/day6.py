def puzzle(puzzle_input: str) -> int:
    """
    puzzle Day 6

    Finds in a chunksize of 4 (predetermined), if no duplicate letters appear

    Args:
        puzzle_input (str): input string

    Returns:
        int: index
    """

    # check if type is correct
    if type(puzzle_input) != str:
        raise TypeError("Input needs to be a string")

    buffer_size = 4

    for i in range(0, len(puzzle_input)):
        buffer = puzzle_input[i : i + buffer_size]
        unique = True

        for j in set(buffer):
            if buffer.count(j) > 1:
                unique = False
                break

        if unique:
            return i + buffer_size

    # wrong value
    return -1