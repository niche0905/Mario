from pico2d import *
import player
import enemy

def handle_events():
    # fill here
    global running
    global character

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                character.direction = True
                character.go = True
            elif event.key == SDLK_RIGHT:
                character.direction = False
                character.go = True
            elif event.key == SDLK_UP:
                if character.y == character.floor:
                    character.jump = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and character.direction == True:
                character.go = False
            elif event.key == SDLK_RIGHT and character.direction == False:
                character.go = False

WIDTH, HEIGHT = 800, 600
open_canvas(WIDTH, HEIGHT)

running = True
character = player.Mario()
goomba = enemy.Goomba()

while running:
    clear_canvas()

    character.update()
    goomba.update()

    character.draw()
    goomba.draw()

    update_canvas()
    delay(0.05)
    handle_events()

close_canvas()