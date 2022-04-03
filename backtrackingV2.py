from itertools import chain
import copy

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
    
# v4
def backtrack(board, openSpaces, starting=0):

    # no more spaces on the board
    # check win and return the condition
    game_is_over, winning_character = win(board)

    if game_is_over and winning_character == 'o':
        printBoard(normalBoard(board))
        print()
        return (True, openSpaces[starting])

    if isFull(board):
        # tie game - go back to next position but return starting point
        if not game_is_over:
            return (False, 0)

    original_board = copy.deepcopy(board)

    for starting_pos in openSpaces:

        # computer only plays on even number of spaces left (8, 6, 4, 2)
        if len(openSpaces) % 2 == 0:
            character = 'o'
        else:
            character = 'x'

        board = copy.deepcopy(original_board)

        printBoard(normalBoard(board))
        print()
        board[starting_pos] = character

        game_is_over, winning_pos = backtrack(board, notOccupied(board), starting)

        # win - return first move
        if game_is_over:
            return (True, starting_pos)

        # lose - go back to next starting position
        if not game_is_over and winning_pos == -1:
            continue

    return (False, -1)

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

# board
board = [['x', ' ', ' '], ['o', 'o', ' '], ['x', ' ', ' ']]
board = flattenBoard(board)

# backtracking
is_win, starting_pos = backtrack(board, notOccupied(board))

# print result
print(is_win, starting_pos)
