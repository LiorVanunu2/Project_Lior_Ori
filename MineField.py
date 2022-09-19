import consts
import pygame
def create_background_matrix(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            color = consts.BLACK_COLOR
            pygame.draw.rect(screen, color,
                             (j * size, i * size, size - 1, size - 1))
    pygame.display.update()