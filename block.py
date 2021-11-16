from pico2d import *

class hard_brick:
    image = None
    def __init__(self):
        if hard_brick.image == None:
            hard_brick.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 50, 450, 50, 50

    def draw(self):
        hard_brick.image.clip_draw(261, 812, 29, 29, self.x, self.y, self.width, self.height)

class soft_brick:
    image = None
    def __init__(self):
        if grass_right.image == None:
            grass_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 350, 450, 50, 50

    def draw(self):
        grass_right.image.clip_draw(2, 942, 28, 28, self.x, self.y, self.width, self.height)

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

class random_block:
    image = None
    def __init__(self):
        if grass_right.image == None:
            grass_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 450, 450, 50, 50
        self.frame = 0 # 0 1 2 3

    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        grass_right.image.clip_draw(34 + 33 * self.frame, 943, 28, 28, self.x, self.y, self.width, self.height)

class mush_left:
    image = None
    def __init__(self):
        if grass_left.image == None:
            grass_left.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 550, 450, 50, 50

    def draw(self):
        grass_left.image.clip_draw(457, 683, 28, 28, self.x, self.y, self.width, self.height)

class mush_mid:
    image = None
    def __init__(self):
        if grass_mid.image == None:
            grass_mid.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 600, 450, 50, 50

    def draw(self):
        grass_mid.image.clip_draw(489, 683, 28, 28, self.x, self.y, self.width, self.height)

class mush_right:
    image = None
    def __init__(self):
        if grass_right.image == None:
            grass_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 650, 450, 50, 50

    def draw(self):
        grass_right.image.clip_draw(521, 683, 28, 28, self.x, self.y, self.width, self.height)