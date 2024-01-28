import pygame
import spritesheet

pygame.init()

BG  = (20, 120, 75)
WIDTH = 450
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('tennis ball animation')

sprite_sheet_image = pygame.image.load('./sprites/tennis_ball_sprite.png').convert_alpha()
sprites = [spritesheet.SpriteSheet(
                                    sprite_sheet_image,
                                    x_boundary=WIDTH, 
                                    y_boundary=HEIGHT
                                ) for i in range(5)]

run = True
i = 0
if __name__ == '__main__':
    while run:
        pygame.time.delay(20)

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
