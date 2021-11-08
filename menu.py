import pygame
import sys

def print_text(screen, message, x, y):
    pygame.font.init()
    font = pygame.font.SysFont("Helvetica", 40, True)
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (x, y))

class Button:
    def __init__(self, width, height, message):
        self.width = width
        self.height = height
        self.inactive_clr = (0, 0, 0)
        self.active_clr = (62, 136, 108)
        self.message = message
    
    def intersection(self, x, y, left_x, top_y):
        return (left_x < x < left_x + self.width) and (top_y < y < top_y + self.height)

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, (0, 0, 0), (x, y, self.width, self.height))
        mouse = pygame.mouse.get_pos()
        if self.intersection(mouse[0], mouse[1], x, y):
            draw_color = self.active_clr
        else:
            draw_color = self.inactive_clr
        pygame.draw.rect(screen, draw_color, (x, y, self.width, self.height))
        print_text(screen, self.message, x+10, y+10)

class Menu: 
    def __init__(self):
        self.start_btn = Button(300, 70, "START")
        self.exit_btn = Button(300, 70, "EXIT")
        self.record_table_btn = Button(300, 70, "RECORD TABLE")

    def draw(self, screen, WIDTH, HEIGHT):
        screen.fill((27, 16, 40))
        left_border = WIDTH / 2 - self.start_btn.width/ 2
        self.start_btn.draw(screen, left_border, int(HEIGHT / 5 + 30))
        self.exit_btn.draw(screen, left_border, int(HEIGHT / 5 * 2 + 30))
        self.record_table_btn.draw(screen, left_border, int(HEIGHT / 5 * 3 + 30))
