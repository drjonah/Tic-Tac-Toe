from itertools import chain
import copy
from math import inf
from operator import index

# flat -> 2d


def normalBoard(board):
    newBoard = []

    for i in range(3):
        temp = []
        temp.append(board[i*3:i*3+3])
        newBoard.append(temp[0])

    return newBoard

# 2d -> flat


def flattenBoard(board):
    return list(chain.from_iterable(board))

# see if square is not occupied


def notOccupied(board):
    open = list()

    for i in range(len(board)):
        if board[i] == ' ':
            open.append(i)

    return open


def isFull(board):
    for x in board:
        if x == ' ':
            return False

    return True

# win through a flattened list


def win(board: list) -> tuple:

    for player in ['x', 'o']:

        for i in range(len(board)//3):
            # horizontal
            if (board[i*3] == player and board[(i*3)+1] == player and board[(i*3)+2] == player):
                return True, player
            # vertical
            elif (board[i] == player and board[i+3] == player and board[i+6] == player):
                return True, player

        # diagonal: left to right
        if (board[0] == player and board[4] == player and board[8] == player):
            return True, player
        # diagonal: right to left
        elif (board[2] == player and board[4] == player and board[6] == player):
            return True, player

    return False, str()


def ai(board):
    # open spaces
    na = notOccupied(board)

    # list for winning moves
    # moves[0] = tie
    # moves[1] = win
    moves = [[], []]

    for open_space in na:

        # because we want to revert back to the original board after trying the combinations #
        # original board
        original_board = copy.deepcopy(board)

        # print
        print('\n')
        print('ai move @ index ', open_space)

        # put ai in empty space
        board[open_space] = 'o'

        # find best move
        move = minimax(board, len(na), False)  # return -1,0,1
        print('move score: ', move)

        # when a move is winning we want to save the move to a list #
        # if move is 1 it is winning
        if move == 0:
            moves[0].append(open_space)

        if move == 1:
            moves[1].append(open_space)

        # print
        printBoard(normalBoard(board))

        # because we want to revert back to the original board after trying the combinations #
        # resets board to original board
        board = original_board

        print()

    # idk what to do here lol
    return moves


def minimax(board, depth, maximizingPlayer):

    print()
    printBoard(normalBoard(board))
    print()

    game_over, winning_character = win(board)

    # indicates a tie
    if depth == 0 or isFull(board):
        return 0

    # indicates a win
    if game_over and winning_character == 'o':
        return 1

    # indicates a loss
    if game_over and winning_character == 'x':
        return -1

    # computer is findings its max win
    if maximizingPlayer:
        maxEval = -inf
        computer_board = copy.deepcopy(board)

        for pos in notOccupied(board):
            board[pos] = 'o'
            eval = minimax(board, depth-1, False)
            maxEval = max(maxEval, eval)
            board = computer_board

        return maxEval

    # player is finding its min loss
    else:
        minEval = inf
        player_board = copy.deepcopy(board)

        for pos in notOccupied(board):
            board[pos] = 'x'
            eval = minimax(board, depth-1, True)
            minEval = min(minEval, eval)
            board = player_board

        return minEval


def printBoard(board: list) -> None:
    for i in range(3):
        row = str()

        for j in range(3):

            if (j < 2):
                row += (' ' + board[i][j] + ' |')
            else:
                row += (' ' + board[i][j])

        print(row)

        if (i < 2):
            print("-----------")


def main():
    # board
    # board = [['o', 'o', 'x'], [' ', 'o', ' '], ['x', ' ', ' ']]
    # board = [['o', 'x', 'o'], ['x', 'x', 'o'], [' ', ' ', ' ']]
    # board = [[' ', ' ', ' '], [' ', 'x', ' '], [' ', ' ', ' ']]
    board = [['x', 'x', 'o'], ['x', 'o', ' '], [' ', ' ', ' ']]
    board = flattenBoard(board)

    # backtracking
    print('starting backtracking...')
    move = ai(board)

    for i in move:
        base = ' '
        for j in i:
            base += str(j)
            base += ' '

        if move.index(i) == 0:
            print('ties: ' + base + ' ')
        if move.index(i) == 1:
            print('wins: ' + base + ' ')

    # print result
    # printBoard(normalBoard(move))

    # input()


if __name__ == '__main__':
    main()
