import pygame
from random import randint

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('first game')

x = y = 50
width, height = (30, 30)

vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x < 500 - 30:
        x += 5
    if y < 500 - 30:
        y += 5

    color = tuple(randint(1, 255) for _ in range(3))

    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height) )
    pygame.display.update()

pygame.quit()
