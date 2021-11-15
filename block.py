from pico2d import *

class hard_brick:
    image = None
    def __init__(self):
        if hard_brick.image == None:
            hard_brick.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 50, 450, 50, 50

    def draw(self):
        hard_brick.image.clip_draw(261, 812, 29, 29, self.x, self.y, self.width, self.height)

class grass_left:
    image = None
    def __init__(self):
        if grass_left.image == None:
            grass_left.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 150, 450, 50, 50

    def draw(self):
        grass_left.image.clip_draw(2, 780, 28, 28, self.x, self.y, self.width, self.height)

class grass_mid:
    image = None
    def __init__(self):
        if grass_mid.image == None:
            grass_mid.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 200, 450, 50, 50

    def draw(self):
        grass_mid.image.clip_draw(35, 780, 28, 28, self.x, self.y, self.width, self.height)

class grass_right:
    image = None
    def __init__(self):
        if grass_right.image == None:
            grass_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 250, 450, 50, 50

    def draw(self):
        grass_right.image.clip_draw(67, 780, 28, 28, self.x, self.y, self.width, self.height)