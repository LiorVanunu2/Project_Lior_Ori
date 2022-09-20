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
        soldier_rect.x -= 1
    if keys_pressed[
        pygame.K_RIGHT] and 0 < soldier_rect.x * consts.SOLDIER_STEP + consts.SOLDIER_STEP * 2 < consts.SCREEN_WIDTH:
        soldier_rect.x += 1
    if keys_pressed[
        pygame.K_UP] and 0 < soldier_rect.y * consts.SOLDIER_STEP < consts.SCREEN_HEIGHT:
        soldier_rect.y -= 1
    if keys_pressed[
        pygame.K_DOWN] and 0 < soldier_rect.y * consts.SOLDIER_STEP + consts.SOLDIER_STEP * 4 < consts.SCREEN_HEIGHT:
        soldier_rect.y += 1

    return soldier_rect

# The moveRight() method takes two arguments. The first one is implicit and is called self.
# It refers to the current object. The second one is called pixels and refers to the number of pixels we will use to move the car.
