import random
import json
import os

import game_framework
import server

import map_2
import map_3

from pico2d import *
import game_world

from player import Mario
from block import hard_brick, soft_brick, grass_left, grass_mid, grass_right, random_block, mush_left, mush_mid, mush_right, pipe_left, pipe_right, mid_left, mid_right

name = "Map1State"

def enter():
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

    game_world.add_object(server.character, 1)
    game_world.add_objects(server.blocks, 0)

def exit():
    game_world.clear()
    server.character = None
    server.blocks = []
    server.camera_pivot = 0

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
    global left_down, right_down
    for game_object in game_world.all_objects():
        game_object.update()

    if server.character.x < 0:
        server.characterx = 0
    if server.character.x >= 400 and server.character.x <= 4800 - 400:
        server.camera_pivot = server.character.x - 400

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
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




