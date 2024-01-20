import pygame
from random import randint, random

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('first game')
class Square():
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 30 
        self.height = 30

        self.x_vel = random() * 10
        self.y_vel = random() * 10

        self.x_target = 500 - self.width
        self.y_target = 500 - self.height

        self.color = tuple(randint(1, 255) for _ in range(3))
    
    def crash(self):
        ####################################
        pygame.mixer.Sound.play(pygame.mixer.Sound("crash.wav"))
        pygame.mixer.music.stop()

    def move(self):
        # x attributes
        if self.x + self.x_vel > self.x_target and self.x_target > 0:
            self.x = self.x_target
        if self.x + self.x_vel < self.x_target and self.x_target == 0:
            self.x = self.x_target
        
        # change x target and color
        if self.x == self.x_target and self.x_target > 0:
            self.x_target = 0
            self.color = tuple(randint(1, 255) for _ in range(3))
            self.crash()
        if self.x == self.x_target and self.x_target == 0:
            self.x_target = 500 - self.width
            self.color = tuple(randint(1, 255) for _ in range(3))            
            self.crash()

        if self.x_target > 0:
            self.x += self.x_vel
        if self.x_target == 0:
            self.x -= self.x_vel

        # y attributes
        if self.y + self.y_vel > self.y_target and self.y_target > 0:
            self.y = self.y_target
        if self.y + self.y_vel < self.y_target and self.y_target == 0:
            self.y = self.y_target
        
        # change y target and color
        if self.y == self.y_target and self.y_target > 0:
            self.y_target = 0
            self.color = tuple(randint(1, 255) for _ in range(3))      
            self.crash()      
        if self.y == self.y_target and self.y_target == 0:
            self.y_target = 500 - self.width
            self.color = tuple(randint(1, 255) for _ in range(3))
            self.crash()

        if self.y_target > 0:
            self.y += self.y_vel
        if self.y_target == 0:
            self.y -= self.y_vel


run = True

square_1 = Square()
square_2 = Square()
square_3 = Square()

while run:
    pygame.time.delay(32)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))
    pygame.draw.rect(win, square_1.color, (square_1.x, square_1.y, square_1.width, square_1.height))
    pygame.draw.rect(win, square_2.color, (square_2.x, square_2.y, square_2.width, square_2.height))
    pygame.draw.rect(win, square_3.color, (square_3.x, square_3.y, square_3.width, square_3.height))
    pygame.display.update()

    square_1.move()
    square_2.move()
    square_3.move()

pygame.quit()
