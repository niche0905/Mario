import random
import json
import os

import game_framework
import server

import map_1
import map_3

from pico2d import *
import game_world

from player import Mario
from block import hard_brick, soft_brick, grass_left, grass_mid, grass_right, random_block, mush_left, mush_mid, mush_right, pipe_left, pipe_right, mid_left, mid_right, cave_rock

name = "Map2State"

music = None
background = None

def enter():
    global music
    global background
    server.camera_pivot = 0
    server.character = Mario(50, 200)
    server.blocks.append(cave_rock(25, 75)) # 0
    server.blocks.append(cave_rock(75, 75))
    server.blocks.append(cave_rock(125, 75))
    server.blocks.append(cave_rock(175, 75))
    server.blocks.append(cave_rock(225, 75))
    server.blocks.append(cave_rock(275, 75))
    server.blocks.append(cave_rock(325, 75))
    server.blocks.append(cave_rock(375, 75))
    server.blocks.append(cave_rock(425, 75))
    server.blocks.append(cave_rock(475, 75))
    server.blocks.append(cave_rock(525, 75))
    server.blocks.append(cave_rock(575, 75))
    server.blocks.append(cave_rock(625, 75))
    server.blocks.append(cave_rock(675, 75))
    server.blocks.append(cave_rock(725, 75))
    server.blocks.append(cave_rock(775, 75))

    server.ornblocks.append(cave_rock(25, 575))
    server.ornblocks.append(cave_rock(75, 575))
    server.ornblocks.append(cave_rock(125, 575))
    server.ornblocks.append(cave_rock(175, 575))
    server.ornblocks.append(cave_rock(225, 575))
    server.ornblocks.append(cave_rock(275, 575))
    server.ornblocks.append(cave_rock(325, 575))
    server.ornblocks.append(cave_rock(375, 575))
    server.ornblocks.append(cave_rock(425, 575))
    server.ornblocks.append(cave_rock(475, 575))
    server.ornblocks.append(cave_rock(525, 575))
    server.ornblocks.append(cave_rock(575, 575))
    server.ornblocks.append(cave_rock(625, 575))
    server.ornblocks.append(cave_rock(675, 575))
    server.ornblocks.append(cave_rock(725, 575))
    server.ornblocks.append(cave_rock(775, 575))

    server.ornblocks.append(cave_rock(25, 25))
    server.ornblocks.append(cave_rock(75, 25))
    server.ornblocks.append(cave_rock(125, 25))
    server.ornblocks.append(cave_rock(175, 25))
    server.ornblocks.append(cave_rock(225, 25))
    server.ornblocks.append(cave_rock(275, 25))
    server.ornblocks.append(cave_rock(325, 25))
    server.ornblocks.append(cave_rock(375, 25))
    server.ornblocks.append(cave_rock(425, 25))
    server.ornblocks.append(cave_rock(475, 25))
    server.ornblocks.append(cave_rock(525, 25))
    server.ornblocks.append(cave_rock(575, 25))
    server.ornblocks.append(cave_rock(625, 25))
    server.ornblocks.append(cave_rock(675, 25))
    server.ornblocks.append(cave_rock(725, 25))
    server.ornblocks.append(cave_rock(775, 25))

    server.ornblocks.append(cave_rock(825, 575))
    server.ornblocks.append(cave_rock(875, 575))
    server.ornblocks.append(cave_rock(925, 575))
    server.ornblocks.append(cave_rock(975, 575))
    server.ornblocks.append(cave_rock(1025, 575))
    server.ornblocks.append(cave_rock(1075, 575))
    server.ornblocks.append(cave_rock(1125, 575))

    server.blocks.append(cave_rock(1025, 75))
    server.blocks.append(cave_rock(1075, 75))
    server.blocks.append(cave_rock(1125, 75))
    server.blocks.append(cave_rock(1175, 75))
    server.blocks.append(cave_rock(1225, 75))
    server.blocks.append(cave_rock(1275, 75))
    server.blocks.append(cave_rock(1325, 75))
    server.blocks.append(cave_rock(1375, 75))
    server.blocks.append(cave_rock(1425, 75))
    server.blocks.append(cave_rock(1475, 75))
    server.blocks.append(cave_rock(1525, 75))
    server.blocks.append(cave_rock(1575, 75))

    server.blocks.append(cave_rock(1625, 75))
    server.blocks.append(cave_rock(1625, 125))
    server.blocks.append(cave_rock(1625, 175))
    server.blocks.append(cave_rock(1625, 225))
    server.blocks.append(cave_rock(1625, 275))
    server.blocks.append(cave_rock(1625, 325))
    server.blocks.append(cave_rock(1625, 375))
    server.blocks.append(cave_rock(1475, 225))
    server.blocks.append(cave_rock(1425, 225))
    server.blocks.append(cave_rock(1375, 225))
    server.blocks.append(cave_rock(1325, 225))
    server.blocks.append(cave_rock(1275, 225))
    server.blocks.append(cave_rock(1225, 225))
    server.blocks.append(cave_rock(1175, 225))
    server.blocks.append(cave_rock(1175, 275))
    server.blocks.append(cave_rock(1175, 325))
    server.blocks.append(cave_rock(1175, 375))
    server.blocks.append(cave_rock(1175, 425))
    server.blocks.append(cave_rock(1175, 475))
    server.blocks.append(cave_rock(1175, 525))
    server.blocks.append(cave_rock(1175, 575))
    server.blocks.append(cave_rock(1325, 375))
    server.blocks.append(cave_rock(1375, 375))
    server.blocks.append(cave_rock(1425, 375))
    server.blocks.append(cave_rock(1475, 375))
    server.blocks.append(cave_rock(1525, 375))
    server.blocks.append(cave_rock(1575, 375))

    server.blocks.append(cave_rock(1625, 375))
    server.blocks.append(cave_rock(1675, 375))
    server.blocks.append(cave_rock(1225, 575))
    server.blocks.append(cave_rock(1275, 575))
    server.blocks.append(cave_rock(1325, 575))
    server.blocks.append(cave_rock(1375, 575))
    server.blocks.append(cave_rock(1425, 575))
    server.blocks.append(cave_rock(1475, 575))
    server.blocks.append(cave_rock(1525, 575))
    server.blocks.append(cave_rock(1575, 575))
    server.blocks.append(cave_rock(1625, 575))
    server.blocks.append(cave_rock(1675, 575))
    server.blocks.append(cave_rock(1725, 575))
    server.blocks.append(cave_rock(1775, 575))


    game_world.add_object(server.character, 1)
    game_world.add_objects(server.blocks, 0)
    game_world.add_objects(server.ornblocks, 0)
    game_world.add_objects(server.objects, 1)

    music = load_music('background.mp3')
    music.set_volume(16)
    music.repeat_play()

    background = load_image('cave.jpg')

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
                game_framework.quit()
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
            elif event.key == SDLK_3:
                game_framework.change_state(map_1)
            elif event.key == SDLK_5:
                game_framework.change_state(map_3)
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

    if server.character.x > 4800:
        server.coin += server.pre_coin
        server.score += server.pre_coin * 100 + 5000
        pass
    # 이겼다 판정

    if server.character.if_die():
        pass

def draw():
    clear_canvas()
    background.clip_draw(0, 0, 500, 304, 400, 300, 800, 600)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




