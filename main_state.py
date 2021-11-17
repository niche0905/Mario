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

from block import hard_brick
from block import soft_brick
from block import grass_left
from block import grass_mid
from block import grass_right
from block import random_block
from block import mush_left
from block import mush_mid
from block import mush_right

name = "MainState"


character = None
goomba = None
koopa = None
h_bro = None
c1 = None
m1 = None
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None
b6 = None
b7 = None
b8 = None
b9 = None

def enter():
    global character
    global goomba
    global koopa
    global h_bro
    global c1
    global m1
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
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
    b1 = hard_brick()
    b2 = grass_left()
    b3 = grass_mid()
    b4 = grass_right()
    b5 = soft_brick()
    b6 = random_block()
    b7 = mush_left()
    b8 = mush_mid()
    b9 = mush_right()

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
            elif event.key == SDLK_1 and character.frame_y == 7:
                character.frame_y = 9
                character.floor = 8
            elif event.key == SDLK_2 and character.frame_y == 9:
                character.frame_y = 7
                character.floor = 25
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and character.direction == True:
                character.go = False
            elif event.key == SDLK_RIGHT and character.direction == False:
                character.go = False



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    b6.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    update_canvas()




