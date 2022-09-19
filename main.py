import Screen
import pygame
import consts
import time
import MineField
import Soldier

def main():
    run_game = True
    pygame.init()
    Screen.place_x_grass()
    Screen.place_y_grass()
    MineField.mine_list_x()
    MineField.mine_list_y()
    Screen.init_screen()
    soldier = Soldier.create_soldier()


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
                elif event.key == pygame.K_RIGHT:
                    Soldier.moveRight(soldier)
                else: pass
        Screen.init_screen()





if __name__ == '__main__':
    main()
