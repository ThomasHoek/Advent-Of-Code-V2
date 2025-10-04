from typing import Any


def inner_ball_check(ball_split: list[str]) -> int:
    max_red = 0
    max_green = 0
    max_blue = 0
    for ball_grab in ball_split:
        seperate_balls = ball_grab.split(",")
        for i in seperate_balls:
            i_clean = i.strip()
            num, colour = i_clean.split(" ")
            match colour:
                case "blue":
                    if int(num) > max_blue:
                        max_blue = int(num)
                case "red":
                    if int(num) > max_red:
                        max_red = int(num)
                case "green":
                    if int(num) > max_green:
                        max_green = int(num)
                case _:
                    assert NotImplementedError("Should not reach this point")
    return max_green * max_red * max_blue


def puzzle(puzzle_input: Any) -> Any:
    total = 0
    for game in puzzle_input:
        game_info, balls = game.split(": ")
        # game_number = int(game_info.replace("Game ", ""))

        ball_split = balls.split(";")
        total += inner_ball_check(ball_split)

    return total
