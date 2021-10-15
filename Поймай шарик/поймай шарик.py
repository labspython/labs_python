import pygame
from pygame.draw import *
from random import randint
pygame.init()

result = 0

FPS = 50
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    def __init__(self):
        self.coord = [randint(100, 1100), randint(100, 900)]
        self.r = 50
        self.velocity = [randint(-15, 15), randint(-15, 15)]
        self.color = COLORS[randint(0, 5)]
        self.flag = True

    def move(self):
        v0_x, v0_y = self.velocity
        self.coord[0] += v0_x
        self.coord[1] += v0_y

    def draw(self):
        circle(screen, self.color, (self.coord[0], self.coord[1]), self.r)

    def collision(self, BORDER_EDGERS):
        if self.coord[0] <= 0 or self.coord[0] >= BORDER_EDGERS[0]:
            self.velocity[0] *= -1
        if self.coord[1] <= 0 or self.coord[1] >= BORDER_EDGERS[1]:
            self.velocity[1] *= -1
            
    def event(self, event):
        x0, y0 = self.coord
        pos_x, pos_y = event.pos
        if (pos_x-x0)**2 + (pos_y - y0)**2 <= self.r**2:
            self.flag = False
            
pygame.display.update()
clock = pygame.time.Clock()
finished = False

pool = [Ball(), Ball(), Ball(), Ball(), Ball(), Ball()]


while not finished:
    clock.tick(FPS)
            
    for ball in pool:
        ball.move()
        ball.draw()
        ball.collision([1200, 900])
    for event in pygame.event.get():
        for i, ball in enumerate(pool):
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ball.event(event)
                if not ball.flag:
                    pool.pop(i)
                    result += 1
    if not pool:
        finished = True                  


    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()

print('Enter your name:')
name = str(input())
print(result)
