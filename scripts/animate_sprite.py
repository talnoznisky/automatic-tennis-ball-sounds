import pygame
from random import randint
import spritesheet

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('tennis ball animation')

BG  = (0, 100, 75)
sprite_sheet_image = pygame.image.load('./sprites/tennis_ball_sprite.png').convert_alpha()


# create multiple sprite sheet objs
sprites = [spritesheet.SpriteSheet(sprite_sheet_image) for i in range(20)]


run = True
i = 0
while run:
    pygame.time.delay(40)

    win.fill(BG)
    if i < 8:
        for sprite in sprites:
            frame = sprite.return_frame(30, 30, 1.5)
            win.blit(frame, (sprite.x, sprite.y))
            sprite.move()
        i += 1
    if i == 7:
        i = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit()
