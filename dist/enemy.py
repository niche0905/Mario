import random

from pico2d import *
# import math
import game_world
import server

# WIDTH, HEIGHT = 800, 600

g = 10

class Goomba:
    image = None
    def __init__(self, x = 400, y = 300):
        if Goomba.image == None:
            Goomba.image = load_image('enemis.png')
        self.x, self.y = x, y
        self.velocity = 0
        self.floor = 10
        self.frame = 0
        self.width, self.height = 29, 29
        self.status = 0 # 0 seek 1 follow
        self.direction = True # T left F right
        self.old_y = 0
        self.float = True
        self.dby = 0

    def update(self):
        if abs(server.character.x - self.x) < 200:
            self.status = 1
        else:
            self.status = 0
        if self.status == 1:
            if server.character.x < self.x:
                self.direction = True
            else:
                self.direction = False

        if self.direction == True:
            self.x -= 5
        else:
            self.x += 5

        self.old_y = self.y

        self.velocity -= g
        self.y += self.velocity
        self.float = True

        for b in server.blocks:
            if collide(self, b):
                left_c, bottom_c, right_c, top_c = self.get_bb()
                left_b, bottom_b, right_b, top_b = b.get_bb()
                if self.velocity <= 0:
                    if (self.old_y - self.floor >= top_b) and (bottom_c < top_b):
                        self.y = self.floor + top_b
                        self.velocity = 0
                        self.float = False
                        self.dby = b.y
                    elif (self.old_y - self.floor <= top_b) and (bottom_c < top_b):
                        if self.direction:
                            self.x = right_b + 16 + 1
                            self.direction = False
                        else:
                            self.x = left_b - 16 - 1
                            self.direction = True

        flag = True
        if self.float == False and self.status == 0:
            if self.direction:
                for b in server.blocks:
                    if b.y == self.dby and b.x == self.x - (self.x % 50) + 25:
                        flag = False
                if flag:
                    self.direction = False
            else:
                for b in server.blocks:
                    if b.y == self.dby and b.x == self.x - (self.x % 50) + 25:
                        flag = False
                if flag:
                    self.direction = True

        self.frame = (self.frame + 1) % 2

        if collide2(self, server.character):
            server.character.hit()

        # ???????????? ???????????????

        if self.y < -100:
            game_world.remove_object(self)
            server.enemys.remove(self)


    def draw(self):
        Goomba.image.clip_draw(self.frame * self.width, 8 * self.height, self.width, self.height, self.x + self.width / 2 - server.camera_pivot, self.y, self.width * 2, self.height * 2)
        if server.rect_can_see:
            draw_rectangle(*self.get_bb(True))

    def get_bb(self, camera = False):
        if camera:
            return self.x - self.width / 2 - server.camera_pivot, self.y - self.floor, self.x + self.width / 2 - server.camera_pivot, self.y + self.height / 2
        else:
            return self.x - self.width / 2, self.y - self.floor, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        game_world.remove_object(self)
        server.enemys.remove(self)


    # def death_check(self):
    #     self.death = True

