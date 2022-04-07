import pygame
import sys

pygame.init()
size = width, height = 450, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

# fill board with color
screen.fill((175, 203, 255))

# board
game_board = ['x', 'x', 'o', 'x', 'o', ' ', ' ', ' ', ' ']


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

    pygame.display.flip()


def draw_squares(game_board):
    color = (215, 249, 255)

    for x in range(len(game_board)//3):

        for y in range(len(game_board)//3):

            pygame.draw.rect(screen, color, pygame.Rect(150 + (x*50), 150 + (y*50), 47, 47))
            pygame.display.flip()


# math for board size
number_of_squares = len(game_board)
square_dimentions = (width - 300) // number_of_squares
print(square_dimentions)

draw_lines(game_board)
draw_squares(game_board)


# main game loop
run = True
while run:
    # game event loop
    for event in pygame.event.get():
        # used in quiting game
        if event.type == pygame.QUIT:
            sys.exit()

    # updates game
    pygame.display.flip()
