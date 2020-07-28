import pygame
import os

class Image(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        #image.get.rect() gets the rect size of the image
        self.rect = self.image.get_rect()
        #the "rect" has different locations / coords on the perimeter of the rect. Ex rect.left is the left middle side of rect
        self.rect.left, self.rect.top = location


class Screen():

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def draw_screen(self):

        x = 865 / 3
        y = 75
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

        return pygame.display.set_mode((self.width, self.height))

    #@classmethod
    #def CollidePoint(cls, m_x, m_y, b_x, b_y):
        #if((b_x < m_x and m_x < b_x + 225) and (b_y < m_y and m_y < b_y + 70)):
            #return True






