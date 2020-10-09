import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class draw_ball:

    def __init__(self):
        self.x = randint(100,700)
        self.y = randint(100,500)
        self.r = randint(30,50)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)

    def circle_draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0

while not finished:
    b = draw_ball()
    b.circle_draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (b.x - x)**2+(b.y-y)**2 <= (b.r)**2:
                score += 1
                print(score)

    screen.fill(BLACK)

pygame.quit()