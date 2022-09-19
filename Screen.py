import pygame
import time
import os
import Soldier
import consts
import random
import MineField

screen = pygame.display.set_mode((consts.NUM_COL * consts.SIZE, consts.NUM_ROW * consts.SIZE))
dic_list_xy = {}


def put_flag():
    flag_image = pygame.image.load(os.path.join("Pictures", consts.FLAG_IMAGE))
    flag = pygame.transform.scale(flag_image, consts.FLAG_SIZE)
    screen.blit(flag, consts.FLAG_START)


def put_soldier():
    soldier_image = pygame.image.load(os.path.join("Pictures", consts.SOLDIER_IMAGE))
    soldier = pygame.transform.scale(soldier_image, consts.SOLDIER_SIZE)
    screen.blit(soldier, consts.SOLDIER_START)


# Set the size of each cell in the screen
def place_x_grass():
    """

    :return: a list of random x places for grass
    """
    list_x = []
    for i in range(20):
        ran_num = random.randint(0, consts.NUM_COL * 20 - 1 - consts.GRASS_SIZE[0])
        list_x.append(ran_num)
    dic_list_xy['list_x'] = list_x


def place_y_grass():
    """

    :return: a list of random y places for grass
    """
    list_Y = []
    for i in range(20):
        ran_num = random.randint(0, consts.NUM_ROW * 20 - 1 - consts.GRASS_SIZE[1])
        list_Y.append(ran_num)
    dic_list_xy['list_y'] = list_Y


def put_grass():
    """
    put the grass in random place on screen
    :return: null
    """
    list_x = dic_list_xy['list_x']
    list_y = dic_list_xy['list_y']

    for i in range(20):
        grass_image = pygame.image.load(os.path.join("Pictures", consts.GRASS_IMAGE))
        grass = pygame.transform.scale(grass_image, consts.GRASS_SIZE)
        screen.blit(grass, (list_x[i], list_y[i]))


def put_mine():
    """
    take the mine picture and put in the screen 20 times in random place.
    :return: null
    """
    list_x = MineField.dic_list_xy_mine['list_x']
    list_y = MineField.dic_list_xy_mine['list_y']
    for i in range(20):
        mine_image = pygame.image.load(os.path.join("Pictures", consts.MINE_IMAGE))
        mine = pygame.transform.scale(mine_image, consts.MINE_SIZE)
        screen.blit(mine, (list_x[i], list_y[i]))


def create_background_matrix(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            color = consts.BLACK_COLOR
            pygame.draw.rect(screen, color,
                             (j * size, i * size, size - 1, size - 1))
    #         להוסיף קריאה לפונקציה ליצירת מוקשים וגם פונקציה להראות את החייל
    pygame.display.update()
    put_flag()
    put_soldier()
    put_mine()
    pygame.display.update()


def draw_grid_background():
    pygame.display.flip()
    pygame.display.update()
    # Create zeros matrix
    matrix = [[0 for x in range(consts.NUM_COL)] for y in range(consts.NUM_ROW)]
    MineField.create_background_matrix(matrix, screen, consts.SIZE)


pygame.init()
# Set the screen size
num_cols, num_rows = 50, 25
screen.fill(consts.GRID_COLOR)
pygame.display.flip()
pygame.display.update()
background_matrix = [[0 for x in range(num_cols)] for y in
                     range(num_rows)]


def init_screen():
    screen.fill(consts.GREEN_COLOR)
    put_flag()
    put_soldier()
    put_grass()
    pygame.display.update()
