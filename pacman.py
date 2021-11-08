import pygame

class Pacman:
    def __init__(self, field, start_x, start_y):
        self.field = field
        self.x = start_x
        self.y = start_y
        
        self.current_direction = "up"
        self.next_direction = "up"
        
        self.update_interval = 5
        self.frames_since_last_update = 0
        
        self.buffer_turn = 0
        
    def move_in_direction(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
    
    def teleport(self, x, y):
        self.x = x
        self.y = y
    
    def next_coordinates(self, direction):
        if direction == "stop":
            return (self.x, self.y)
        elif direction == "up":
            return (self.x, self.y - 1)
        elif direction == "right":
            return (self.x + 1, self.y)
        elif direction == "down":
            return (self.x, self.y + 1)
        elif direction == "left":
            return (self.x - 1, self.y)
    
    def set_next_direction(self, new_direction):
        assert(new_direction in {"up", "right", "down", "left", "stop"})
        self.next_direction = new_direction
        self.buffer_turn = 2
    
    def iterate(self):
        #Этот if даст методу исполниться раз в self.update_interval итераций (кадров)
        self.frames_since_last_update += 1
        if self.frames_since_last_update < self.update_interval:
            return
        else:
            self.frames_since_last_update = 0
        
        
        # Не идти в стену
        if self.field.is_wall(*self.next_coordinates(self.current_direction)):
            self.current_direction = "stop"
        
        # Повернуть только если смена направления была на этой или предидущей итерации и в сторону поворота нет стены
        if (self.buffer_turn > 0) and not self.field.is_wall(*self.next_coordinates(self.next_direction)):
            self.current_direction = self.next_direction
        
        if self.buffer_turn > 0:
            self.buffer_turn -= 1
        
        self.move_in_direction(self.current_direction)
        
        
    def draw(self, screen, field_top_left_x, field_top_left_y, tile_size):
        pygame.draw.rect(screen, (255, 210, 0), 
            (self.x*tile_size + field_top_left_x, 
             self.y*tile_size + field_top_left_y, 
             tile_size, tile_size))
