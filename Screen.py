import pygame

# Set the size of each cell in the screen
size = 20
black_color = (10, 10, 10)
grid_color = (40, 40, 40)


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


pygame.init()
# Set the screen size
num_cols, num_rows = 50, 25
screen = pygame.display.set_mode((num_cols * size, num_rows * size))
screen.fill(grid_color)
pygame.display.flip()
pygame.display.update()
current_generation_matrix = [[0 for x in range(num_cols)] for y in
                             range(num_rows)]
fill_colors(current_generation_matrix, screen, size)
while True:
    # Wait for events
    for event in pygame.event.get():
        # if user wants to QUIT, close pygame
        if event.type == pygame.QUIT:
            pygame.quit()

