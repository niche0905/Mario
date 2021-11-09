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
        self.frame_x, self.frame_y = 0, 5
        self.width, self.height = 64, 85
        self.velocity = 0
        self.floor = 30

    def update(self):
        if self.go:
            if self.direction:
                self.x -= 7
            else:
                self.x += 7
            self.frame_x = (self.frame_x + 1) % 3
        else:
            self.frame_x = 0

        if self.y > self.floor:
            self.frame_x = 3
            self.velocity -= g
        if self.jump:
            self.velocity = 40
            self.jump = False

        self.y += self.velocity

        if self.y < self.floor:
            self.y = self.floor
            self.velocity = 0
            self.frame_x = 0

    def draw(self):
        if self.direction:
            Mario.image.clip_composite_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, 0, 'n', self.x, self.y, self.width, self.height)
        else:
            Mario.image.clip_composite_draw(self.frame_x * self.width + int((self.frame_x + 1) * 0.5), self.frame_y * self.height, self.width, self.height, 0, 'h', self.x, self.y, self.width, self.height)


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