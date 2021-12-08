import random
import json
import os

import game_framework
import server

import select_state

from pico2d import *
import game_world

from player import Mario
from block import hard_brick, soft_brick, random_block, mush_left, mush_mid, mush_right, mush_neck, mush_bottom, cloud_left, cloud_mid, cloud_right, pipe_left, pipe_right, mid_left, mid_right
from enemy import Goomba, Koopa, Hammer_bro, Flying_Koopa
from object import coin, mushroom

name = "Map3State"

music = None
background = None

def enter():
    global music
    global background
    server.camera_pivot = 0
    server.character = Mario(50, 200, server.character_state)

    server.blocks.append(mush_left(25, 75))
    server.blocks.append(mush_mid(75, 75))
    server.blocks.append(mush_mid(125, 75))
    server.blocks.append(mush_mid(175, 75))
    server.blocks.append(mush_mid(225, 75))
    server.ornblocks.append(mush_neck(225, 25))
    server.blocks.append(mush_mid(275, 75))
    server.blocks.append(mush_mid(325, 75))
    server.blocks.append(mush_mid(375, 75))
    server.blocks.append(mush_right(425, 75))

    server.blocks.append(mush_left(525, 225))
    server.blocks.append(mush_mid(575, 225))
    server.blocks.append(mush_mid(625, 225))
    server.blocks.append(mush_mid(675, 225))
    server.blocks.append(mush_mid(725, 225))
    server.blocks.append(random_block(725, 425))
    server.blocks.append(mush_neck(725, 175))
    server.blocks.append(mush_bottom(725, 125))
    server.blocks.append(mush_bottom(725, 75))
    server.blocks.append(mush_bottom(725, 25))
    server.blocks.append(mush_mid(775, 225))
    server.blocks.append(mush_mid(825, 225))
    server.blocks.append(mush_mid(875, 225))
    server.blocks.append(mush_right(925, 225))

    server.objects.append(coin(675, 275))
    server.objects.append(coin(725, 275))
    server.objects.append(coin(775, 275))

    server.blocks.append(mush_left(1025, 325))
    server.blocks.append(mush_mid(1075, 325))
    server.blocks.append(mush_mid(1125, 325))
    server.blocks.append(mush_mid(1175, 325))
    server.blocks.append(mush_mid(1225, 325))
    server.ornblocks.append(mush_neck(1225, 275))
    server.ornblocks.append(mush_bottom(1225, 225))
    server.ornblocks.append(mush_bottom(1225, 175))
    server.ornblocks.append(mush_bottom(1225, 125))
    server.ornblocks.append(mush_bottom(1225, 75))
    server.ornblocks.append(mush_bottom(1225, 25))
    server.blocks.append(mush_mid(1275, 325))
    server.blocks.append(mush_mid(1325, 325))
    server.blocks.append(mush_mid(1375, 325))
    server.blocks.append(mush_right(1425, 325))

    server.enemys.append(Hammer_bro(1225, 375))

    server.blocks.append(cloud_left(1675, 225))
    server.blocks.append(cloud_mid(1725, 225))
    server.blocks.append(cloud_right(1775, 225))

    server.enemys.append(Flying_Koopa(1850, 200))

    server.blocks.append(cloud_left(1975, 275))
    server.blocks.append(cloud_mid(2025, 275))
    server.blocks.append(cloud_right(2075, 275))

    server.enemys.append(Flying_Koopa(2200, 250))

    server.blocks.append(cloud_left(2325, 175))
    server.blocks.append(cloud_mid(2375, 175))
    server.blocks.append(cloud_right(2425, 175))

    server.blocks.append(hard_brick(2625, 225))
    server.blocks.append(hard_brick(2675, 225))
    server.blocks.append(hard_brick(2725, 225))
    server.blocks.append(hard_brick(2775, 225))
    server.blocks.append(hard_brick(2825, 225))

    server.objects.append(coin(2625, 275))
    server.objects.append(coin(2675, 275))
    server.objects.append(coin(2725, 275))
    server.objects.append(coin(2775, 275))
    server.objects.append(coin(2825, 275))

    server.blocks.append(soft_brick(2625, 375))
    server.blocks.append(soft_brick(2675, 375))
    server.blocks.append(soft_brick(2725, 375))
    server.blocks.append(soft_brick(2775, 375))
    server.blocks.append(soft_brick(2825, 375))

    server.blocks.append(mush_left(3175, 375))
    server.blocks.append(mush_mid(3225, 375))
    server.blocks.append(mush_mid(3275, 375))
    server.ornblocks.append(mush_neck(3275, 325))
    server.ornblocks.append(mush_bottom(3275, 275))
    server.ornblocks.append(mush_bottom(3275, 225))
    server.ornblocks.append(mush_bottom(3275, 175))
    server.ornblocks.append(mush_bottom(3275, 125))
    server.ornblocks.append(mush_bottom(3275, 75))
    server.ornblocks.append(mush_bottom(3275, 25))
    server.blocks.append(mush_mid(3325, 375))
    server.blocks.append(mush_right(3375, 375))

    server.enemys.append(Flying_Koopa(3500, 300))

    server.blocks.append(pipe_left(3625, 325))
    server.blocks.append(pipe_right(3675, 325))
    server.blocks.append(mid_left(3625, 275))
    server.blocks.append(mid_right(3675, 275))
    server.blocks.append(mid_left(3625, 225))
    server.blocks.append(mid_right(3675, 225))
    server.blocks.append(mid_left(3625, 175))
    server.blocks.append(mid_right(3675, 175))
    server.blocks.append(mid_left(3625, 125))
    server.blocks.append(mid_right(3675, 125))
    server.blocks.append(mid_left(3625, 75))
    server.blocks.append(mid_right(3675, 75))
    server.blocks.append(mid_left(3625, 25))
    server.blocks.append(mid_right(3675, 25))

    server.blocks.append(pipe_left(3825, 425))
    server.blocks.append(pipe_right(3875, 425))
    server.blocks.append(mid_left(3825, 375))
    server.blocks.append(mid_right(3875, 375))
    server.blocks.append(mid_left(3825, 325))
    server.blocks.append(mid_right(3875, 325))
    server.blocks.append(mid_left(3825, 275))
    server.blocks.append(mid_right(3875, 275))
    server.blocks.append(mid_left(3825, 225))
    server.blocks.append(mid_right(3875, 225))
    server.blocks.append(mid_left(3825, 175))
    server.blocks.append(mid_right(3875, 175))
    server.blocks.append(mid_left(3825, 125))
    server.blocks.append(mid_right(3875, 125))
    server.blocks.append(mid_left(3825, 75))
    server.blocks.append(mid_right(3875, 75))
    server.blocks.append(mid_left(3825, 25))
    server.blocks.append(mid_right(3875, 25))

    server.objects.append(coin(3825, 475))
    server.objects.append(coin(3875, 475))

    server.blocks.append(pipe_left(4025, 225))
    server.blocks.append(pipe_right(4075, 225))
    server.blocks.append(mid_left(4025, 175))
    server.blocks.append(mid_right(4075, 175))
    server.blocks.append(mid_left(4025, 125))
    server.blocks.append(mid_right(4075, 125))
    server.blocks.append(mid_left(4025, 75))
    server.blocks.append(mid_right(4075, 75))
    server.blocks.append(mid_left(4025, 25))
    server.blocks.append(mid_right(4075, 25))

    server.enemys.append(Flying_Koopa(4200, 250))

    server.blocks.append(cloud_left(4325, 275))
    server.blocks.append(cloud_mid(4375, 275))
    server.blocks.append(cloud_right(4425, 275))

    server.enemys.append(Flying_Koopa(4550, 250))

    server.blocks.append(mush_left(4625, 375))
    server.blocks.append(mush_mid(4675, 375))
    server.blocks.append(mush_mid(4725, 375))
    server.blocks.append(mush_mid(4775, 375))

    game_world.add_object(server.character, 1)
    game_world.add_objects(server.enemys, 1)
    game_world.add_objects(server.blocks, 0)
    game_world.add_objects(server.ornblocks, 0)
    game_world.add_objects(server.objects, 1)

    music = load_music('background.mp3')
    music.set_volume(16)
    music.repeat_play()

    background = load_image('sky.jpg')

def exit():
    global music
    global background

    game_world.clear()
    server.character = None
    server.blocks = []
    server.enemys = []
    server.ornblocks = []
    server.objects = []
    server.camera_pivot = 0
    server.pre_coin = 0

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
    global left_down, right_down
    for game_object in game_world.all_objects():
        game_object.update()

    if server.character.x >= 400 and server.character.x <= 4800 - 400:
        server.camera_pivot = server.character.x - 400

    if server.character.if_die():
        server.character_state = 1
        game_framework.change_state(select_state)

    elif server.character.x > 4800:
        server.coin += server.pre_coin
        server.score += server.pre_coin * 100 + 5000
        server.character_state = server.character.status
        if server.clear_stage <= 2:
            server.clear_stage = 3
        game_framework.change_state(select_state)
    # 이겼다 판정


def draw():
    clear_canvas()
    background.clip_draw(0, 0, 510, 340, 400, 300, 800, 600)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




