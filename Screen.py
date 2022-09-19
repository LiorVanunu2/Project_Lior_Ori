import pygame
import time
import os
import Soldier
import consts

screen = pygame.display.set_mode((consts.NUM_COL * consts.SIZE, consts.NUM_ROW * consts.SIZE))
def put_flag():
    flag_image = pygame.image.load(os.path.join("Pictures", consts.FLAG_IMAGE))
    flag = pygame.transform.scale(flag_image, consts.FLAG_SIZE)
    screen.blit(flag, consts.FLAG_START)

def put_soldier():
    soldier_image=pygame.image.load(os.path.join("Pictures", consts.SOLDIER_IMAGE))
    soldier=pygame.transform.scale(soldier_image, consts.SOLDIER_SIZE)
    screen.blit(soldier, consts.SOLDIER_START)

# Set the size of each cell in the screen



def create_background_matrix(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            color = consts.BLACK_COLOR
            pygame.draw.rect(screen, color,
                             (j * size, i * size, size - 1, size - 1))
    # להוסיף קריאה לפונקציה ליצירת מוקשים וגם פונקציה להראות את החייל
    put_flag()
    put_soldier()
    pygame.display.update()

def draw_grid_background():
    pygame.display.flip()
    pygame.display.update()
    # Create zeros matrix
    matrix = [[0 for x in range(consts.NUM_COL)] for y in range(consts.NUM_ROW)]
    create_background_matrix(matrix, screen, consts.SIZE)



# def set_regular_background_color():
#     screen.fill(consts.GREEN_COLOR)
#     pygame.display.flip()


pygame.init()
# Set the screen size
num_cols, num_rows = 50, 25
screen.fill(consts.GRID_COLOR)
pygame.display.flip()
pygame.display.update()
background_matrix = [[0 for x in range(num_cols)] for y in
                     range(num_rows)]
# while True:
#     # Wait for events
#     for event in pygame.event.get():
#         set_regular_background_color(green_color)
#         # if user wants to QUIT, close pygame
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 create_background_matrix(background_matrix, screen, size)

def init_screen ():
    screen.fill(consts.GREEN_COLOR)
    put_flag()
    put_soldier()
    pygame.display.update()




