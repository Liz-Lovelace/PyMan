import pygame

class Interface:
    def __init__(self):
        self.main_font = pygame.font.SysFont('Comic Sans MS', 20)
    
    def draw(self, screen, WIDTH, HEIGHT, score = -1, high_score = -1, lives = -1, level = -1):
        score_surface = self.main_font.render(f'Score: {str(score)}', False, (255, 255, 0))
        high_score_surface = self.main_font.render(f'High Score: {str(high_score)}', False, (255, 100, 0))
        level_surface = self.main_font.render(f'Level: {str(level)}', False, (0, 255, 255))
        
        screen.blit(score_surface, (10, 10))
        screen.blit(high_score_surface, (WIDTH - 140, 10))
        screen.blit(level_surface, (10, HEIGHT - 40))
        #отрисовка картинки жизней * на lives