import sys
sys.path.insert(0, '/users/jonah/Desktop/coding/tic-tac-toe/src')

from ai import *

def printBoard(board: list) -> None:
    """Prints the board in a fancy way

    Args:
        board (list): Game board for Tic-Tac-Toe
    """
    for i in range(3):

        print(f' {board[(i*3)]} | {board[(i*3)+1]} | {board[(i*3)+2]}')

        if (i < 2):
            print("--- --- ---")

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
    all_difficulties = [1, 2, 3]

    for difficulty in all_difficulties:
        for board in all_board:
            printBoard(board)
            move = ai(board, difficulty)
            print('Alex\'s move: ', move)

            print()
        
        print()


if __name__ == '__main__':
    main()
