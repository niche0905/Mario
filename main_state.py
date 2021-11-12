import random
import json
import os

from pico2d import *

import game_framework

from pico2d import *
import game_world

from player import Mario
from enemy import Goomba
from enemy import Koopa
from enemy import Hammer_bro
from object import coin
from object import mushroom

name = "MainState"


character = None
goomba = None
koopa = None
h_bro = None
c1 = None
m1 = None

def enter():
    global character
    global goomba
    global koopa
    global h_bro
    global c1
    global m1
    character = Mario()
    goomba = Goomba()
    koopa = Koopa()
    h_bro = Hammer_bro()
    c1 = coin()
    m1 = mushroom()
    game_world.add_object(character, 0)
    game_world.add_object(goomba, 0)
    game_world.add_object(koopa, 0)
    game_world.add_object(h_bro, 0)
    game_world.add_object(c1, 0)
    game_world.add_object(m1, 0)

def exit():
    game_world.clear()



def pause():
    pass


def resume():
    pass


def handle_events():
    global character
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_LEFT:
                character.direction = True
                character.go = True
            elif event.key == SDLK_RIGHT:
                character.direction = False
                character.go = True
            elif event.key == SDLK_UP:
                if character.y == character.floor:
                    character.jump = True
            elif event.key == SDLK_DOWN:
                if character.hold == True:
                    character.spec = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and character.direction == True:
                character.go = False
            elif event.key == SDLK_RIGHT and character.direction == False:
                character.go = False



def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




