import pygame
import sys

pygame.init()
size = width, height = 450, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tic-Tac-Toe')

# fill board with color
screen.fill((0, 255, 255))

# board
board = [['x', ' ', ' '], [' ', 'o', ' '], ['x', ' ', ' ']]

# images
x_img = pygame.transform.scale(pygame.image.load("./img/x.png"), (50, 50))
o_img = pygame.transform.scale(pygame.image.load("./img/o.png"), (50, 50))

rect = x_img.get_rect()
rect = rect.move((150, 150))
screen.blit(x_img, rect)

rect = x_img.get_rect()
rect = rect.move((200, 200))
screen.blit(x_img, rect)

rect = o_img.get_rect()
rect = rect.move((250, 250))
screen.blit(o_img, rect)


def draw_board(board):

    BLACK = (0, 0, 0)

    top = width//len(board)
    bottom = width - top

    # drawing vertical lines
    pygame.draw.line(screen, BLACK, (200, top), (200, bottom), 3)
    pygame.draw.line(screen, BLACK, (250, top), (250, bottom), 3)

    # drawing horizontal lines
    pygame.draw.line(screen, BLACK, (top, 200), (bottom, 200), 3)
    pygame.draw.line(screen, BLACK, (top, 250), (bottom, 250), 3)

    pygame.display.flip()


# math for board size
number_of_squares = len(board)
square_dimentions = (width - 300) // number_of_squares
print(square_dimentions)

color = (250, 250, 250)

draw_board(board)

# test
# pygame.draw.rect(screen,color,(150,150,square_dimentions,square_dimentions))

# pygame.draw.rect(screen,color,(200,200,square_dimentions,square_dimentions))

# pygame.draw.rect(screen,color,(250,250,square_dimentions,square_dimentions))

# font = pygame.font.SysFont(None, 75//5)

# img = font.render(str(5), True, (0, 0, 0))
# screen.blit(img, ((3*(150//5))+20, (3*(150//5))+20))

# pygame.display.flip()

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
