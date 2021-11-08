import pygame
class Field:
    def __init__(self):
        self.x_tile_count = 15
        self.y_tile_count = 10
        self.wall_field = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                           [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                           [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    def is_wall(self, x, y):
        if self.wall_field[y][x]:
            return True
        else:
            return False
    
    def draw(self, screen, top_left_x, top_left_y, tile_size):
        empty_tile_color = (0, 0, 0)
        wall_tile_color = (0, 0, 255)
        for i in range(self.y_tile_count):
            for j in range(self.x_tile_count):
                draw_color = empty_tile_color
                if self.wall_field[i][j] == 1:
                    draw_color = wall_tile_color
                pygame.draw.rect(screen, draw_color, (j*tile_size + top_left_x, i*tile_size + top_left_y, tile_size, tile_size))
