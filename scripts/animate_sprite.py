import pygame
from random import randint
import spritesheet

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('tennis ball animation')

BG  = (0, 100, 75)
BLACK = (0,0,0)
sprite_sheet_image = pygame.image.load('./sprites/tennis_ball_sprite.png').convert_alpha()

sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
animation_frames = [sprite_sheet.get_image(i, 30, 30, 1.5, BLACK) for i in range(8)]

run = True
i = 0
while run:
    pygame.time.delay(40)

    win.fill(BG)
    if i < 8:
        frame = animation_frames[i]
        win.blit(frame, (sprite_sheet.x, sprite_sheet.y))
        i += 1
    if i == 7:
        i = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    sprite_sheet.move()
pygame.quit()
