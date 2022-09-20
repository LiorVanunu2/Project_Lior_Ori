import Screen
import pygame
import os
import consts
import time


def create_soldier():
    soldier_image = pygame.image.load(
            os.path.join("Pictures", consts.SOLDIER_IMAGE))
    soldier = pygame.transform.scale(soldier_image, consts.SOLDIER_SIZE)
    return soldier


def soldier_movement(keys_pressed, soldier_rect):
    if keys_pressed[
        pygame.K_LEFT] and 0 < soldier_rect.x * consts.SOLDIER_STEP < consts.SCREEN_WIDTH:
        soldier_rect.x -= consts.SOLDIER_STEP * consts.SIZE
    if keys_pressed[
        pygame.K_RIGHT] and 0 < soldier_rect.x * consts.SOLDIER_STEP + consts.SIZE * 2 < consts.SCREEN_WIDTH:
        soldier_rect.x += consts.SOLDIER_STEP * consts.SIZE
    if keys_pressed[
        pygame.K_UP] and 0 < soldier_rect.y * consts.SOLDIER_STEP < consts.SCREEN_HEIGHT:
        soldier_rect.y -= consts.SOLDIER_STEP * consts.SIZE
    if keys_pressed[
        pygame.K_DOWN] and 0 < soldier_rect.y * consts.SOLDIER_STEP + consts.SIZE * 4 < consts.SCREEN_HEIGHT:
        soldier_rect.y += consts.SOLDIER_STEP * consts.SIZE
    Screen.screen.blit(create_soldier(),
                       (soldier_rect.x, soldier_rect.y))
    pygame.display.flip()
    pygame.display.update()


# The moveRight() method takes two arguments. The first one is implicit and is called self.
# It refers to the current object. The second one is called pixels and refers to the number of pixels we will use to move the car.
def show_soldier(soldier, soldier_rect):
    Screen.screen.blit(soldier,
                       (soldier_rect.x, soldier_rect.y))
    pygame.display.flip()
    pygame.display.update()


def calculate_legs_index(soldier, soldier_rect):
    legs_index_list = []
    legs_list = []
    for num in range(2):
        j = soldier_rect.x / consts.SIZE
        i = soldier_rect.y / consts.SIZE
        legs_list.append(j)

    pass
