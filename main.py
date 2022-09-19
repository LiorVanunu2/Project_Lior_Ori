import Screen
import pygame
import consts
import time
import MineField

def main():
    run_game = True
    pygame.init()
    Screen.place_x_grass()
    Screen.place_y_grass()
    MineField.mine_list_x()
    MineField.mine_list_y()
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
                    # time.sleep(10)
                else: pass
        Screen.init_screen()





if __name__ == '__main__':
    main()
