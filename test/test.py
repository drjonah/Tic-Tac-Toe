from src.ai import *

def get_boards():
    board1 = [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ']
    board2 = [' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    board3 = ['o', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ']
    board4 = ['o', 'x', 'x', 'o', ' ', ' ', 'x', ' ', ' ']
    board5 = ['x', 'x', 'o', 'x', 'o', ' ', ' ', ' ', ' ']

    return board1 + board2 + board3 + board4 + board5

def run():
    print(get_boards())

if __name__ == '__main__':
    run()