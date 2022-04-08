import copy
import random
from math import inf
from api.api import *


def ai(board, difficulty):

    # available positions from the start
    open_starting_positions = not_occupied(board)
    open_starting_positions_length = len(open_starting_positions)

    # managging depth
    if difficulty == 1:
        depth = open_starting_positions_length//9
    elif difficulty == 2:
        depth = open_starting_positions_length//6
    else:
        depth = open_starting_positions_length

    # [ [lose], [tie], [win] ]
    moves = [[], [], []]

    if open_starting_positions_length == 9:
        moves[2].append(4)
        return moves

    # analyzing positions
    for open_space in open_starting_positions:

        original_board = copy.deepcopy(board)

        board[open_space] = 'o'
        move = minimax(board, depth, False)  # return -1,0,1

        if move == -1:
            moves[0].append(open_space)
        elif move == 0:
            moves[1].append(open_space)
        else:
            moves[2].append(open_space)

        board = original_board

    print(f'AI [{difficulty}]: {moves}')
    if len(moves[2]) > 0:
        return moves[2][0]
    elif len(moves[1]) > 0:
        return moves[1][random.randint(0, len(moves[1])-1)]
    else:
        return moves[0][random.randint(0, len(moves[0])-1)]


def minimax(board, depth, maximizingPlayer):

    game_over, winning_character = win(board)

    if game_over and winning_character == 'o':  # win
        return 1

    if game_over and winning_character == 'x':  # lose
        return -1

    if depth == 0 or is_full(board):  # tie or depth requirement met
        return 0

    # computer is findings its max win
    if maximizingPlayer:
        max_num = -inf

        for pos in not_occupied(board):
            board[pos] = 'o'
            num = minimax(board, depth-1, False)
            max_num = max(max_num, num)
            board[pos] = ' '

        return max_num

    # player is finding its min loss
    else:
        min_num = inf

        for pos in not_occupied(board):
            board[pos] = 'x'
            num = minimax(board, depth-1, True)
            min_num = min(min_num, num)
            board[pos] = ' '

        return min_num


def main():
    # Board Examples
    # board = [['o', 'o', 'x'], [' ', 'o', ' '], ['x', ' ', ' ']]
    # board = [['o', 'x', 'o'], ['x', 'x', 'o'], [' ', ' ', ' ']]
    board = [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ']
    # board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # board = [' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # board = ['o', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ']
    # board = ['o', 'x', 'x', 'o', ' ', ' ', 'x', ' ', ' ']
    # board = ['x', 'x', 'o', 'x', 'o', ' ', ' ', ' ', ' ']
    # board = flattenBoard(board)

    # backtracking
    print('Tic Tac Toe Board')
    printBoard(board)
    print('\nStarting Alex...')
    print()
    test_board = copy.deepcopy(board)
    move = ai(test_board, 3)
    print('Alex\'s move: ', move)

    input('\npress enter to quit...')


if __name__ == '__main__':
    main()
