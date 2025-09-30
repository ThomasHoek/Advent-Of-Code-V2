import os

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input = open(f"{dir_path}/input2.txt", "r").readline()


def converter_int(num: int) -> str:
    return chr(num + 96)


def converter_str(string: str) -> int:
    return ord(string) - 96


def next_password(password: list) -> list:
    """next_password generator

    Increases the password

    Parameters
    ----------
    string : str
        Previous password

    Returns
    -------
    str
        Next iteration of the password
    """
    password.reverse()
    password[0] += 1

    while 27 in password:
        for index, value in enumerate(password):
            if value == 27:
                password[index] = 1
                try:
                    password[index + 1] += 1
                except IndexError:
                    password[-1] = 1

    for index, value in enumerate(password):
        if value == 9 or value == 15 or value == 12:  # i
            password[index] += 1
            for i in range(index-1, 0, -1):
                password[i] = 1

    password.reverse()
    return password


def check_password(password: list) -> list:
    password = next_password(password)
    while True:
        check = False
        for i in range(len(password) - 2):
            cur = password[i]
            if cur == (password[i + 1] - 1) and cur == (password[i + 2] - 2):
                check = True

        if check:  # if earlier if statements are also valid
            check = False
            count = 0
            prev_letter = None
            for i in range(len(password) - 1):
                cur = password[i]
                if cur == password[i + 1] and prev_letter is not cur:
                    prev_letter = cur
                    count += 1

            if count > 1:
                check = True

        if check:
            return password
        else:
            password = next_password(password)


num_puzzle = [converter_str(num) for num in puzzle_input.rstrip()]
awnser_num = check_password(num_puzzle)
awnser_str = ''.join([converter_int(num) for num in awnser_num])
print(awnser_str)
