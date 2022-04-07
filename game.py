import copy
import datetime
import os
from ai import *


def is_on_game_board(move):
    if move >= 0 and move < 9:
        return True

    return False


def is_open(game_board, move):
    if game_board[move] == ' ':
        return True

    return False


def move_player(game_board, move):
    if is_on_game_board(move) and is_open(game_board, move):
        game_board[move] = 'x'
        return game_board, True
    return game_board, False


def win(game_board: list) -> tuple:
    """Checks to see if someone has won the game and which player won

    Args:
        game_board (list): Game board for Tic-Tac-Toe

    Returns:
        tuple: (bool, str) - (whether the game has ended [True - finished, False - continue], winning character [IF ANY])
    """

    for player in ['x', 'o']:

        for i in range(len(game_board)//3):
            # horizontal
            if (game_board[i*3] == player and game_board[(i*3)+1] == player and game_board[(i*3)+2] == player):
                return True, player
            # vertical
            elif (game_board[i] == player and game_board[i+3] == player and game_board[i+6] == player):
                return True, player

        # diagonal: left to right
        if (game_board[0] == player and game_board[4] == player and game_board[8] == player):
            return True, player
        # diagonal: right to left
        elif (game_board[2] == player and game_board[4] == player and game_board[6] == player):
            return True, player

    return False, str()


def printBoard(game_board: list) -> None:
    """Prints the board in a fancy way

    Args:
        game_board (list): Game board for Tic-Tac-Toe
    """
    for i in range(3):

        print(
            f' {game_board[(i*3)]} | {game_board[(i*3)+1]} | {game_board[(i*3)+2]}')

        if (i < 2):
            print("-----------")


def store_games(game_board, difficulty, number_of_moves, winner):
    TIME_STAMP = str(datetime.datetime.now())
    FILE_NAME = ('-').join(TIME_STAMP.split('.')[0].split(':'))

    try:
        with open(f'./games/{FILE_NAME}.txt', 'w') as FILE:

            FILE.write('Tic-Tac-Toe\n\n')
            FILE.write(f'Time Stamp: {TIME_STAMP}\n')
            FILE.write(f'Difficulty: {difficulty}\n')
            FILE.write(f'Move Count: {number_of_moves}\n')
            FILE.write(f'Winner: {winner}\n\n')

            FILE.write('Game Board:\n')
            for i in range(3):

                FILE.write(
                    f' {game_board[(i*3)]} | {game_board[(i*3)+1]} | {game_board[(i*3)+2]}\n')

                if (i < 2):
                    FILE.write("-----------\n")

        print('Game stored.')

    except:
        print('Game saving failed.')

def end(game_board, result, character, difficulty, number_of_moves):
    if result and character == 'x':
        print('Win!')
        printBoard(game_board)
        store_games(game_board, difficulty, number_of_moves, character)
        return True
    elif result and character == 'o':
        print('Loss!')
        printBoard(game_board)
        store_games(game_board, difficulty, number_of_moves, character)
        return True
    elif isFull(game_board):
        print('Tie!')
        printBoard(game_board)
        store_games(game_board, difficulty, number_of_moves, character)
        return True
    return False


def main():
    os.system('cls')
    print('IMPOSSIBLE TIC TAC TOE')

    # game board
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # constants
    # difficulty = 8 # easy
    # difficulty = 4 # medium
    difficulty = 1 # hard
    number_of_moves = 0

    run = True
    while run:

        printBoard(game_board)

        player_move = int(input('move: '))

        if is_on_game_board(player_move) and is_open(game_board, player_move):
            game_board[player_move] = 'x'
            number_of_moves += 1
        else:
            print('Invalid move!')
            continue

        result, character = win(game_board)
        if end(game_board, result, character, difficulty, number_of_moves):
            break

        game_board_copy = copy.copy(game_board)
        game_board[ai(game_board_copy, difficulty)] = 'o'
        number_of_moves += 1

        result, character = win(game_board)
        if end(game_board, result, character, difficulty, number_of_moves):
            break
    # main()


if __name__ == '__main__':
    main()