class Koopa:
    image = None
    def __init__(self, x = 400, y = 300):
        if Koopa.image == None:
            Koopa.image = load_image('enemis.png')
        self.x, self.y = x, y
        self.velocity = 0
        self.floor = 20
        self.frame = 5
        self.width, self.height = 29, 29
        self.status = 0 # 0 alive 1 stop_shell 2 moving_shell
        self.direction = True # T left F right
        self.death = False
        self.old_y = 0
        self.float = True
        self.dby = 0

    def update(self):
        if self.death:
            # del(self) # ?????? ???????
            pass

        if self.status == 0:
            if self.direction == True:
                self.x -= 3
            else:
                self.x += 3

            self.old_y = self.y

            self.velocity -= g
            self.y += self.velocity
            self.float = True

            for b in server.blocks:
                if collide(self, b):
                    left_c, bottom_c, right_c, top_c = self.get_bb()
                    left_b, bottom_b, right_b, top_b = b.get_bb()
                    if self.velocity <= 0:
                        if (self.old_y - self.floor >= top_b) and (bottom_c < top_b):
                            self.y = self.floor + top_b
                            self.velocity = 0
                            self.float = False
                            self.dby = b.y
                        elif (self.old_y - self.floor <= top_b) and (bottom_c < top_b):
                            if self.direction:
                                self.x = right_b + 16 + 1
                                self.direction = False
                            else:
                                self.x = left_b - 16 - 1
                                self.direction = True


            flag = True
            if self.float == False:
                if self.direction:
                    for b in server.blocks:
                        if b.y == self.dby and b.x == self.x - (self.x % 50) + 25:
                            flag = False
                    if flag:
                        self.direction = False
                else:
                    for b in server.blocks:
                        if b.y == self.dby and b.x == self.x - (self.x % 50) + 25:
                            flag = False
                    if flag:
                        self.direction = True


            self.frame = (self.frame - 5 + 1) % 2 + 5
        else:
            if self.status == 1:
                pass
            elif self.status == 2:
                if self.direction == True:
                    self.x -= 15
                else:
                    self.x += 15

            self.old_y = self.y

            self.velocity -= g
            self.y += self.velocity

            for b in server.blocks:
                if collide(self, b):
                    left_c, bottom_c, right_c, top_c = self.get_bb()
                    left_b, bottom_b, right_b, top_b = b.get_bb()
                    if self.velocity <= 0:
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


            self.frame = 12


        if collide2(self, server.character):
            server.character.hit()


        if self.y < -100:
            game_world.remove_object(self)
            server.enemys.remove(self)

    def draw(self):
        if self.status == 0:
            if self.direction == True:
                Koopa.image.clip_composite_draw(self.frame * self.width, 8 * self.height, self.width, self.height, 0, 'n', self.x - server.camera_pivot, self.y, self.width * 2, self.height * 2)
            else:
                Koopa.image.clip_composite_draw(self.frame * self.width, 8 * self.height, self.width, self.height, 0, 'h', self.x - server.camera_pivot, self.y, self.width * 2, self.height * 2)
            if server.rect_can_see:
                draw_rectangle(*self.get_bb(True))
        else:
            Koopa.image.clip_composite_draw(self.frame * self.width, 8 * self.height, self.width, self.height, 0, 'n', self.x - 10 - server.camera_pivot, self.y, self.width * 2, self.height * 2)
            if server.rect_can_see:
                draw_rectangle(*self.get_bb(True))

    def get_bb(self, camera = False):
        if camera:
            if self.status == 0:
                return self.x - self.width / 2 - server.camera_pivot, self.y - self.floor, self.x + self.width / 2 - server.camera_pivot, self.y + self.height / 2
            else:
                return self.x - self.width / 2 - server.camera_pivot, self.y - self.floor, self.x + self.width / 2 - server.camera_pivot, self.y + self.height / 2
        else:
            if self.status == 0:
                return self.x - self.width / 2, self.y - self.floor, self.x + self.width / 2, self.y + self.height / 2
            else:
                return self.x - self.width / 2, self.y - self.floor, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
        if self.status == 0:
            self.floor = 10
            self.status = 1
        elif self.status == 1:
            self.status = 2
            if random.randint(0, 2) == 0:
                self.direction == True
            else:
                self.direction == False
        elif self.status == 2:
            self.status = 1

class Flying_Koopa:
    image = None
    def __init__(self, x = 200, y = 300):
        if Flying_Koopa.image == None:
            Flying_Koopa.image = load_image('enemis.png')
        self.x, self.y = x, y
        self.sy = y
        self.velocity = 0
        self.frame = 3
        self.width, self.height = 29, 29
        self.direction = True # T up F down
        self.floor = 20

    def update(self):
        if self.direction == True:
            self.y += 3
        else:
            self.y -= 3

        if self.frame == 3:
            self.frame = 4
        elif self.frame == 4:
            self.frame = 3

        if self.y >= self.sy + 100:
            self.direction = False
        elif self.y <= self.sy - 100:
            self.direction = True

        if collide2(self, server.character):
            server.character.hit()

        if self.y < -100:
            game_world.remove_object(self)
            server.enemys.remove(self)

    def draw(self):
        Flying_Koopa.image.clip_composite_draw(self.frame * self.width, 8 * self.height, self.width, self.height, 0, 'n', self.x - server.camera_pivot, self.y, self.width * 2, self.height * 2)
        if server.rect_can_see:
            draw_rectangle(*self.get_bb(True))

    def get_bb(self, camera = False):
        if camera:
            return self.x - self.width / 2 - server.camera_pivot, self.y - self.floor, self.x + self.width / 2 - server.camera_pivot, self.y + self.height / 2
        else:
            return self.x - self.width / 2, self.y - self.floor, self.x + self.width / 2, self.y + self.height / 2

    def hit(self):
            game_world.remove_object(self)
            server.enemys.remove(self)

