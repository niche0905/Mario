from pico2d import *

class coin:
    image = None
    def __init__(self):
        if coin.image == None:
            coin.image = load_image('mario2.png')
        self.x, self.y = 500, 300
        self.width, self.height = 48, 48

    def update(self):
        pass

    def draw(self):
        coin.image.clip_draw(1 * self.width, 1 * self.height + 16, self.width, self.height, self.x, self.y, self.width, self.height)


g = 10

class mushroom:
    image = None
    def __init__(self):
        if mushroom.image == None:
            mushroom.image = load_image('mario2.png')
        self.x, self.y = 300, 300
        self.width, self.height = 48, 48
        self.direction = True # T left F right
        self.velocity = 0
        self.floor = 24

    def update(self):
        if self.direction == True:
            self.x -= 3
        else:
            self.x += 3
        if self.y > self.floor:
            self.velocity -= g
            self.y += self.velocity

        if self.x < 0:
            self.x = 0
            self.direction = False
        if self.x > 800:
            self.x = 800
            self.direction = True
        if self.y < self.floor:
            self.y = self.floor
            self.velocity = 0

    def draw(self):
        mushroom.image.clip_draw(4 * self.width + 4, 2 * self.height + 16, self.width, self.height, self.x, self.y, self.width, self.height)
