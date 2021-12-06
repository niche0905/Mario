from pico2d import *
# import math
import server

PIXEL_PER_METER = (50.0 / 1.0)
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

g = 6

class Mario:
    image = None
    def __init__(self):
        if Mario.image == None:
            Mario.image = load_image('mario2.png')
        self.x, self.y = 500, 300
        self.direction = True # T left F right
        self.go = False
        self.jump = False
        self.float = True
        self.old_y = 0
        self.spec = False
        self.frame_x, self.frame_y = 0, 7
        self.width, self.height = 64, 85
        self.velocity = 0
        self.floor = 25
        self.cap = 30

    def update(self):
        if self.go:
            if self.direction:
                self.x -= 18
            else:
                self.x += 18

            if self.float == False:
                if self.frame_y == 7:
                    if self.frame_x == 2:
                        self.frame_y = 6
                    self.frame_x = (self.frame_x + 1) % 3
                elif self.frame_y == 6:
                    if self.frame_x == 2:
                        self.frame_y = 7
                    self.frame_x = (self.frame_x + 1) % 3
                elif self.frame_y == 9:
                    if self.frame_x == 1:
                        self.frame_y = 8
                    self.frame_x = (self.frame_x + 1) % 2
                elif self.frame_y == 8:
                    if self.frame_x == 1:
                        self.frame_y = 9
                    self.frame_x = (self.frame_x + 1) % 2
        else:
            if self.float == False:
                self.frame_x = 0
                if self.frame_y == 6 or self.frame_y == 8:
                    self.frame_y = self.frame_y + 1

        if self.jump:
            self.velocity = 50
            if self.frame_y == 6 or self.frame_y == 8:
                self.frame_y = self.frame_y + 1
            self.frame_x = 3
            self.jump = False
            self.float = True
        if self.spec:
            self.velocity = 0
            self.spec = False
            if self.frame_y == 6 or self.frame_y == 8:
                self.frame_y = self.frame_y + 1
            self.frame_x = 7

        self.old_y = self.y

        if self.float:
            self.velocity -= g
            if self.frame_x == 7:
                self.velocity -= g
            if self.velocity < -30:
                self.velocity = -30
            self.y += self.velocity

        for o in server.objects:
            if collide(server.character, o):
                pass

        for e in server.enemys:
            if collide(server.character, e):
                left_c, bottom_c, right_c, top_c = server.character.get_bb()
                left_e, bottom_e, right_e, top_e = e.get_bb()
                if server.character.velocity < 0:
                    if (self.old_y - self.floor > top_e) and (bottom_c < top_e):
                        mid_x = (left_c + right_c) / 2
                        if left_e < mid_x and mid_x < right_e:
                            # 적 죽여버려~
                            pass

        for b in server.blocks:
            if collide(server.character, b):
                left_c, bottom_c, right_c, top_c = server.character.get_bb()
                left_b, bottom_b, right_b, top_b = b.get_bb()
                if server.character.velocity < 0:
                    if (self.old_y - self.floor > top_b) and (bottom_c < top_b):
                        server.character.y = server.character.floor + top_b
                        server.character.float = False
                        server.character.velocity = 0
                        server.character.frame_x = 0
                    elif (self.old_y - self.floor < top_b) and (bottom_c < top_b):
                        if self.direction:
                            self.x = right_b + 16
                        else:
                            self.x = left_b - 16
                else:
                    if (self.old_y + self.cap < bottom_b) and (top_c > bottom_b):
                        server.character.y = -server.character.cap + bottom_b
                        server.character.velocity = 0
                    elif (self.old_y + self.cap > bottom_b) and (top_c > bottom_b):
                        if self.direction:
                            self.x = right_b + 16
                        else:
                            self.x = left_b - 16

    def draw(self):
        if self.direction:
            Mario.image.clip_composite_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, 0, 'n', self.x, self.y, self.width, self.height)
        else:
            Mario.image.clip_composite_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, 0, 'h', self.x, self.y, self.width, self.height)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.frame_y == 7 or self.frame_y == 6:
            return self.x - 32 / 2, self.y - self.floor, self.x + 32 / 2, self.y + self.cap
        elif self.frame_y == 9 or self.frame_y == 8:
            return self.x - 32 / 2, self.y - self.floor, self.x + 32 / 2, self.y + self.cap

# image = load_image('mario2.png')

#mario = Mario()
#
# open_canvas(800, 600)
#
# clear_canvas()
# mario.draw()
# update_canvas()
#
# delay (5)

# while running:
#     clear_canvas()
#     if go:
#         if look:
#             x -= 5
#         else:
#             x += 5
#         frame_x = (frame_x + 1) % 3
#     else:
#         frame_x = 0
#     if y > 40:
#         down_vector -= g
#     if jump:
#         down_vector = 40
#         jump = False
#     elif y <= 40:
#         y = 40
#         down_vector = 0
#     y += down_vector
#     mario.clip_draw(frame_x * width + int((frame_x + 1) * 0.5), frame_y * height, width, height, x, y)
#     # mario.clip_composite_draw(frame_x * width + int((frame_x + 1) * 0.5), frame_y * height, width, height, math.radians(0), True, x, y)
#     update_canvas()
#     delay(0.05)
#     handle_events()
#
# close_canvas()


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
