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
        if abs(character_x - self.x) < 50:
            self.status = 1
        else:
            self.status = 0
        if self.status == 1:
            if character_x < self.x:
                self.direction = 0
            else:
                self.direction = 1

        if self.direction == True:
            self.x -= 5
        else:
            self.x += 5
        if self.y > self.floor:
            self.velocity -= g
            self.y += self.velocity

        if self.x < 0:
            self.x = 0
            self.direction = 1
        if self.x > 800:
            self.x = 800
            self.direction = 0
        if self.y < self.floor:
            self.y = self.floor
            self.velocity = 0

        self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(self.frame * self.width, 8 * self.height, self.width, self.height, self.x, self.y, self.width * 2, self.height * 2)

    # def death_check(self):
    #     self.death = True

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
character_x, chararcter_y = 800, 30

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