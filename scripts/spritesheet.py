import pygame
from random import choice, randint, random

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
        self.x = 50
        self.y = 50
        self.width = 30 
        self.height = 30

        self.x_vel = random() * 10
        self.y_vel = random() * 10

        self.x_target = 500 - self.width
        self.y_target = 500 - self.height
        
        self.possible_sounds = self.get_possible_sounds()

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width) + 7 * (frame + 1) , 7 ,30,30))
        
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        image.set_colorkey(color)

        return image
    
    @staticmethod
    def get_possible_sounds():
        from glob import glob
        return glob('/Users/talnoznisky/sounds/LoFi Drum Kit Vol. 2/*/*.wav')

    def crash(self):
        ####################################
        pygame.mixer.Sound.play(pygame.mixer.Sound(choice(self.possible_sounds)))
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
            self.crash()
        if self.x == self.x_target and self.x_target == 0:
            self.x_target = 500 - self.width
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
            self.crash()      
        if self.y == self.y_target and self.y_target == 0:
            self.y_target = 500 - self.width
            self.crash()

        if self.y_target > 0:
            self.y += self.y_vel
        if self.y_target == 0:
            self.y -= self.y_vel
