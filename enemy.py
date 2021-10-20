from pico2d import *
# import math

# WIDTH, HEIGHT = 800, 600

g = 10

class Goomba:
    def __init__(self):
        self.image = load_image('enemis.png')
        self.x, self.y = 400, 300
        self.velocity = 0
        self.floor = 10
        self.frame = 0
        self.width, self.height = 29, 29
        self.status = 0 # 0 seek 1 follow
        self.direction = True # T left F right
        self.death = False

    def update(self):
        if self.death:
            # del(self) # 이거 되냐?
            pass
        if abs(900 - self.x) < 50:
            self.status = 1
        else:
            self.status = 0
        if self.status == 1:
            if character_x < self.x:
                self.direction = True
            else:
                self.direction = False

        if self.direction == True:
            self.x -= 5
        else:
            self.x += 5
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

        self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(self.frame * self.width, 8 * self.height, self.width, self.height, self.x, self.y, self.width * 2, self.height * 2)

    # def death_check(self):
    #     self.death = True

class Koopa:
    def __init__(self):
        self.image = load_image('enemis.png')
        self.x, self.y = 400, 300
        self.velocity = 0
        self.floor = 20
        self.frame = 5
        self.width, self.height = 29, 29
        self.status = 0 # 0 alive 1 shell
        self.direction = True # T left F right
        self.death = False

    def update(self):
        if self.death:
            # del(self) # 이거 되냐?
            pass

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

        self.frame = (self.frame - 5 + 1) % 2 + 5

    def draw(self):
        if self.direction == True:
            self.image.clip_composite_draw(self.frame * self.width, 8 * self.height, self.width, self.height, 0, 'n', self.x, self.y, self.width * 2, self.height * 2)
        else:
            self.image.clip_composite_draw(self.frame * self.width, 8 * self.height, self.width, self.height, 0, 'h', self.x, self.y, self.width * 2, self.height * 2)

class Hammer_bro:
    def __init__(self):
        self.image = load_image('enemis.png')
        self.x, self.y = 400, 300
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
        self.death = False

    def update(self):
        if self.death:
            # del(self) # 이거 되냐?
            pass

        if character_x < self.x:
            self.direction = True
        else:
            self.direction = False

        if self.status == 0:
            self.frame = 3

        if abs(character_x - self.x) < 300 and abs(30 - self.y) < 30 and self.status == 0:
            self.status = 1
            self.frame = 5
            if self.direction:
                self.hammer_velocity = -5
            else:
                self.hammer_velocity = 5
            self.hx, self.hy = self.x, self.y

        if self.y > self.floor:
            self.velocity -= g
            self.y += self.velocity

        if self.y < self.floor:
            self.y = self.floor
            self.velocity = 0

        if self.status == 1:
            self.hx += self.hammer_velocity
            self.hammer_frame = (self.hammer_frame + 1) % 4
            if abs(self.x - self.hx) > 400:
                self.hammer_velocity *= -1
            if abs(self.x - self.hx) < 3:
                self.status = 0
                self.frame = 4

    def draw(self):
        if self.direction == True:
            self.image.clip_composite_draw(self.frame * self.width, 5 * self.height, self.width, self.height, 0, 'n', self.x, self.y, self.width * 2, self.height * 2)
        else:
            self.image.clip_composite_draw(self.frame * self.width, 5 * self.height, self.width, self.height, 0, 'h', self.x, self.y, self.width * 2, self.height * 2)
        if self.status == 1:
            if self.hammer_velocity > 0:
                if self.hammer_frame >= 2:
                    self.image.clip_composite_draw((1 - self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'n', self.hx, self.hy, self.hammer_width * 2, self.hammer_height * 2)
                else:
                    self.image.clip_composite_draw((self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'n', self.hx, self.hy, self.hammer_width * 2, self.hammer_height * 2)
            else:
                if self.hammer_frame >= 2:
                    self.image.clip_composite_draw((1 - self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'h', self.hx, self.hy, self.hammer_width * 2, self.hammer_height * 2)
                else:
                    self.image.clip_composite_draw((self.hammer_frame % 2) * self.hammer_width + 29 * 9, ((self.hammer_frame // 2)) * self.hammer_height + 29 * 5, self.hammer_width, self.hammer_height, 0, 'h', self.hx, self.hy, self.hammer_width * 2, self.hammer_height * 2)
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
character_x, chararcter_y = 200, 30

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