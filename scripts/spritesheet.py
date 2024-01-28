import pygame
from random import choice, random

class SpriteSheet():
    def __init__(self, image, x_boundary, y_boundary, frame_count=7):
        self.sheet = image

        self.frame_count = frame_count
        self.current_frame = 0

        self.x = 0
        self.y = 0

        self.width = 30 
        self.height = 30

        self.x_vel = random() * 10
        self.y_vel = random() * 10

        self.x_boundary =   x_boundary
        self.y_boundary =   y_boundary
        self.x_target =     x_boundary - self.width
        self.y_target =     y_boundary - self.height
        
        self.possible_sounds = self.get_possible_sounds()

    def update_current_frame(self):
        if self.current_frame < self.frame_count:
            self.current_frame += 1
        else: 
            self.current_frame = 0

    def return_frame(self, width, height, scale, color=(0,0,0)):
        current_frame = self.current_frame
        
        new_frame = pygame.Surface((width, height)).convert_alpha()
        new_frame.blit(self.sheet, (0,0), ((current_frame * width) + 7 * (current_frame + 1) , 7 ,30,30))
        new_frame = pygame.transform.scale(new_frame, (width * scale, height * scale))
        new_frame.set_colorkey(color)
        
        self.update_current_frame()

        return new_frame

    @staticmethod
    def get_possible_sounds():
        from glob import glob
        return glob('./sounds/*.wav')

    def play_sound(self):
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
            self.play_sound()
        if self.x == self.x_target and self.x_target == 0:
            self.x_target = self.x_boundary - self.width
            self.play_sound()

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
            self.play_sound()      
        if self.y == self.y_target and self.y_target == 0:
            self.y_target = self.y_boundary - self.height
            self.play_sound()

        if self.y_target > 0:
            self.y += self.y_vel
        if self.y_target == 0:
            self.y -= self.y_vel
