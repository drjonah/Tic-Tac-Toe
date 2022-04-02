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
    board = board[0] + board[1] + board[2]
    return board

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

# v3
def backtrack3(board, openSpaces):

    if len(openSpaces) == 0:
        return True

    for space in openSpaces:

        if len(openSpaces) % 2 == 0:
            player = 'o'
        else:
            player = 'x'

        board[space] = player

        result, winner = win(normalBoard(board))

        if result and winner == 'o':
            # winning board, return index
            if backtrack3(board, notOccupied(board)):
                return True

        if not result and winner == 'x':
            # losing board, go to previous level
            board[space] = ' '

    return False


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


board = [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board = flattenBoard(board)

if backtrack3(board, notOccupied(board)):

    printBoard(normalBoard(board))
