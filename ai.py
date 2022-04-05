import copy
import random
from math import inf


def notOccupied(board: list) -> list:
    """Checks to see which spaces on the board are no occupied

    Args:
        board (list): Game board for Tic-Tac-Toe 

    Returns:
        list: A list of all available positions on the game board
    """

    return [i for i in range(len(board)) if board[i] == ' ']


def isFull(board: list) -> bool:
    """Checks to see if the board has any empty spaces

    Args:
        board (list): Game board for Tic-Tac-Toe

    Returns:
        bool: True - game board is full, False - game board is NOT full
    """
    for i in board:
        if i == ' ':
            return False
    return True


def win(board: list) -> tuple:
    """Checks to see if someone has won the game and which player won

    Args:
        board (list): Game board for Tic-Tac-Toe

    Returns:
        tuple: (bool, str) - (whether the game has ended [True - finished, False - continue], winning character [IF ANY])
    """

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


def printBoard(board: list) -> None:
    """Prints the board in a fancy way

    Args:
        board (list): Game board for Tic-Tac-Toe
    """
    for i in range(3):

        print(f' {board[(i*3)]} | {board[(i*3)+1]} | {board[(i*3)+2]}')

        if (i < 2):
            print("-----------")


def ai(board):

    open_starting_positions = notOccupied(board)

    # [ [lose], [tie], [win] ]
    moves = [[], [], []]

    for open_space in open_starting_positions:

        original_board = copy.deepcopy(board)

        board[open_space] = 'o'
        move = minimax(board, len(open_starting_positions), False)  # return -1,0,1

        if move == -1:
            moves[0].append(open_space)
        elif move == 0:
            moves[1].append(open_space)
        else:
            moves[2].append(open_space)

        board = original_board


    print('move list: ', moves)
    if len(moves[2]) > 0:
        return moves[2][0]
    elif len(moves[1]) > 0:
        return moves[1][random.randint(0, len(moves[1])-1)]
    else:
        return moves[0][random.randint(0, len(moves[0])-1)]


def minimax(board, depth, maximizingPlayer):

    game_over, winning_character = win(board)

    if depth == 0 or isFull(board): # tie or depth requirement met
        return 0

    if game_over and winning_character == 'o': # win
        return 1

    if game_over and winning_character == 'x': # lose
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


def main():
    # boards
    # board = [['o', 'o', 'x'], [' ', 'o', ' '], ['x', ' ', ' ']]
    # board = [['o', 'x', 'o'], ['x', 'x', 'o'], [' ', ' ', ' ']]
    board = [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ']
    # board = ['x', 'x', 'o', 'x', 'o', ' ', ' ', ' ', ' ']
    # board = flattenBoard(board)

    # backtracking
    print('starting backtracking...')
    move = ai(board)
    print('best move: ', move)

    return move


if __name__ == '__main__':
    main()
