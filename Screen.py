import pygame
import time
import os
import Soldier
import consts


def put_flag():
    flag_image = pygame.image.load(os.path.join("Pictures", consts.FLAG_IMAGE))
    screen.blit(flag_image, consts.FLAG_START)
    pygame.display.update()


# Set the size of each cell in the screen
size = 20
black_color = (10, 10, 10)
grid_color = (40, 40, 40)
green_color = (61, 145, 64)


def create_background_matrix(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            color = black_color
            pygame.draw.rect(screen, color,
                             (j * size, i * size, size - 1, size - 1))
    pygame.display.update()


def set_regular_background_color(color):
    screen.fill(color)
    pygame.display.flip()


pygame.init()
# Set the screen size
num_cols, num_rows = 50, 25
screen = pygame.display.set_mode((num_cols * size, num_rows * size))
screen.fill(grid_color)
pygame.display.flip()
pygame.display.update()
background_matrix = [[0 for x in range(num_cols)] for y in
                     range(num_rows)]
while True:
    # Wait for events
    for event in pygame.event.get():
        set_regular_background_color(green_color)
        # if user wants to QUIT, close pygame
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                create_background_matrix(background_matrix, screen, size)

def init_screen ():
    pygame.init()
    num_cols, num_rows = 50, 25
    screen = pygame.display.set_mode((num_cols * size, num_rows * size))
    screen.fill(grid_color)
    pygame.display.flip()
    pygame.display.update()
    background_matrix = [[0 for x in range(num_cols)] for y in
                         range(num_rows)]
    set_regular_background_color(green_color)
    put_flag()




