import Screen
import pygame
import os
import consts


# The moveRight() method takes two arguments. The first one is implicit and is called self.
# It refers to the current object. The second one is called pixels and refers to the number of pixels we will use to move the car.
def moveRight(soldier):
    soldier.rect.x += consts.SIZE

    # self.rect.x += consts.size


def moveLeft(self):
    self.rect.x -= consts.SIZE


def moveUp(self):
    self.rect.y += consts.SIZE


def moveDown(self):
    self.rect.y -= consts.SIZE

def create_soldier():
    soldier_image = pygame.image.load(os.path.join("Pictures", consts.SOLDIER_IMAGE))
    soldier = pygame.transform.scale(soldier_image, consts.SOLDIER_SIZE)
    return soldier


