import random
from colorama import Fore

def createBoard() -> list:
    board = list()

    for i in range(3):
        row = list()
        for j in range(3):
            row.append(' ')
        board.append(row)

    return board

def printBoard(board: list) -> None:
    for i in range(3):
        row = str()

        for j in range(3):

            if (j < 2): row += (' ' + board[i][j] + ' |')
            else: row += (' ' + board[i][j])

        print(row)

        if (i < 2): print("-----------")

def move(board: list, move: str) -> list:
    
    try:
        row, col = move.split(',')
    except:
        print('Invalid move')
        return board

    if (validateMove(board, int(row), int(col))):
        board[int(row)][int(col)] = 'x'
        return board
    else:
        print('Invalid move')
        return board

def full(board: list) -> bool:
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ': return False
        
    return True

def validateMove(board: list, row: int, col: int) -> bool:
    # on the board
    if (row < 0 or col < 0 or row > 2 or col > 2): return False
    # not taken
    elif (board[row][col] != ' '): return False

    return True

def win(board: list) -> tuple:

    for player in ['x', 'o']:

        for i in range(3):
            # verticle
            if (board[i][0] == player and board[i][1] == player and board[i][2] == player): return True, player
            # horizontal
            elif (board[0][i] == player and board[1][i] == player and board[2][i] == player): return True, player
        # diagonal: left to right
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player): return True, player
        # diagonal: right to left
        elif (board[0][2] == player and board[1][1] == player and board[2][0] == player): return True, player

    return False, str()

def computer(board) -> list:
    
    if (full(board)): return board

    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)

        if (validateMove(board, row, col)): 
            board[int(row)][int(col)] = 'o'
            break
    
    print(f'Computer {row},{col}')
    return board

def main():
    board = createBoard()

    while True:
        printBoard(board)

        # player
        playerMove = str(input('Move (0,1,2): '))
        board = move(board, playerMove)

        # computer
        board = computer(board)

        isWon, winner = win(board)
        if (isWon or full(board)):
            printBoard(board)
            print(f'{winner} wins')
            break

if __name__ == '__main__':
    main()