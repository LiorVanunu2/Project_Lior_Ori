import pygame

# Set the size of each cell in the screen
size = 10

# set colors
black_color = (10, 10, 10)
grid_color = (40, 40, 40)


# DEAD_CELL = 0


# Update screen colors by the recieved matrix. Cell with '0' value will be black, otherwise white.
def fill_colors(matrix, screen, size):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # run over all the cells in the current matrix
    for i in range(num_rows):
        for j in range(num_cols):
            color = black_color
            pygame.draw.rect(screen, color,
                             (j * size, i * size, size - 1, size - 1))
    pygame.display.update()


# Main function
def main():
    # Initial pygame
    pygame.init()
    # Set the screen size
    num_cols, num_rows = 50, 25
    screen = pygame.display.set_mode((num_cols * size, num_rows * size))
    screen.fill(grid_color)
    pygame.display.flip()
    pygame.display.update()
    # running = False
    # Create zeros matrix
    current_generation_matrix = [[0 for x in range(num_cols)] for y in
                                 range(num_rows)]
    fill_colors(current_generation_matrix, screen, size)

    while True:
        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return

                # # pygame.draw.rect(screen, alive_color, ((position[0] // size) * size, (position[1] // size) * size, size - 1, size - 1))
                # fill_colors(current_generation_matrix, screen, size)
                # pygame.display.update()

        # if running:
        #     next_generation_matrix = next_generation(current_generation_matrix)
        #     current_generation_matrix = next_generation_matrix
        #     fill_colors(current_generation_matrix, screen, size)


if __name__ == '__main__':
    main()
