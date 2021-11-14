from pico2d import *

class hard_brick:
    image = None
    def __init__(self):
        if hard_brick.image == None:
            hard_brick.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = 50, 450, 50, 50

    def draw(self):
        hard_brick.image.clip_draw(261, 812, 30, 30, self.x, self.y, self.width, self.height)