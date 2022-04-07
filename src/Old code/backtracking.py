from itertools import chain
import copy

class Board:
    def __init__(self, board) -> None:
        self.emptySpace = board

    def getEmptySpaces(self):
        return self.emptySpace

    def removeSpace(self, i):
        del self.emptySpace[i]

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

# win through normal board
def win(board: list) -> tuple:

    for player in ['x', 'o']:

        for i in range(3):
            # verticle
            if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
                return True, player
            # horizontal
            elif (board[0][i] == player and board[1][i] == player and board[2][i] == player):
                return True, player
        # diagonal: left to right
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
            return True, player
        # diagonal: right to left
        elif (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return True, player

    return False, str()

# win through a flattened list
def win2(board: list) -> tuple:

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

# see if square is not occupied
def notOccupied(board):
    open = list()

    for i in range(len(board)):
        if board[i] == ' ':
            open.append(i)

    return open

# v1
def backtrack(board, index):

    # find way that if nothing works for initial index to restart everything at the next index
    # find way to return index and convert to board quardenates
    # find way to alternate

    # potential just alternate places until found

    if index == len(board):
        return (board, True)

    winner, result = win(normalBoard(board))

    if winner:
        return (board, True)

    # open = openSpaces(board, index)
    print(open)

    for num in open:
        for character in ['o', 'x']:
            board[index] = character

            board, valid = backtrack(board, num)

            if valid:
                return (board, True)

    return (board, False)

# v2
def backtrack2(board, openSpaces):

    if len(openSpaces) == 0:
        return board

    for space in openSpaces:

        if len(openSpaces) % 2 == 0:
            player = 'o'
        else:
            player = 'x'

        board[space] = player

        result, winner = win(normalBoard(board))

        if result and winner == 'o':
            # winning board, return index
            return space

        if not result and winner == 'x':
            # losing board, go to previous level
            pass

        return backtrack2(board, notOccupied(board))

    return board

def isFull(board):
    for x in board:
        if x == ' ':
            return False

    return True

# v3
def backtrack3(board, openSpaces):

    # no more spaces on the board
    # check win and return the condition
    if isFull(board):
        
        game_is_over, winning_character = win2(board)
        # board is full
        if not game_is_over:
            return (False, -1)

    for starting_pos in openSpaces:
        print(starting_pos)

        # computer only plays on even number of spaces left (8, 6, 4, 2)
        if len(openSpaces) % 2 == 0:
            character = 'o'
        else:
            character = 'x'

        board[starting_pos] = character

        game_is_over, winning_character = win2(board)
        # if game_is_over and winning_character == 'x':
        #     return (False, -1)

        # this means that computer has a winning position so that position is returned
        if game_is_over and winning_character == 'o':
            return (True, starting_pos)

        else:
            return backtrack3(board, notOccupied(board))

    return (False, -1)
    
# v4
def backtrack4(board, openSpaces, starting=0):

    # no more spaces on the board
    # check win and return the condition
    game_is_over, winning_character = win2(board)

    if game_is_over and winning_character == 'o':
        printBoard(normalBoard(board))
        print()
        return (True, openSpaces[starting])

    if isFull(board):
        # board is full
        if not game_is_over:
            return (False, -1)

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

        game_is_over, winning_character = backtrack4(board, notOccupied(board), starting)

        if game_is_over:
            return (True, starting_pos)

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


board = [['x', ' ', ' '], ['o', 'o', ' '], ['x', ' ', ' ']]
board = flattenBoard(board)

b = Board(notOccupied(board))

is_win, starting_pos = backtrack4(board, notOccupied(board))
printBoard(normalBoard(board))
print(is_win, starting_pos)
