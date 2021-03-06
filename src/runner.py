import json


def main():
    # load json
    with open('./src/settings.json', 'r') as FILE:
        settings = json.load(FILE)

    # parse jsoon
    gamemode = settings['mode']
    difficulty = settings['ai difficulty']

    # run game
    if gamemode == 'cli':
        from cli import run_cli
        run_cli(difficulty)
    elif gamemode == 'gui':
        from gui import run_gui
        run_gui(difficulty)
    else:
        print('Unknown gamemode!')


if __name__ == '__main__':
    main()
