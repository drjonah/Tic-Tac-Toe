import pygame
import sys

pygame.init()
size = width, height = 450, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

# fill board with color
screen.fill((255, 255, 255))

# board 
board = [['x', ' ', ' '], [' ', 'o', ' '], ['x', ' ', ' ']]

def draw_board(board: list):


    pygame.display.flip()

# math for board size
number_of_squares = len(board)
square_dimentions = (width - 150) // number_of_squares
print(square_dimentions)

# test
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen,(0,0,250),(50*(j+1),50*(i+1),square_dimentions,square_dimentions))


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