import pygame
from random import randint

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('first game')

x = y = 50
width, height = (30, 30)

vel = 5
target = 500 - 30
run = True

while run:
    pygame.time.delay(50)
    print(target)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x == target and target > 0:
        target = 0
    if x == target == 0:
        target = 500 - 30
    if target > 0:
        x += vel
    if target == 0:
        x -= vel

    color = tuple(randint(1, 255) for _ in range(3))

    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height) )
    pygame.display.update()

pygame.quit()
