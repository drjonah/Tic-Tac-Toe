from itertools import chain
import copy
from math import inf

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
    moves = []

    for open_space in na:

        print('\n')
        print('start @ index ', open_space)

        # put ai in empty space
        board[open_space] = 'o'
        printBoard(normalBoard(board))

        # find best move
        move = minimax(board, open_space, len(na), False)  # return -1,0,1
        print(move)

        # if move is 1 it is winning
        if move == 1:
            moves.append(open_space)

        try:
            print('ai move @ index ', open_space)
        except:
            print('ai move @ index infinity')
        
        printBoard(normalBoard(board))

        # resets board
        board[open_space] = ' '

        print()

    return max(moves)


def minimax(board, position, depth, maximizingPlayer):

    if depth == 0 or isFull(board):
        return 0

    game_over, winning_character = win(board)

    if game_over and winning_character == 'o':
        return 1

    if game_over and winning_character == 'x':
        return -1

    # computer
    if maximizingPlayer:
        maxEval = -inf
        board[position] = 'o'

        for pos in notOccupied(board):

            eval = minimax(board, pos, depth-1, False)
            maxEval = max(maxEval, eval)

        return maxEval

    # player
    else:
        minEval = inf
        board[position] = 'x'

        for pos in notOccupied(board):
            eval = minimax(board, pos, depth-1, True)
            minEval = min(minEval, eval)

        return minEval


# v5
def backtrack(board):

    game_is_over, winning_character = win(board)

    if game_is_over and winning_character == 'o':
        return 1

    if isFull(board):
        return 0

    if game_is_over and winning_character == 'x':
        return -1

    original_board = copy.deepcopy(board)
    open_space_list = notOccupied(board)

    for open_space in open_space_list:

        if len(open_space_list) % 2 == 0:
            character = 'o'
        else:
            character = 'x'

        board = copy.deepcopy(original_board)
        board[open_space] = character

        score = backtrack(board)

        if score == 1:
            return 1


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
    print('\nbest move @ index', move)

    # print result
    # printBoard(normalBoard(move))

    # input()


if __name__ == '__main__':
    main()
