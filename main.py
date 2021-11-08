import pygame
import random
import math
from interface import Interface
from pacman import Pacman
from field import Field

WIDTH = 560
HEIGHT = 480
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("PyMan")
clock = pygame.time.Clock()

class GameState:
    def __init__(self):
        self.game_mode = "menu"
        self.current_frame = 0
        self.paused = False
        self.game_over = False
    def frameUpdate(self):
        self.current_frame += 1

game = GameState()
game.game_mode = "game"
interface = Interface()
tile_size = 30
field = Field()
pacman = Pacman(field, 1, 1)
while not game.game_over:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game.paused = False if game.paused else True
            if event.key == pygame.K_d:
                pacman.set_next_direction("right")
            if event.key == pygame.K_s:
                pacman.set_next_direction("down")
            if event.key == pygame.K_a:
                pacman.set_next_direction("left")
            if event.key == pygame.K_w:
                pacman.set_next_direction("up")

    if (game.paused):
        continue
    
    pacman.iterate()
    # BEGIN DRAWING 
    if game.game_mode == "game":
        screen.fill((0, 0, 0))
        field.draw(screen, 30, 30, tile_size)
        interface.draw(screen, WIDTH, HEIGHT, score = game.current_frame)
        pacman.draw(screen, 30, 30, tile_size)
    elif game.game_mode == "menu":
        screen.fill((25, 0, 60))

    # END DRAWING 
    game.frameUpdate()
    pygame.display.flip()       

pygame.quit()