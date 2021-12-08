from pico2d import *

import game_world
import server
from object import mushroom

class hard_brick:
    image = None
    def __init__(self, x = 50, y = 450):
        if hard_brick.image == None:
            hard_brick.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        hard_brick.image.clip_draw(261, 812, 29, 29, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class soft_brick:
    image = None
    def __init__(self, x = 350, y = 450):
        if grass_right.image == None:
            grass_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        grass_right.image.clip_draw(2, 942, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class grass_left:
    image = None
    def __init__(self, x = 150, y = 450):
        if grass_left.image == None:
            grass_left.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        grass_left.image.clip_draw(2, 780, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class grass_mid:
    image = None
    def __init__(self, x = 200, y = 450):
        if grass_mid.image == None:
            grass_mid.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        grass_mid.image.clip_draw(35, 780, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class grass_right:
    image = None
    def __init__(self, x = 250, y = 450):
        if grass_right.image == None:
            grass_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        grass_right.image.clip_draw(67, 780, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class random_block:
    image = None
    sound = None
    def __init__(self, x = 450, y = 450):
        if random_block.image == None:
            random_block.image = load_image('blocks.png')
        if random_block.sound == None:
            random_block.sound = load_wav('random.mp3')
        self.x, self.y, self.width, self.height = x, y, 50, 50
        self.frame = 0 # 0 1 2 3
        self.able = True

    def update(self):
        if self.able:
            self.frame = (self.frame + 1) % 3

    def draw(self):
        random_block.image.clip_draw(34 + 33 * self.frame, 943, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        if self.able:
            random_block.sound.play()
            self.able = False
            m1 = mushroom(self.x, self.y + 50)
            server.objects.append(m1)
            game_world.add_object(m1, 1)
            self.frame = 3

class mush_left:
    image = None
    def __init__(self, x = 550, y = 450):
        if mush_left.image == None:
            mush_left.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mush_left.image.clip_draw(457, 683, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class mush_mid:
    image = None
    def __init__(self, x = 600, y = 450):
        if mush_mid.image == None:
            mush_mid.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mush_mid.image.clip_draw(489, 683, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class mush_right:
    image = None
    def __init__(self, x = 650, y = 450):
        if mush_right.image == None:
            mush_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mush_right.image.clip_draw(521, 683, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class mush_neck:
    image = None
    def __init__(self, x = 600, y = 400):
        if mush_neck.image == None:
            mush_neck.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mush_neck.image.clip_draw(489, 650, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class mush_bottom:
    image = None
    def __init__(self, x = 600, y = 350):
        if mush_bottom.image == None:
            mush_bottom.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mush_bottom.image.clip_draw(489, 618, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class pipe_left:
    image = None
    def __init__(self, x = 650, y = 350):
        if pipe_left.image == None:
            pipe_left.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        pipe_left.image.clip_draw(554, 198, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class pipe_right:
    image = None
    def __init__(self, x = 700, y = 350):
        if pipe_right.image == None:
            pipe_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        pipe_right.image.clip_draw(587, 198, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class mid_left:
    image = None
    def __init__(self, x = 650, y = 300):
        if mid_left.image == None:
            mid_left.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mid_left.image.clip_draw(554, 165, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class mid_right:
    image = None
    def __init__(self, x = 700, y = 300):
        if mid_right.image == None:
            mid_right.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        mid_right.image.clip_draw(587, 165, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass

class cave_rock:
    image = None
    def __init__(self, x = 50, y = 450):
        if cave_rock.image == None:
            cave_rock.image = load_image('blocks.png')
        self.x, self.y, self.width, self.height = x, y, 50, 50

    def update(self):
        pass

    def draw(self):
        cave_rock.image.clip_draw(2, 165, 28, 28, self.x - server.camera_pivot, self.y, self.width, self.height)

    def get_bb(self):
        return self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        pass
