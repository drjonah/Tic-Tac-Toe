import copy
import os
from ai import *
from api.api import *

def run_cli(difficulty):
    os.system('cls')
    print('IMPOSSIBLE TIC TAC TOE')

    # game board
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # constant
    number_of_moves = 0

    run = True
    while run:

        printBoard(game_board)

        player_move = int(input('[YOU] move: '))

        if is_on_game_board(player_move) and is_open(game_board, player_move):
            game_board[player_move] = 'x'
            number_of_moves += 1
        else:
            print('Invalid move!')
            continue

        result, character = win(game_board)
        if end(game_board, result, character, difficulty, number_of_moves):
            input('\npress enter to quit...')
            break

        game_board_copy = copy.copy(game_board)
        computer_move = ai(game_board_copy, difficulty)
        game_board[computer_move] = 'o'
        print(f'[AI] move: {computer_move}')
        number_of_moves += 1

        result, character = win(game_board)
        if end(game_board, result, character, difficulty, number_of_moves):
            input('\npress enter to quit...')
            break

if __name__ == '__main__':
    # difficulty = 1 # childs play
    # difficulty = 2 # hard
    difficulty = 3 # impossible
    run_cli(difficulty)