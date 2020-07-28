import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT] and self.rect.x > 0:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] and self.rect.x < 750:
            self.speedx = 5
        if keystate[pygame.K_UP] and self.rect.y > 0:
            self.speedy = -5
        if keystate[pygame.K_DOWN] and self.rect.y < 550:
            self.speedy = 5

        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Blaster(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speedy = 0

    def update(self, xpos, ypos):
        keystate = pygame.key.get_pressed()

        if self.rect.y < 0:
            self.rect.y = ypos
            self.rect.x = xpos
            self.speedy = 0

        if self.speedy == 0:
            self.rect.y = ypos
            self.rect.x = xpos

        #Note: Game is slowing down as space bar is being spammed. Get this code to not run when blaster is fired
        if keystate[pygame.K_SPACE]:
                self.speedy = -10
        self.rect.y += self.speedy

class Abilities(Player):
    def __init__(self, image_file, location):
        Player.__init__(self, image_file, location)


    def update(self, xpos, ypos):
        self.rect.y = ypos-10
        self.rect.x = xpos-10


