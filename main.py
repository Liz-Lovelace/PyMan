import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyMan")
clock = pygame.time.Clock()

GAME_RUNNING = True
while GAME_RUNNING:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUNNING = False
    screen.fill((0, 0, 0))
    # BEGIN DRAWING 


    # END OF ALL DRAWING 
    pygame.display.flip()       

pygame.quit()