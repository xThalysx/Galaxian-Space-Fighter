import pygame
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speedx = 0
        self.speedy = 3

    def reset(self):
        x_pos = random.randint(0, 750)
        y_pos = random.randint(-200, 0)
        self.rect.y = y_pos
        self.rect.x = x_pos


    def update(self, IncreaseSpeed):

        if self.rect.y > 600:
            self.reset()

        if IncreaseSpeed:
            self.speedy += 0.5

        self.rect.y += self.speedy