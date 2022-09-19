import Screen
import pygame
import consts
import time

def main():
    run_game = True
    pygame.init()
    Screen.init_screen()
    while run_game:
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Screen.draw_grid_background()
                    time.sleep(consts.SHOW_MATRIX)
                else: pass
        Screen.init_screen()



if __name__ == '__main__':
    main()
