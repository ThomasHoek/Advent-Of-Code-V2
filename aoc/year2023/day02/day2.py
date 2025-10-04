from typing import Any

# globals
max_red = 12
max_green = 13
max_blue = 14


def inner_ball_check(ball_split: list[str]) -> bool:
    for ball_grab in ball_split:
        seperate_balls = ball_grab.split(",")
        for i in seperate_balls:
            i_clean = i.strip()
            num, colour = i_clean.split(" ")
            match colour:
                case "blue":
                    if int(num) > max_blue:
                        return False
                case "red":
                    if int(num) > max_red:
                        return False
                case "green":
                    if int(num) > max_green:
                        return False
                case _:
                    assert NotImplementedError("Should not reach this point")
    return True


def puzzle(puzzle_input: Any) -> Any:
    total = 0
    for game in puzzle_input:
        game_info, balls = game.split(": ")
        game_number = int(game_info.replace("Game ", ""))

        ball_split = balls.split(";")
        if inner_ball_check(ball_split):
            total += game_number

    return total
