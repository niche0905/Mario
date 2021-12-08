import random
import json
import os

import game_framework
import server

import select_state

from pico2d import *
import game_world

from player import Mario
from block import soft_brick, grass_left, grass_mid, grass_right, grass_bottom1, grass_bottom2, random_block, pipe_left, pipe_right, mid_left, mid_right
from object import coin, mushroom

name = "Map1State"

music = None
background = None

def enter():
    global music
    global background
    server.camera_pivot = 0
    server.character = Mario(50, 200)
    server.blocks.append(grass_mid(25, 25)) # 0
    server.blocks.append(grass_mid(75, 25))
    server.blocks.append(grass_mid(125, 25))
    server.blocks.append(grass_mid(175, 25))
    server.blocks.append(grass_mid(225, 25))
    server.blocks.append(grass_mid(275, 25))
    server.blocks.append(grass_mid(325, 25))
    server.blocks.append(grass_mid(375, 25))
    server.blocks.append(grass_mid(425, 25))
    server.blocks.append(grass_mid(475, 25))
    server.blocks.append(grass_mid(525, 25))
    server.blocks.append(grass_mid(575, 25))
    server.blocks.append(grass_mid(625, 25))
    server.blocks.append(grass_mid(675, 25))
    server.blocks.append(grass_mid(725, 25))
    server.blocks.append(grass_mid(775, 25))

    server.objects.append(coin(525, 75))
    server.objects.append(coin(575, 75))
    server.objects.append(coin(625, 75))

    server.blocks.append(soft_brick(375, 275))
    server.blocks.append(soft_brick(425, 275))
    server.blocks.append(soft_brick(475, 275))
    server.blocks.append(random_block(525, 275))
    server.blocks.append(soft_brick(575, 275))
    server.blocks.append(soft_brick(625, 275))
    server.blocks.append(soft_brick(675, 275))

    server.blocks.append(grass_mid(825, 25)) # 800
    server.blocks.append(grass_mid(875, 25))
    server.blocks.append(grass_mid(925, 25))
    server.blocks.append(grass_mid(975, 25))
    server.blocks.append(grass_mid(1025, 25))
    server.blocks.append(grass_mid(1075, 25))
    server.blocks.append(grass_right(1125, 25))

    server.blocks.append(grass_left(1325, 25))
    server.blocks.append(grass_mid(1375, 25))
    server.blocks.append(grass_mid(1425, 25))
    server.blocks.append(grass_mid(1475, 25))
    server.blocks.append(grass_mid(1525, 25))
    server.blocks.append(grass_mid(1575, 25))

    server.blocks.append(grass_mid(1625, 25)) # 1600
    server.blocks.append(grass_mid(1675, 25))
    server.blocks.append(pipe_left(1675, 175))
    server.blocks.append(pipe_right(1725, 175))
    server.blocks.append(mid_left(1675, 125))
    server.blocks.append(mid_right(1725, 125))
    server.blocks.append(mid_left(1675, 75))
    server.blocks.append(mid_right(1725, 75))
    server.blocks.append(grass_mid(1725, 25))
    server.blocks.append(grass_mid(1775, 25))
    server.blocks.append(grass_mid(1825, 25))
    server.blocks.append(grass_mid(1875, 25))
    server.blocks.append(grass_mid(1925, 25))
    server.blocks.append(grass_mid(1975, 25))
    server.blocks.append(grass_mid(2025, 25))
    server.blocks.append(grass_mid(2075, 25))
    server.blocks.append(grass_mid(2125, 25))
    server.blocks.append(grass_mid(2175, 25))
    server.blocks.append(grass_mid(2225, 25))
    server.blocks.append(grass_mid(2275, 25))
    server.blocks.append(grass_mid(2325, 25))
    server.blocks.append(grass_mid(2375, 25))

    server.blocks.append(soft_brick(1875, 325))
    server.blocks.append(soft_brick(1925, 325))
    server.blocks.append(soft_brick(1975, 325))
    server.blocks.append(soft_brick(2025, 325))
    server.blocks.append(soft_brick(2075, 325))
    server.blocks.append(soft_brick(2125, 325))

    server.objects.append(coin(1925, 375))
    server.objects.append(coin(1975, 375))
    server.objects.append(coin(2025, 375))
    server.objects.append(coin(2075, 375))

    server.blocks.append(grass_mid(2425, 25)) # 2400
    server.blocks.append(grass_mid(2475, 25))
    server.blocks.append(grass_mid(2425, 25))
    server.blocks.append(grass_mid(2475, 25))
    server.blocks.append(grass_mid(2525, 25))
    server.blocks.append(grass_mid(2575, 25))
    server.blocks.append(grass_mid(2625, 25))
    server.blocks.append(grass_mid(2675, 25))
    server.blocks.append(grass_right(2725, 25))

    server.blocks.append(grass_left(2975, 75))
    server.blocks.append(grass_mid(3025, 75))
    server.blocks.append(grass_mid(3075, 75))
    server.blocks.append(grass_mid(3125, 75))
    server.blocks.append(grass_mid(3175, 75))
    server.ornblocks.append(grass_bottom1(2975, 25))
    server.ornblocks.append(grass_bottom2(3025, 25))
    server.ornblocks.append(grass_bottom1(3075, 25))
    server.ornblocks.append(grass_bottom2(3125, 25))
    server.ornblocks.append(grass_bottom1(3175, 25))

    server.objects.append(coin(3125, 125))
    server.objects.append(coin(3175, 125))
    server.objects.append(coin(3225, 125))
    server.objects.append(coin(3275, 125))

    server.blocks.append(grass_mid(3225, 75))  # 3200
    server.blocks.append(grass_mid(3275, 75))
    server.blocks.append(grass_mid(3325, 75))
    server.blocks.append(grass_mid(3375, 75))
    server.blocks.append(grass_mid(3425, 75))
    server.blocks.append(grass_mid(3475, 75))
    server.blocks.append(grass_mid(3525, 75))
    server.blocks.append(grass_mid(3575, 75))
    server.blocks.append(grass_mid(3625, 75))
    server.blocks.append(grass_mid(3675, 75))
    server.blocks.append(grass_mid(3725, 75))
    server.blocks.append(grass_right(3775, 75))
    server.ornblocks.append(grass_bottom2(3225, 25))
    server.ornblocks.append(grass_bottom1(3275, 25))
    server.ornblocks.append(grass_bottom2(3325, 25))
    server.ornblocks.append(grass_bottom1(3375, 25))
    server.ornblocks.append(grass_bottom2(3425, 25))
    server.ornblocks.append(grass_bottom1(3475, 25))
    server.ornblocks.append(grass_bottom2(3525, 25))
    server.ornblocks.append(grass_bottom1(3575, 25))
    server.ornblocks.append(grass_bottom2(3625, 25))
    server.ornblocks.append(grass_bottom1(3675, 25))
    server.ornblocks.append(grass_bottom2(3725, 25))
    server.ornblocks.append(grass_bottom1(3775, 25))
    server.blocks.append(grass_mid(3825, 25))
    server.blocks.append(grass_mid(3875, 25))
    server.blocks.append(grass_mid(3925, 25))
    server.blocks.append(grass_mid(3975, 25))

    server.blocks.append(grass_right(4025, 25))  # 4000
    server.blocks.append(grass_left(4225, 25))
    server.blocks.append(grass_left(4275, 75))
    server.blocks.append(grass_left(4325, 125))
    server.blocks.append(grass_left(4375, 175))
    server.blocks.append(grass_left(4425, 225))
    server.blocks.append(grass_left(4475, 275))
    server.blocks.append(grass_left(4525, 325))
    server.blocks.append(grass_mid(4575, 325))
    server.blocks.append(grass_mid(4625, 325))
    server.blocks.append(grass_mid(4675, 325))
    server.blocks.append(grass_mid(4725, 325))
    server.blocks.append(grass_mid(4775, 325))
    server.ornblocks.append(grass_bottom2(4275, 25))
    server.ornblocks.append(grass_bottom1(4325, 25))
    server.ornblocks.append(grass_bottom2(4375, 25))
    server.ornblocks.append(grass_bottom1(4425, 25))
    server.ornblocks.append(grass_bottom2(4475, 25))
    server.ornblocks.append(grass_bottom1(4525, 25))
    server.ornblocks.append(grass_bottom2(4575, 25))
    server.ornblocks.append(grass_bottom1(4625, 25))
    server.ornblocks.append(grass_bottom2(4675, 25))
    server.ornblocks.append(grass_bottom1(4725, 25))
    server.ornblocks.append(grass_bottom2(4775, 25))

    server.ornblocks.append(grass_bottom1(4325, 75))
    server.ornblocks.append(grass_bottom2(4375, 75))
    server.ornblocks.append(grass_bottom1(4425, 75))
    server.ornblocks.append(grass_bottom2(4475, 75))
    server.ornblocks.append(grass_bottom1(4525, 75))
    server.ornblocks.append(grass_bottom2(4575, 75))
    server.ornblocks.append(grass_bottom1(4625, 75))
    server.ornblocks.append(grass_bottom2(4675, 75))
    server.ornblocks.append(grass_bottom1(4725, 75))
    server.ornblocks.append(grass_bottom2(4775, 75))

    server.ornblocks.append(grass_bottom2(4375, 125))
    server.ornblocks.append(grass_bottom1(4425, 125))
    server.ornblocks.append(grass_bottom2(4475, 125))
    server.ornblocks.append(grass_bottom1(4525, 125))
    server.ornblocks.append(grass_bottom2(4575, 125))
    server.ornblocks.append(grass_bottom1(4625, 125))
    server.ornblocks.append(grass_bottom2(4675, 125))
    server.ornblocks.append(grass_bottom1(4725, 125))
    server.ornblocks.append(grass_bottom2(4775, 125))

    server.ornblocks.append(grass_bottom1(4425, 175))
    server.ornblocks.append(grass_bottom2(4475, 175))
    server.ornblocks.append(grass_bottom1(4525, 175))
    server.ornblocks.append(grass_bottom2(4575, 175))
    server.ornblocks.append(grass_bottom1(4625, 175))
    server.ornblocks.append(grass_bottom2(4675, 175))
    server.ornblocks.append(grass_bottom1(4725, 175))
    server.ornblocks.append(grass_bottom2(4775, 175))

    server.ornblocks.append(grass_bottom2(4475, 225))
    server.ornblocks.append(grass_bottom1(4525, 225))
    server.ornblocks.append(grass_bottom2(4575, 225))
    server.ornblocks.append(grass_bottom1(4625, 225))
    server.ornblocks.append(grass_bottom2(4675, 225))
    server.ornblocks.append(grass_bottom1(4725, 225))
    server.ornblocks.append(grass_bottom2(4775, 225))

    server.ornblocks.append(grass_bottom1(4525, 275))
    server.ornblocks.append(grass_bottom2(4575, 275))
    server.ornblocks.append(grass_bottom1(4625, 275))
    server.ornblocks.append(grass_bottom2(4675, 275))
    server.ornblocks.append(grass_bottom1(4725, 275))
    server.ornblocks.append(grass_bottom2(4775, 275))

    server.blocks.append(grass_mid(4825, 325))
    server.blocks.append(grass_mid(4875, 325))
    server.blocks.append(grass_mid(4925, 325))
    server.blocks.append(grass_mid(4975, 325))

    game_world.add_object(server.character, 1)
    game_world.add_objects(server.blocks, 0)
    game_world.add_objects(server.ornblocks, 0)
    game_world.add_objects(server.objects, 1)

    music = load_music('background.mp3')
    music.set_volume(16)
    music.repeat_play()

    background = load_image('grass.jpg')

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
        game_framework.change_state(select_state)

    elif server.character.x > 4800:
        server.coin += server.pre_coin
        server.score += server.pre_coin * 100 + 5000
        if server.clear_stage <= 0:
            server.clear_stage = 1
        game_framework.change_state(select_state)
    # 이겼다 판정


    # if left_down:
    #     server.camera_pivot -= 50
    #     if server.camera_pivot < 0:
    #         server.camera_pivot = 0
    #         left_down = False
    #
    # if right_down:
    #     server.camera_pivot += 50
    #     if server.camera_pivot + 800 > 4800:
    #         server.camera_pivot = 4800 - 800
    #         right_down = False

def draw():
    clear_canvas()
    background.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




