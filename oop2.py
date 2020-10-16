import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 20
w, l = (1200, 900)
screen = pygame.display.set_mode((w, l))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
maxRadius = 42
score=0

class Square(Ball):

    def draw(self):
        rect()




class Ball:

    def __init__(self):
        self.x = randint(42, 1200)
        self.y = randint(42, 900)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.r = randint(10, 42)
        self.color = COLORS[randint(0, 5)]


    def move(self):
        if(self.x + self.r) > 1200 or (self.x - self.r) < 0:
            self.vx = -self.vx

        if(self.y + self.r) > 900 or (self.y - self.r) < 0:
            self.vy = -self.vy

        self.x += self.vx
        self.y += self.vy

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def check_event(self, pos):
        x, y = pos
        if (self.x - x) ** 2 + (self.y - y) ** 2 <= (self.r) ** 2:
           return True


balls = [Ball() for i in range(17)]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    for objct in balls:
        objct.move()
        objct.draw()

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for objct in balls:
                if (objct.check_event(event.pos)) == True:
                    score+=1
                    print(score)

    screen.fill(BLACK)

pygame.quit()
