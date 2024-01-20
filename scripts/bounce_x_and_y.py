import pygame
from random import randint

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('first game')

x = y = 50
width, height = (30, 30)

x_vel = randint(1, 5)
y_vel = randint(1, 5)

x_target = 500 - width
y_target = 500 - height
run = True

while run:
    pygame.time.delay(20)
    print(x, y, x_target, y_target)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if x + x_vel > x_target and x_target > 0:
        x = x_target
    if x + x_vel < x_target and x_target == 0:
        x = x_target
    if x == x_target and x_target > 0:
        x_target = 0
    if x == x_target and x_target == 0:
        x_target = 500 - width
    if x_target > 0:
        x += x_vel
    if x_target == 0:
        x -= x_vel

    if y + y_vel > y_target and y_target > 0:
        y = y_target
    if y + y_vel < y_target and y_target == 0:
        y = y_target
    if y == y_target and y_target > 0:
        y_target = 0
    if y == y_target and y_target == 0:
        y_target = 500 - width
    if y_target > 0:
        y += y_vel
    if y_target == 0:
        y -= y_vel

    color = tuple(randint(1, 255) for _ in range(3))

    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height) )
    pygame.display.update()

pygame.quit()
