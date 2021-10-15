import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (217, 217, 217), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 10)
circle(screen, (255, 0, 0), (250, 180), 15)
circle(screen, (0, 0, 0), (250, 180), 8)
line(screen, (0, 0, 0), (100, 120), (180, 170), 10)
line(screen, (0, 0, 0), (300, 140), (220, 170), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

