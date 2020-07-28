from Enemy import *
import math

class Enemy2(Enemy):

    def __init__(self, image_file, location):
        Enemy.__init__(self, image_file, location)
        self.speed = 2.5

    def update(self, playerX, playerY):
        dx, dy = playerX - self.rect.x, playerY - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed





