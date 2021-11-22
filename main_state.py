import random
import json
import os

from pico2d import *

import game_framework
import map_1
import map_2
import map_3

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
from block import pipe_left
from block import pipe_right
from block import mid_left
from block import mid_right

name = "MainState"


character = None
goomba = None
koopa = None
h_bro = None
c1 = None
m1 = None
blocks = []

def enter():
    global character
    global goomba
    global koopa
    global h_bro
    global c1
    global m1
    global blocks
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
    blocks.append(hard_brick(775, 25))
    blocks.append(grass_mid(25, -25))
    blocks.append(grass_mid(75, -25))
    blocks.append(grass_mid(125, -25))
    blocks.append(grass_mid(175, -25))
    blocks.append(grass_mid(225, -25))
    blocks.append(grass_mid(275, -25))
    blocks.append(grass_mid(325, -25))
    blocks.append(grass_mid(375, -25))
    blocks.append(grass_mid(425, -25))
    blocks.append(grass_mid(475, -25))
    blocks.append(grass_mid(525, -25))
    blocks.append(grass_mid(575, -25))
    blocks.append(grass_mid(625, -25))
    blocks.append(grass_mid(675, -25))
    blocks.append(grass_mid(725, -25))
    blocks.append(grass_mid(775, -25))
    blocks.append(grass_left())
    blocks.append(grass_mid())
    blocks.append(grass_right())
    blocks.append(soft_brick())
    blocks.append(random_block())
    blocks.append(mush_left())
    blocks.append(mush_mid())
    blocks.append(mush_right())
    blocks.append(pipe_left())
    blocks.append(pipe_right())
    blocks.append(mid_left())
    blocks.append(mid_right())
    game_world.add_objects(blocks, 0)

def exit():
    game_world.clear()
    global blocks
    del(blocks)


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
                if character.hold == False:
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
            elif event.key == SDLK_3:
                game_framework.change_state(map_1)
            elif event.key == SDLK_4:
                game_framework.change_state(map_2)
            elif event.key == SDLK_5:
                game_framework.change_state(map_3)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and character.direction == True:
                character.go = False
            elif event.key == SDLK_RIGHT and character.direction == False:
                character.go = False



def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for b in blocks:
        if collide(character, b):
            left_c, bottom_c, right_c, top_c = character.get_bb()
            left_b, bottom_b, right_b, top_b = b.get_bb()
            if character.velocity < 0:
                mid_x = (left_c + right_c) / 2
                if left_b < mid_x and mid_x < right_b:
                    character.db_left, character.db_bottom, character.db_right, character.db_top = b.get_bb()
                if character.y < character.floor + top_b:
                    character.y = character.floor + top_b
                    character.hold = False
                    character.velocity = 0
                    character.frame_x = 0
            else:
                if character.direction: # left
                    character.x = right_b + 16
                else: # right
                    character.x = left_b - 16



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

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
