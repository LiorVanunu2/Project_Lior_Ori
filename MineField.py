import consts
import Screen
import pygame
import os
import random

dic_list_xy_mine = {}


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
    Screen.put_flag()
    Screen.put_soldier()
    Screen.put_mine()
    pygame.display.update()


# def create_mine():
#     mine_image = pygame.image.load(os.path.join("Pictures", consts.MINE_IMAGE))
#     mine = pygame.transform.scale(mine_image, consts.MINE_SIZE)
#     return mine

def mine_list_x():
    """

    :return: list of x places for Mine
    """
    list_x = []
    for i in range(20):
        ran_num = random.randint(0, consts.NUM_COL * 20 - 1 - consts.MINE_SIZE[0])
        list_x.append(ran_num)
    dic_list_xy_mine['list_x'] = list_x


def mine_list_y():
    """

    :return: list os y places for mine
    """
    list_y = []
    for i in range(20):
        ran_num = random.randint(0, consts.NUM_COL * 20 - 1 - consts.MINE_SIZE[1])
        list_y.append(ran_num)
    dic_list_xy_mine['list_y'] = list_y
