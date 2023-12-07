# For every line:
# get index of line

def check_if_game_applicable(input_string):
    lines = input_string.split('\n')
    final_sum = 0

    max_red = 12
    max_green = 13
    max_blue = 14

    for idx, line in enumerate(lines):
        current_game = idx + 1
        current_game_applicable = True
        games = line.split(';')
        for game in games:
            amount_green = 0
            amount_blue = 0
            amount_red = 0
            index_green = game.find('green')
            if index_green > 1:
                amount_green = int(game[index_green - 3] + game[index_green - 2])
            index_blue = game.find('blue')
            if index_blue > 1:
                amount_blue = int(game[index_blue - 3] + game[index_blue - 2])
            index_red = game.find('red')
            if index_red > 1:
                amount_red = int(game[index_red - 3] + game[index_red - 2])
            if amount_red > max_red or amount_blue > max_blue or amount_green > max_green:
                current_game_applicable = False
        if current_game_applicable:
            final_sum += current_game
    print(final_sum)


def power_of_min_applicable_games(input_string):
    lines = input_string.split('\n')
    final_sum = 0

    max_red = 12
    max_green = 13
    max_blue = 14

    for idx, line in enumerate(lines):
        current_game_applicable = True
        games = line.split(';')
        max_green_game = 0
        max_red_game = 0
        max_blue_game = 0
        for game in games:
            amount_green = 0
            amount_blue = 0
            amount_red = 0
            index_green = game.find('green')
            if index_green > 1:
                amount_green = int(game[index_green - 3] + game[index_green - 2])
            index_blue = game.find('blue')
            if index_blue > 1:
                amount_blue = int(game[index_blue - 3] + game[index_blue - 2])
            index_red = game.find('red')
            if index_red > 1:
                amount_red = int(game[index_red - 3] + game[index_red - 2])
            if amount_red > max_red or amount_blue > max_blue or amount_green > max_green:
                current_game_applicable = False
            else:
                if amount_green >= max_green_game:
                    max_green_game = amount_green
                if amount_red >= max_red_game:
                    max_red_game = amount_red
                if amount_blue >= max_blue_game:
                    max_blue_game = amount_blue
        if current_game_applicable:
            final_sum += max_blue_game * max_red_game * max_green_game
    print(final_sum)
