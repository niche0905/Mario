import random
import json
import os

from pico2d import *

import game_framework
import select_state
import server

import game_world

from player import Mario
from enemy import Goomba
from enemy import Koopa
from enemy import Flying_Koopa
from enemy import Hammer_bro
from object import coin
from object import mushroom

from block import hard_brick
from block import soft_brick
from block import grass_left
from block import grass_mid
from block import grass_right
from block import grass_bottom1
from block import grass_bottom2
from block import random_block
from block import mush_left
from block import mush_mid
from block import mush_right
from block import mush_neck
from block import mush_bottom
from block import pipe_left
from block import pipe_right
from block import mid_left
from block import mid_right
from block import pipe_top
from block import pipe_bottom
from block import mid_top
from block import mid_bottom
from block import cave_rock
from block import cloud_left
from block import cloud_mid
from block import cloud_right

name = "MainState"
music = None
background = None

def enter():
    global music
    global background
    server.character = Mario(900, 300)
    server.enemys.append(Goomba())
    server.enemys.append(Koopa())
    server.enemys.append(Hammer_bro())
    server.enemys.append(Flying_Koopa())
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
    server.blocks.append(mush_neck())
    server.blocks.append(mush_bottom())
    server.blocks.append(pipe_left())
    server.blocks.append(pipe_right())
    server.blocks.append(mid_left())
    server.blocks.append(mid_right())
    server.blocks.append(cave_rock())
    server.blocks.append(grass_bottom1())
    server.blocks.append(grass_bottom2())
    server.blocks.append(pipe_top())
    server.blocks.append(pipe_bottom())
    server.blocks.append(mid_top())
    server.blocks.append(mid_bottom())
    server.blocks.append(cloud_left())
    server.blocks.append(cloud_mid())
    server.blocks.append(cloud_right())
    game_world.add_object(server.character, 0)
    game_world.add_objects(server.enemys, 0)
    game_world.add_objects(server.objects, 0)
    game_world.add_objects(server.blocks, 0)
    server.camera_pivot = 0
    music = load_music('background.mp3')
    music.set_volume(16)
    music.repeat_play()
    background = load_image('grass.jpg')

def exit():
    global music
    global background
    game_world.clear()
    server.character = None
    server.enemys = []
    server.objects = []
    server.blocks = []
    server.ornblocks = []
    server.camera_pivot = 0
    del(music)
    del(background)


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
                game_framework.change_state(select_state)
            elif event.key == SDLK_LEFT:
                server.character.direction = True
                server.character.go = True
            elif event.key == SDLK_RIGHT:
                server.character.direction = False
                server.character.go = True
            elif event.key == SDLK_UP:
                if server.character.float == False:
                    server.character.jump = True
            elif event.key == SDLK_DOWN:
                if server.character.float == True:
                    server.character.spec = True
            elif event.key == SDLK_1 and (server.character.frame_y == 7 or server.character.frame_y == 6):
                server.character.frame_y = 9
                server.character.frame_x = 0
                server.character.floor = 8
                server.character.cap = 25
                server.character.float = True
            elif event.key == SDLK_2 and (server.character.frame_y == 9 or server.character.frame_y == 8):
                server.character.frame_y = 7
                server.character.frame_x = 0
                server.character.floor = 25
                server.character.y += 18
                server.character.cap = 30
                server.character.float = True
            elif event.key == SDLK_o:
                if server.rect_can_see:
                    server.rect_can_see = False
                else:
                    server.rect_can_see = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT and server.character.direction == True:
                server.character.go = False
            elif event.key == SDLK_RIGHT and server.character.direction == False:
                server.character.go = False



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if server.character.if_die():
        pass
    # 스테이트 바꾸기





def draw():
    clear_canvas()
    background.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
