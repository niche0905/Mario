import random
import json
import os

from pico2d import *

import game_framework
import select_state

import game_world

name = "LogoState"

logo_image = None

def enter():
    global logo_image
    logo_image = load_image('logo.jpg')

def exit():
    global logo_image
    logo_image = None

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                game_framework.change_state(select_state)



def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    logo_image.clip_draw(0, 0, 600, 600, 400, 300, 800, 600)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

