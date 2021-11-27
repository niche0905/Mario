import random
import json
import os

from pico2d import *

import game_framework
import map_1
import map_2
import map_3
import server

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



def enter():
    server.character = Mario()
    server.enemys.append(Goomba())
    server.enemys.append(Koopa())
    server.enemys.append(Hammer_bro())
    server.objects.append(coin())
    server.objects.append(mushroom())
    server.blocks.append(hard_brick(775, 25))
    server.blocks.append(grass_mid(25, -25))
    server.blocks.append(grass_mid(75, -25))
    server.blocks.append(grass_mid(125, -25))
    server.blocks.append(grass_mid(175, -25))
    server.blocks.append(grass_mid(225, -25))
    server.blocks.append(grass_mid(275, -25))
    server.blocks.append(grass_mid(325, -25))
    server.blocks.append(grass_mid(375, -25))
    server.blocks.append(grass_mid(425, -25))
    server.blocks.append(grass_mid(475, -25))
    server.blocks.append(grass_mid(525, -25))
    server.blocks.append(grass_mid(575, -25))
    server.blocks.append(grass_mid(625, -25))
    server.blocks.append(grass_mid(675, -25))
    server.blocks.append(grass_mid(725, -25))
    server.blocks.append(grass_mid(775, -25))
    server.blocks.append(grass_left())
    server.blocks.append(grass_mid())
    server.blocks.append(grass_right())
    server.blocks.append(soft_brick())
    server.blocks.append(random_block())
    server.blocks.append(mush_left())
    server.blocks.append(mush_mid())
    server.blocks.append(mush_right())
    server.blocks.append(pipe_left())
    server.blocks.append(pipe_right())
    server.blocks.append(mid_left())
    server.blocks.append(mid_right())
    game_world.add_object(server.character, 0)
    game_world.add_objects(server.enemys, 0)
    game_world.add_objects(server.objects, 0)
    game_world.add_objects(server.blocks, 0)

def exit():
    game_world.clear()
    server.character = None
    server.enemys = []
    server.objects = []
    server.blocks = []

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
            elif event.key == SDLK_LEFT:
                server.character.direction = True
                server.character.go = True
            elif event.key == SDLK_RIGHT:
                server.character.direction = False
                server.character.go = True
            elif event.key == SDLK_UP:
                if server.character.hold == False:
                    server.character.jump = True
            elif event.key == SDLK_DOWN:
                if server.character.hold == True:
                    server.character.spec = True
            elif event.key == SDLK_1 and server.character.frame_y == 7:
                server.character.frame_y = 9
                server.character.floor = 8
            elif event.key == SDLK_2 and server.character.frame_y == 9:
                server.character.frame_y = 7
                server.character.floor = 25
            elif event.key == SDLK_3:
                game_framework.change_state(map_1)
            elif event.key == SDLK_4:
                game_framework.change_state(map_2)
            elif event.key == SDLK_5:
                game_framework.change_state(map_3)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and server.character.direction == True:
                server.character.go = False
            elif event.key == SDLK_RIGHT and server.character.direction == False:
                server.character.go = False



def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for b in server.blocks:
        if collide(server.character, b):
            left_c, bottom_c, right_c, top_c = character.get_bb()
            left_b, bottom_b, right_b, top_b = b.get_bb()
            if server.character.velocity < 0:
                mid_x = (left_c + right_c) / 2
                if left_b < mid_x and mid_x < right_b:
                    server.character.db_left, server.character.db_bottom, server.character.db_right, server.character.db_top = b.get_bb()
                if server.character.y < server.character.floor + top_b:
                    server.character.y = server.character.floor + top_b
                    server.character.hold = False
                    server.character.velocity = 0
                    server.character.frame_x = 0
            else:
                if server.character.direction: # left
                    server.character.x = right_b + 16
                else: # right
                    server.character.x = left_b - 16



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