class Hammer_bro:
    image = None
    def __init__(self, x = 400, y = 300):
        if Hammer_bro.image == None:
            Hammer_bro.image = load_image('enemis.png')
        self.x, self.y = x, y
        self.velocity = 0
        self.floor = 20
        self.frame = 3
        self.width, self.height = 29, 29
        self.status = 0 # 0 get hammer 1 throw hammer
        self.hx, self.hy = self.x, self.y
        self.hammer_velocity = 0
        self.hammer_frame = 0 # 0 ~ 3 : 4
        self.hammer_width, self.hammer_height = 14, 14
        self.direction = True # T left F right
        self.old_y = 0

    def update(self):
        if server.character.x < self.x:
            self.direction = True
        else:
            self.direction = False

        if self.status == 0:
            self.frame = 3

        if abs(server.character.x - self.x) < 300 and abs(server.character.y - self.y) < 30 and self.status == 0:
            self.status = 1
            self.frame = 5
            if self.direction:
                self.hammer_velocity = -5
            else:
                self.hammer_velocity = 5
            self.hx, self.hy = self.x, self.y


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


        if collide2(self, server.character):
            server.character.hit()

        if self.y < -100:
            game_world.remove_object(self)
            server.enemys.remove(self)

        if self.status == 1:
            self.hx += self.hammer_velocity * 2
            self.hammer_frame = (self.hammer_frame + 1) % 4
            if abs(self.x - self.hx) > 400:
                self.hammer_velocity *= -1
            if abs(self.x - self.hx) < 3:
                self.status = 0
                self.frame = 4

            if collide3(self, server.character):
                server.character.hit()

    def draw(self):
        if self.direction == True:
            Hammer_bro.image.clip_composite_draw(self.frame * self.width, 5 * self.height, self.width, self.height, 0, 'n', self.x - server.camera_pivot, self.y, self.width * 2, self.height * 2)
        else:
            Hammer_bro.image.clip_composite_draw(self.frame * self.width, 5 * self.height, self.width, self.height, 0, 'h', self.x - server.camera_pivot, self.y, self.width * 2, self.height * 2)
        if server.rect_can_see:
            draw_rectangle(*self.get_bb(True))
        if self.status == 1:
            if self.hammer_velocity > 0:
                if self.hammer_frame >= 2:
                    Hammer_bro.image.clip_composite_draw((1 - self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'n', self.hx - server.camera_pivot, self.hy, self.hammer_width * 2, self.hammer_height * 2)
                else:
                    Hammer_bro.image.clip_composite_draw((self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'n', self.hx - server.camera_pivot, self.hy, self.hammer_width * 2, self.hammer_height * 2)
            else:
                if self.hammer_frame >= 2:
                    Hammer_bro.image.clip_composite_draw((1 - self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'h', self.hx - server.camera_pivot, self.hy, self.hammer_width * 2, self.hammer_height * 2)
                else:
                    Hammer_bro.image.clip_composite_draw((self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'h', self.hx - server.camera_pivot, self.hy, self.hammer_width * 2, self.hammer_height * 2)
            if server.rect_can_see:
                draw_rectangle(*self.get_bb2(True))

    def get_bb(self, camera = False):
        if camera:
            return self.x - self.width / 2 - server.camera_pivot, self.y - self.floor, self.x + self.width / 2 - server.camera_pivot, self.y + self.height / 2
        else:
            return self.x - self.width / 2, self.y - self.floor, self.x + self.width / 2, self.y + self.height / 2

    def get_bb2(self, camera = False):
        if camera:
            return self.hx - self.hammer_width / 2 - server.camera_pivot, self.hy - self.hammer_height / 2, self.hx + self.hammer_width / 2 - server.camera_pivot, self.hy + self.hammer_height / 2
        else:
            return self.hx - self.hammer_width / 2, self.hy - self.hammer_height / 2, self.hx + self.width / 2, self.hy + self.hammer_height / 2

    def hit(self):
        game_world.remove_object(self)
        server.enemys.remove(self)


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

def collide2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    top_a -= 10

    if left_a >= right_b:
        return False
    if right_a <= left_b:
        return False
    if top_a <= bottom_b:
        return False
    if bottom_a >= top_b:
        return False

    return True

def collide3(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb2()
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

# def handle_events():
#     global running
#
#     events = get_events()
#
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN:
#             if event.key == SDLK_ESCAPE:
#                 running = False

# open_canvas(WIDTH, HEIGHT)

# running = True

# goomba = Goomba()

# while running:
#     clear_canvas()
#
#     goomba.update()
#
#     goomba.draw()
#
#     update_canvas()
#     delay(0.05)
#
#     handle_events()


# close_canvas()