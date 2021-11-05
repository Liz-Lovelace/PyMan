import pygame
import random
import math
from interface import Interface

WIDTH = 360
HEIGHT = 480
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyMan")
clock = pygame.time.Clock()

class GameState:
    def __init__(self):
        self.game_mode = "menu"
        self.current_frame = 0
        self.paused = False
        
    def frameUpdate(self):
        self.current_frame += 1

GAME_RUNNING = True
game = GameState()
game.game_mode = "game"
interface = Interface(screen)
while GAME_RUNNING:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game.paused = False if game.paused else True

    if (game.paused):
        continue
        
    # BEGIN DRAWING 
    if game.game_mode == "game":
        screen.fill((0, 0, 0))
        interface.draw(screen, WIDTH, HEIGHT, score = game.current_frame)

    elif game.game_mode == "menu":
        screen.fill((25, 0, 60))

    # END DRAWING 
    game.frameUpdate()
    pygame.display.flip()       

pygame.quit()