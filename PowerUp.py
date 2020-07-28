from Enemy import *

class PowerUP(Enemy):

    def __init__(self, image_file, location):
        Enemy.__init__(self, image_file, location)
        self.speedx = 0
        self.speedy = 0
        self.move = False

    def reset(self):
        x_pos = random.randint(-600, -50)
        y_pos = random.randint(0, 650 / 2)
        self.rect.y = y_pos
        self.rect.x = x_pos

    def update(self, spawn):

        if (spawn):
            self.move = True

        if self.move == True:
            self.speedx = 2
            self.rect.x += self.speedx

        if self.rect.x > 850:
            self.move = False
            self.speedx = 0
            self.reset()
