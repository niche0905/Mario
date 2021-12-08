import random
import json
import os

from pico2d import *

import game_framework
import map_1
import map_2
import map_3
import main_state
import server

import game_world


name = "SelectState"

background = None
s1_image = None
s2_image = None
s3_image = None
coin_image = None
font = None

def enter():
    global background, s1_image, s2_image, s3_image, coin_image, font
    background = load_image('white.png')
    s1_image = load_image('grass.jpg')
    s2_image = load_image('cave.jpg')
    s3_image = load_image('sky.jpg')
    coin_image = load_image('mario2.png')
    font = load_font('ENCR10B.TTF', 32)

def exit():
    global background, s1_image, s2_image, s3_image, coin_image, font
    background = None
    s1_image = None
    s2_image = None
    s3_image = None
    coin_image = None
    font = None

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
            elif event.key == SDLK_s:
                pass
            elif event.key == SDLK_p:
                game_framework.change_state(main_state)
            # 정보를 저장해보거라
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x >= 50 and event.x <= 750:
                if event.y >= 25 and event.y <= 175:
                    if server.clear_stage >= 0:
                        game_framework.change_state(map_1)
                elif event.y >= 205 and event.y <= 355:
                    if server.clear_stage >= 1:
                        game_framework.change_state(map_2)
                elif event.y >= 385 and event.y <= 535:
                    if server.clear_stage >= 2:
                        game_framework.change_state(map_3)



def update():
    pass
    # 스테이트 바꾸기





def draw():
    clear_canvas()
    background.clip_draw(0, 0, 752, 1336, 400, 300, 800, 600)
    s1_image.clip_draw(0, 0, 1280, 1024, 400, 460, 700, 150)
    s2_image.clip_draw(0, 0, 500, 304, 400, 280, 700, 150)
    s3_image.clip_draw(0, 0, 510, 340, 400, 100, 700, 150)
    coin_image.clip_draw(48, 64, 48, 48, 775, 575, 48, 48)
    font.draw(700, 575, '%d' % server.coin, (0, 0, 0))
    font.draw(50, 575, 'score: %d' % server.score, (0, 0, 0))
    update_canvas()
