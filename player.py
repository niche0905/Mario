from pico2d import *
# import math

g = 10

class Mario:
    image = None
    def __init__(self):
        if Mario.image == None:
            Mario.image = load_image('mario2.png')
        self.x, self.y = 400, 300
        self.direction = True # T left F right
        self.go = False
        self.jump = False
        self.hold = True
        self.spec = False
        self.frame_x, self.frame_y = 0, 7
        self.width, self.height = 64, 85
        self.velocity = 0
        self.floor = 25
        self.db_left, self.db_bottom, self.db_right, self.db_top = 0, 0, 0, 0

    def update(self):
        if self.go:
            if self.direction:
                self.x -= 7
            else:
                self.x += 7
            if self.frame_x != 3 and self.frame_x != 7:
                if self.frame_y == 7:
                    self.frame_x = (self.frame_x + 1) % 3
                elif self.frame_y == 9:
                    self.frame_x = (self.frame_x + 1) % 2
        else:
            if self.frame_x != 3 and self.frame_x != 7:
                self.frame_x = 0

        if self.jump:
            self.velocity = 50
            self.frame_x = 3
            self.jump = False
            self.hold = True
        if self.spec:
            self.velocity = 0
            self.spec = False
            self.frame_x = 7

        if self.hold:
            self.velocity -= g
            if self.frame_x == 7:
                self.velocity -= g
            self.y += self.velocity
        else:
            left_a, bottom_a, right_a, top_a = self.get_bb()

            if left_a >= self.db_right:
                self.hold = True
            else:
                if right_a <= self.db_left:
                    self.hold = True
                else:
                    if top_a <= self.db_bottom:
                        self.hold = True
                    else:
                        if bottom_a >= self.db_top:
                            self.hold = True
                        else:
                            pass

        if self.y < self.floor:
            self.y = self.floor
            self.hold = False
            self.velocity = 0
            self.frame_x = 0

    def draw(self):
        if self.direction:
            Mario.image.clip_composite_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, 0, 'n', self.x, self.y, self.width, self.height)
        else:
            Mario.image.clip_composite_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, 0, 'h', self.x, self.y, self.width, self.height)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.frame_y == 7:
            return self.x - 32 / 2, self.y - self.floor, self.x + 32 / 2, self.y + 60 / 2
        elif self.frame_y == 9:
            return self.x - 32 / 2, self.y - self.floor, self.x + 32 / 2, self.y + 50 / 2

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