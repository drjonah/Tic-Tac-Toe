import sys
sys.path.insert(0, '/users/jonah/Desktop/coding/tic-tac-toe')

from ai import *

def get_boards():
    board = [
        [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', 'x', 'x', 'o', ' ', ' ', 'x', ' ', ' '],
        ['x', 'x', 'o', 'x', 'o', ' ', ' ', ' ', ' ']
    ]

    return board


def main():
    all_board = get_boards()
    all_difficulties = [4, 2, 1]

    for difficulty in all_difficulties:
        for board in all_board:
            print(f'level {difficulty}, board {board}')
            move = ai(board, difficulty)
            print(f'best move: {move}')

            print()
        
        print()


if __name__ == '__main__':
    main()
