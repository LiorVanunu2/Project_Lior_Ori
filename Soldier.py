import Screen
import pygame
import consts

IMAGE = 'grass.png'
img = pygame.image.load(IMAGE)
Screen.blit(img, (0, 0))
pygame.display.flip()

soldier_img = pygame.image.load("C:\\Users\\pc\\Desktop\\lior_ori\\Project_Lior_Ori\\Pictures\\soldier.png").convert()
Screen.screen.blit(soldier_img, [5, 8])
pygame.display.flip()
