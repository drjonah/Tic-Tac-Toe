import datetime

# AI API
def not_occupied(board: list) -> list:
    """Checks to see which spaces on the board are no occupied

    Args:
        board (list): Game board for Tic-Tac-Toe 

    Returns:
        list: A list of all available positions on the game board
    """

    return [i for i in range(len(board)) if board[i] == ' ']

def is_full(board: list) -> bool:
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

# TERMINAL API
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

def printBoard(board: list) -> None:
    """Prints the board in a fancy way

    Args:
        board (list): Game board for Tic-Tac-Toe
    """
    for i in range(3):

        print(f' {board[(i*3)]} | {board[(i*3)+1]} | {board[(i*3)+2]}')

        if (i < 2):
            print("--- --- ---")

# GUI API
def find_game_board_space(game_board, x, y):
    for square in game_board:
        if (x <= square[1] <= x+50 and y <= square[2] <= y+50):
            return game_board.index(square)

def convert_game_board(game_board):
    new_board = []

    for square in game_board:
        new_board.append(square[0])

    return new_board


# UNIVERSAL API
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

    return False, None

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
    elif is_full(game_board):
        print('Tie!')
        printBoard(game_board)
        store_games(game_board, difficulty, number_of_moves, character)
        return True
    return False

def store_games(game_board, difficulty, number_of_moves, winner):
    TIME_STAMP = str(datetime.datetime.now())
    FILE_NAME = ('-').join(TIME_STAMP.split('.')[0].split(':'))

    try:
        with open(f'./logs/{FILE_NAME}.txt', 'w') as FILE:

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
                    FILE.write("--- --- ---\n")

        print('Game stored.')

    except:
        print('Game saving failed.')