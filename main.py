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
    soldier_rect = soldier.get_rect()
    Screen.put_soldier()

    while run_game:

        consts.FPS_CLOCK.tick(consts.FPS)
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Screen.draw_grid_background(soldier)
                    time.sleep(consts.SHOW_MATRIX)
            keys_pressed = pygame.key.get_pressed()
            Soldier.soldier_movement(keys_pressed, soldier_rect)
            def return_soldier():
                return soldier

            # else: pass
        Soldier.show_soldier(soldier, soldier_rect)
        Screen.init_screen()


if __name__ == '__main__':
    main()
