from pico2d import *
import server

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
        coin.image.clip_draw(1 * self.width, 1 * self.height + 16, self.width, self.height, self.x - server.camera_pivot, self.y, self.width, self.height)
        draw_rectangle(*self.get_bb(True))

    def get_bb(self, camera = False):
        if camera:
            return self.x - 24 - server.camera_pivot, self.y - 22, self.x + 8 - server.camera_pivot, self.y + 16
        else:
            return self.x - 24, self.y - 22, self.x + 8, self.y + 16


g = 10

class mushroom:
    image = None
    def __init__(self, x = 300, y = 300):
        if mushroom.image == None:
            mushroom.image = load_image('mario2.png')
        self.x, self.y = x, y
        self.width, self.height = 48, 48
        self.direction = True # T left F right
        self.velocity = 0
        self.floor = 24
        self.old_y = 0

    def update(self):
        if self.direction == True:
            self.x -= 3
        else:
            self.x += 3

        self.old_y = self.y

        self.velocity -= g
        self.y += self.velocity

        for b in server.blocks:
            if collide(self, b):
                left_c, bottom_c, right_c, top_c = self.get_bb()
                left_b, bottom_b, right_b, top_b = b.get_bb()
                if self.velocity < 0:
                    if (self.old_y - self.floor >= top_b) and (bottom_c < top_b):
                        self.y = self.floor + top_b
                        self.velocity = 0
                    elif (self.old_y - self.floor <= top_b) and (bottom_c < top_b):
                        if self.direction:
                            self.x = right_b + 16 + 1
                            self.direction = False
                        else:
                            self.x = left_b - 16 - 1
                            self.direction = True


    def draw(self):
        mushroom.image.clip_draw(4 * self.width + 4, 2 * self.height + 16, self.width, self.height, self.x - server.camera_pivot, self.y, self.width, self.height)
        draw_rectangle(*self.get_bb(True))

    def get_bb(self, camera = False):
        if camera:
            return self.x - 20 - server.camera_pivot, self.y - self.floor, self.x + 20 - server.camera_pivot, self.y + 16
        else:
            return self.x - 20, self.y - self.floor, self.x + 20, self.y + 16



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a >= right_b:
        return False
    if right_a <= left_b:
        return False
    if top_a <= bottom_b:
        return False
    if bottom_a >= top_b:
        return False

    return True