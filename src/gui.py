from tkinter import font
import pygame
import sys
from ai import *
from api.api import *

# pygame 
pygame.init()
size = width, height = 450, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

# fill board with color
screen.fill((175, 203, 255))

# font
font = pygame.font.Font('freesansbold.ttf', 32)

# x
player_x_image = pygame.image.load('./src/img/x.png')
player_x_image = pygame.transform.scale(player_x_image, (50, 50))
# y
computer_o_image = pygame.image.load('./src/img/o.png')
computer_o_image = pygame.transform.scale(computer_o_image, (50, 50))


def draw_lines(game_board):

    BLACK = (0, 0, 0)

    top = width//(len(game_board)//3)
    bottom = width - top

    # drawing vertical lines
    pygame.draw.line(screen, BLACK, (200, top), (200, bottom), 3)
    pygame.draw.line(screen, BLACK, (250, top), (250, bottom), 3)

    # drawing horizontal lines
    pygame.draw.line(screen, BLACK, (top, 200), (bottom, 200), 3)
    pygame.draw.line(screen, BLACK, (top, 250), (bottom, 250), 3)


def draw_squares(game_board):
    color = (215, 249, 255)

    for x in range(len(game_board)//3):

        for y in range(len(game_board)//3):

            # drawing tiles
            pygame.draw.rect(screen, color, pygame.Rect(
                150 + (x*50), 150 + (y*50), 50, 50))


def draw_title():

    text = font.render('Tic Tac Toe', True, (0, 0, 0), None)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 4)

    # drawing tite
    screen.blit(text, textRect)


def draw_characters(game_board):
    for square in game_board:
        if square[0] != ' ':
            if square[0] == 'x':
                screen.blit(player_x_image, (square[1], square[2]))
            else:
                screen.blit(computer_o_image, (square[1], square[2]))


def draw(game_board):
    draw_squares(game_board)
    draw_lines(game_board)
    draw_title()
    draw_characters(game_board)
    pygame.display.flip()


def run_gui(difficulty):

    # board
    game_board = [
        [' ', 150, 150],
        [' ', 200, 150],
        [' ', 250, 150],
        [' ', 150, 200],
        [' ', 200, 200],
        [' ', 250, 200],
        [' ', 150, 250],
        [' ', 200, 250],
        [' ', 250, 250]
    ]

    number_of_moves = 0

    # main game loop
    run = True
    while run:
        # mouse position
        mouse = pygame.mouse.get_pos()
        # print(mouse)

        # drawing board
        draw(game_board)

        # game event loop
        for event in pygame.event.get():
            # used in quiting game
            if event.type == pygame.QUIT:
                sys.exit()

            # click tiles
            if event.type == pygame.MOUSEBUTTONDOWN:

                for x in range(len(game_board)//3):
                    for y in range(len(game_board)//3):
                        if (150 + (x*50)) <= mouse[0] <= (200 + (x*50)) and (150 + (y*50)) <= mouse[1] <= (200 + (y*50)):
                            pos = find_game_board_space(game_board, 150 + (x*50), 150 + (y*50))
                            game_board[pos][0] = 'x'
                            number_of_moves += 1

        new_board = convert_game_board(game_board)

        result, character = win(new_board)
        if end(new_board, result, character, difficulty, number_of_moves):
            break

        if number_of_moves % 2 != 0:
            computer_move = ai(new_board, difficulty)
            game_board[computer_move][0] = 'o'
            number_of_moves += 1

        result, character = win(new_board)
        if end(new_board, result, character, difficulty, number_of_moves):
            break

if __name__ == '__main__':
    # difficulty = 1 # childs play
    # difficulty = 2 # hard
    difficulty = 3 # impossible
    run_gui(difficulty)