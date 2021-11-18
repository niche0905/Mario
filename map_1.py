import random
import json
import os

import game_framework

import map_1
import map_2
import map_3

from pico2d import *
import game_world

from block import hard_brick, soft_brick, grass_left, grass_mid, grass_right, random_block, mush_left, mush_mid, mush_right, pipe_left, pipe_right, mid_left, mid_right

name = "Map1State"

blocks = []

left_down = None
right_down = None

camera_left, camera_right = None, None

def enter():
    global left_down, right_down
    left_down = False
    right_down = False
    global camera_left, camera_right
    camera_left, camera_right = 0, 800
    global blocks
    blocks.append(grass_mid(25, 25)) # 0
    blocks.append(grass_mid(75, 25))
    blocks.append(grass_mid(125, 25))
    blocks.append(grass_mid(175, 25))
    blocks.append(grass_mid(225, 25))
    blocks.append(grass_mid(275, 25))
    blocks.append(grass_mid(325, 25))
    blocks.append(grass_mid(375, 25))
    blocks.append(grass_mid(425, 25))
    blocks.append(grass_mid(475, 25))
    blocks.append(grass_mid(525, 25))
    blocks.append(grass_mid(575, 25))
    blocks.append(grass_mid(625, 25))
    blocks.append(grass_mid(675, 25))
    blocks.append(grass_mid(725, 25))
    blocks.append(grass_mid(775, 25))

    blocks.append(soft_brick(375, 325))
    blocks.append(soft_brick(425, 325))
    blocks.append(soft_brick(475, 325))
    blocks.append(random_block(525, 325))
    blocks.append(soft_brick(575, 325))
    blocks.append(soft_brick(625, 325))
    blocks.append(soft_brick(675, 325))

    # blocks.append(grass_mid(25, 25)) # 800
    # blocks.append(grass_mid(75, 25))
    # blocks.append(grass_mid(125, 25))
    # blocks.append(grass_mid(175, 25))
    # blocks.append(grass_mid(225, 25))
    # blocks.append(grass_mid(275, 25))
    # blocks.append(grass_right(325, 25))
    #
    # blocks.append(grass_left(525, 25))
    # blocks.append(grass_mid(575, 25))
    # blocks.append(grass_mid(625, 25))
    # blocks.append(grass_mid(675, 25))
    # blocks.append(grass_mid(725, 25))
    # blocks.append(grass_mid(775, 25))

    # blocks.append(grass_mid(25, 25)) # 1600
    # blocks.append(grass_mid(75, 25))
    # blocks.append(pipe_left(75, 175))
    # blocks.append(pipe_right(125, 175))
    # blocks.append(mid_left(75, 125))
    # blocks.append(mid_right(125, 125))
    # blocks.append(mid_left(75, 75))
    # blocks.append(mid_right(125, 75))
    # blocks.append(grass_mid(125, 25))
    # blocks.append(grass_mid(175, 25))
    # blocks.append(grass_mid(225, 25))
    # blocks.append(grass_mid(275, 25))
    # blocks.append(grass_mid(325, 25))
    # blocks.append(grass_mid(375, 25))
    # blocks.append(grass_mid(425, 25))
    # blocks.append(grass_mid(475, 25))
    # blocks.append(grass_mid(525, 25))
    # blocks.append(grass_mid(575, 25))
    # blocks.append(grass_mid(625, 25))
    # blocks.append(grass_mid(675, 25))
    # blocks.append(grass_mid(725, 25))
    # blocks.append(grass_mid(775, 25))
    #
    # blocks.append(soft_brick(375, 375))
    # blocks.append(soft_brick(425, 375))
    # blocks.append(soft_brick(475, 375))
    # blocks.append(soft_brick(525, 375))
    # blocks.append(soft_brick(575, 375))
    # blocks.append(soft_brick(625, 375))

    # blocks.append(grass_mid(25, 25)) # 2400
    # blocks.append(grass_mid(75, 25))
    # blocks.append(grass_mid(125, 25))
    # blocks.append(grass_mid(175, 25))
    # blocks.append(grass_mid(225, 25))
    # blocks.append(grass_mid(275, 25))
    # blocks.append(grass_mid(325, 25))
    # blocks.append(grass_mid(375, 25))
    # blocks.append(grass_right(425, 25))
    #
    # blocks.append(grass_left(575, 75))
    # blocks.append(grass_mid(625, 75))
    # blocks.append(grass_mid(675, 75))
    # blocks.append(grass_mid(725, 75))
    # blocks.append(grass_mid(775, 75))

    # blocks.append(grass_mid(25, 75))  # 3200
    # blocks.append(grass_mid(75, 75))
    # blocks.append(grass_mid(125, 75))
    # blocks.append(grass_mid(175, 75))
    # blocks.append(grass_mid(225, 75))
    # blocks.append(grass_mid(275, 75))
    # blocks.append(grass_mid(325, 75))
    # blocks.append(grass_mid(375, 75))
    # blocks.append(grass_mid(425, 75))
    # blocks.append(grass_mid(475, 75))
    # blocks.append(grass_mid(525, 75))
    # blocks.append(grass_right(575, 75))
    # blocks.append(grass_mid(625, 25))
    # blocks.append(grass_mid(675, 25))
    # blocks.append(grass_mid(725, 25))
    # blocks.append(grass_mid(775, 25))

    # blocks.append(grass_right(25, 25))  # 4000
    # blocks.append(grass_left(225, 25))
    # blocks.append(grass_left(275, 75))
    # blocks.append(grass_left(325, 125))
    # blocks.append(grass_left(375, 175))
    # blocks.append(grass_left(425, 225))
    # blocks.append(grass_left(475, 275))
    # blocks.append(grass_left(525, 325))

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
    global left_down, right_down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_LEFT:
                left_down = True
                right_down = False
            elif event.key == SDLK_RIGHT:
                right_down = True
                left_down = False
            elif event.key == SDLK_3:
                game_framework.change_state(map_1)
            elif event.key == SDLK_4:
                game_framework.change_state(map_2)
            elif event.key == SDLK_5:
                game_framework.change_state(map_3)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left_down = False
            elif event.key == SDLK_RIGHT:
                right_down = False



def update():
    global left_down, right_down
    global camera_left, camera_right
    for game_object in game_world.all_objects():
        game_object.update()
    if left_down:
        camera_left -= 5
        camera_right -= 5
        if camera_left < 0:
            camera_left = 0
            camera_right = 80
            left_down = False

    if right_down:
        camera_left += 5
        camera_right += 5
        if camera_right > 4800:
            camera_left = 4000
            camera_right = 4800
            right_down = False

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




