import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((455, 300))

rect(screen, (153, 227, 237), (0, 0, 455, 150))
rect(screen, (14, 147, 37), (0, 150, 455, 300))
rect(screen, (147, 107, 14), (70, 125, 115, 78))
rect(screen, (14, 147, 145), (109, 150, 36, 30))
polygon(screen, (235, 47, 68), [(70,125), (126,69),
                               (185,125)])
circle(screen, (254, 249, 249), (222, 52), 20)
circle(screen, (254, 249, 249), (242, 52), 20)
circle(screen, (254, 249, 249), (262, 52), 20)
circle(screen, (254, 249, 249), (282, 52), 20)
circle(screen, (254, 249, 249), (242, 38), 20)
circle(screen, (254, 249, 249), (262, 38), 20)
rect(screen, (0, 0, 0), (328, 138, 10, 51))
circle(screen, (15, 83, 14), (335, 117), 20)
circle(screen, (15, 83, 14), (352, 129), 20)
circle(screen, (15, 83, 14), (316, 126), 20)
circle(screen, (15, 83, 14), (358, 98), 20)
circle(screen, (15, 83, 14), (313, 101), 20)
circle(screen, (15, 83, 14), (336, 82), 20)
circle(screen, (255, 255, 0), (400, 30), 20)
line(screen, (255, 240, 0), (400, 30), (370, 40), 1)
line(screen, (255, 240, 0), (400, 30), (365, 42), 1)
line(screen, (255, 240, 0), (400, 30), (372, 45), 1)
line(screen, (255, 240, 0), (400, 30), (390, 55), 1)
line(screen, (255, 240, 0), (400, 30), (410, 65), 1)
line(screen, (255, 240, 0), (400, 30), (355, 30), 1)
line(screen, (255, 240, 0), (400, 30), (340, 20), 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
