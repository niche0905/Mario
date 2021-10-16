from pico2d import *

WIDTH, HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(WIDTH, HEIGHT)
mario = load_image('mario2.png')
enemies = load_image('enemis.png')

running = True
x, y = WIDTH//2, HEIGHT//2
frame_x, frame_y = 0, 4     # 15, 10
width, height = 64, 85
hide_cursor()

while running:
    clear_canvas()
    mario.clip_draw(frame_x * width + int((frame_x + 1) * 0.5), frame_y * height, width, height, x, y)
    update_canvas()
    frame_x = (frame_x + 1) % 15
    if frame_x == 0:
        frame_y = (frame_y + 1) % 10
    delay(0.05)
    handle_events()

close_canvas()