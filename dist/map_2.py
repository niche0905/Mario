import random
import json
import os

import game_framework
import server

import select_state

from pico2d import *
import game_world

from player import Mario
from block import soft_brick, pipe_left, pipe_right, mid_left, mid_right, pipe_top, pipe_bottom, mid_top, mid_bottom, cave_rock
from enemy import Goomba, Koopa, Hammer_bro
from object import coin, mushroom

name = "Map2State"

music = None
background = None

def enter():
    global music
    global background
    server.camera_pivot = 0
    server.character = Mario(50, 200, server.character_state)
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

    server.enemys.append(Goomba(1500, 125))

    server.ornblocks.append(cave_rock(1025, 25))
    server.ornblocks.append(cave_rock(1075, 25))
    server.ornblocks.append(cave_rock(1125, 25))
    server.ornblocks.append(cave_rock(1175, 25))
    server.ornblocks.append(cave_rock(1225, 25))
    server.ornblocks.append(cave_rock(1275, 25))
    server.ornblocks.append(cave_rock(1325, 25))
    server.ornblocks.append(cave_rock(1375, 25))
    server.ornblocks.append(cave_rock(1425, 25))
    server.ornblocks.append(cave_rock(1475, 25))
    server.ornblocks.append(cave_rock(1525, 25))
    server.ornblocks.append(cave_rock(1575, 25))
    server.ornblocks.append(cave_rock(1625, 25))

    server.objects.append(coin(1525, 225))
    server.objects.append(coin(1575, 225))

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

    server.objects.append(coin(1225, 375))
    server.objects.append(coin(1275, 375))

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

    server.enemys.append(Koopa (1500, 425))

    server.blocks.append(cave_rock(1625, 375))
    server.blocks.append(cave_rock(1675, 375))
    server.blocks.append(cave_rock(1675, 325))
    server.blocks.append(cave_rock(1675, 275))
    server.blocks.append(cave_rock(1675, 225))
    server.blocks.append(cave_rock(1675, 175))
    server.blocks.append(cave_rock(1675, 125))
    server.blocks.append(cave_rock(1675, 75))
    server.blocks.append(cave_rock(1675, 25))

    server.blocks.append(soft_brick(1725, 375))
    server.blocks.append(soft_brick(1775, 375))
    server.blocks.append(soft_brick(1825, 375))

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
    server.blocks.append(cave_rock(1825, 575))
    server.blocks.append(cave_rock(1875, 575))
    server.blocks.append(cave_rock(1925, 575))
    server.blocks.append(cave_rock(1875, 575))

    server.blocks.append(cave_rock(1925, 575))
    server.blocks.append(cave_rock(1975, 575))
    server.blocks.append(cave_rock(2025, 575))
    server.blocks.append(cave_rock(2075, 575))
    server.blocks.append(cave_rock(2125, 575))
    server.blocks.append(cave_rock(2175, 575))
    server.blocks.append(cave_rock(2225, 575))
    server.blocks.append(cave_rock(2275, 575))
    server.blocks.append(cave_rock(2325, 575))
    server.blocks.append(cave_rock(2375, 575))
    server.blocks.append(cave_rock(2425, 575))
    server.blocks.append(cave_rock(2475, 575))
    server.blocks.append(cave_rock(2525, 575))
    server.blocks.append(cave_rock(2575, 575))
    server.blocks.append(cave_rock(2625, 575))
    server.blocks.append(cave_rock(2675, 575))
    server.blocks.append(cave_rock(2725, 575))
    server.blocks.append(cave_rock(2775, 575))
    server.blocks.append(cave_rock(2825, 575))
    server.blocks.append(cave_rock(2875, 575))
    server.blocks.append(cave_rock(2925, 575))
    server.blocks.append(cave_rock(2975, 575))
    server.blocks.append(cave_rock(3025, 575))
    server.blocks.append(cave_rock(3075, 575))
    server.blocks.append(cave_rock(3125, 575))
    server.blocks.append(cave_rock(3175, 575))
    server.blocks.append(cave_rock(3225, 575))
    server.blocks.append(cave_rock(3275, 575))
    server.blocks.append(cave_rock(3325, 575))
    server.blocks.append(cave_rock(3375, 575))
    server.blocks.append(cave_rock(3425, 575))
    server.blocks.append(cave_rock(3475, 575))
    server.blocks.append(cave_rock(3525, 575))
    server.blocks.append(cave_rock(3575, 575))
    server.blocks.append(cave_rock(3625, 575))
    server.blocks.append(cave_rock(3675, 575))
    server.blocks.append(cave_rock(3725, 575))
    server.blocks.append(cave_rock(3775, 575))
    server.blocks.append(cave_rock(3825, 575))
    server.blocks.append(cave_rock(3875, 575))
    server.blocks.append(cave_rock(3925, 575))
    server.blocks.append(cave_rock(3975, 575))
    server.blocks.append(cave_rock(4025, 575))
    server.blocks.append(cave_rock(4075, 575))
    server.blocks.append(cave_rock(4125, 575))
    server.blocks.append(cave_rock(4175, 575))
    server.blocks.append(cave_rock(4225, 575))
    server.blocks.append(cave_rock(4275, 575))
    server.blocks.append(cave_rock(4325, 575))
    server.blocks.append(cave_rock(4375, 575))
    server.blocks.append(cave_rock(4425, 575))
    server.blocks.append(cave_rock(4475, 575))
    server.blocks.append(cave_rock(4525, 575))
    server.blocks.append(cave_rock(4575, 575))
    server.blocks.append(cave_rock(4625, 575))
    server.blocks.append(cave_rock(4675, 575))
    server.blocks.append(cave_rock(4725, 575))
    server.blocks.append(cave_rock(4775, 575))

    server.blocks.append(cave_rock(1875, 525))
    server.blocks.append(cave_rock(1875, 475))
    server.blocks.append(cave_rock(1875, 425))
    server.blocks.append(cave_rock(1875, 375))
    server.blocks.append(cave_rock(1875, 325))
    server.blocks.append(cave_rock(1875, 275))
    server.blocks.append(cave_rock(1875, 225))
    server.blocks.append(cave_rock(1875, 175))

    server.blocks.append(cave_rock(1725, 25))
    server.blocks.append(cave_rock(1775, 25))
    server.blocks.append(cave_rock(1825, 25))
    server.blocks.append(cave_rock(1875, 25))
    server.blocks.append(cave_rock(1925, 25))
    server.blocks.append(cave_rock(1975, 25))
    server.blocks.append(cave_rock(2025, 25))
    server.blocks.append(cave_rock(2075, 25))
    server.blocks.append(cave_rock(2125, 75))
    server.blocks.append(cave_rock(2175, 125))
    server.blocks.append(cave_rock(2225, 175))
    server.blocks.append(cave_rock(2275, 225))
    server.blocks.append(cave_rock(2325, 225))
    server.blocks.append(cave_rock(2375, 225))
    server.blocks.append(cave_rock(2425, 225))
    server.blocks.append(cave_rock(2475, 225))

    server.enemys.append(Goomba(2400, 275))

    server.ornblocks.append(cave_rock(2525, 225))
    server.ornblocks.append(cave_rock(2575, 225))

    server.ornblocks.append(cave_rock(2125, 25))
    server.ornblocks.append(cave_rock(2175, 25))
    server.ornblocks.append(cave_rock(2225, 25))
    server.ornblocks.append(cave_rock(2275, 25))
    server.ornblocks.append(cave_rock(2325, 25))
    server.ornblocks.append(cave_rock(2375, 25))
    server.ornblocks.append(cave_rock(2425, 25))
    server.blocks.append(cave_rock(2475, 25))
    server.ornblocks.append(cave_rock(2525, 25))
    server.ornblocks.append(cave_rock(2575, 25))
    server.blocks.append(cave_rock(2625, 25))
    server.ornblocks.append(cave_rock(2675, 25))
    server.ornblocks.append(cave_rock(2725, 25))
    server.ornblocks.append(cave_rock(2775, 25))
    server.ornblocks.append(cave_rock(2825, 25))

    server.ornblocks.append(cave_rock(2175, 75))
    server.ornblocks.append(cave_rock(2225, 75))
    server.ornblocks.append(cave_rock(2275, 75))
    server.ornblocks.append(cave_rock(2325, 75))
    server.ornblocks.append(cave_rock(2375, 75))
    server.ornblocks.append(cave_rock(2425, 75))
    server.blocks.append(cave_rock(2475, 75))
    server.ornblocks.append(cave_rock(2525, 75))
    server.ornblocks.append(cave_rock(2575, 75))
    server.blocks.append(cave_rock(2625, 75))
    server.ornblocks.append(cave_rock(2675, 75))
    server.ornblocks.append(cave_rock(2725, 75))
    server.ornblocks.append(cave_rock(2775, 75))

    server.ornblocks.append(cave_rock(2225, 125))
    server.ornblocks.append(cave_rock(2275, 125))
    server.ornblocks.append(cave_rock(2325, 125))
    server.ornblocks.append(cave_rock(2375, 125))
    server.ornblocks.append(cave_rock(2425, 125))
    server.blocks.append(cave_rock(2475, 125))
    server.ornblocks.append(cave_rock(2525, 125))
    server.ornblocks.append(cave_rock(2575, 125))
    server.blocks.append(cave_rock(2625, 125))
    server.ornblocks.append(cave_rock(2675, 125))
    server.ornblocks.append(cave_rock(2725, 125))

    server.ornblocks.append(cave_rock(2275, 175))
    server.ornblocks.append(cave_rock(2325, 175))
    server.ornblocks.append(cave_rock(2375, 175))
    server.ornblocks.append(cave_rock(2425, 175))
    server.blocks.append(cave_rock(2475, 175))
    server.ornblocks.append(cave_rock(2525, 175))
    server.ornblocks.append(cave_rock(2575, 175))
    server.blocks.append(cave_rock(2625, 175))
    server.ornblocks.append(cave_rock(2675, 175))

    server.blocks.append(cave_rock(2625, 225))
    server.blocks.append(cave_rock(2675, 225))
    server.blocks.append(cave_rock(2725, 175))
    server.blocks.append(cave_rock(2775, 125))
    server.blocks.append(cave_rock(2825, 75))

    server.blocks.append(cave_rock(3125, 75))
    server.blocks.append(cave_rock(3175, 75))
    server.blocks.append(cave_rock(3225, 75))
    server.blocks.append(cave_rock(3275, 75))

    server.ornblocks.append(cave_rock(3125, 25))
    server.ornblocks.append(cave_rock(3175, 25))
    server.ornblocks.append(cave_rock(3225, 25))
    server.ornblocks.append(cave_rock(3275, 25))

    server.blocks.append(cave_rock(3325, 75))
    server.blocks.append(cave_rock(3375, 75))
    server.blocks.append(mid_left(3325, 125))
    server.blocks.append(mid_right(3375, 125))
    server.blocks.append(pipe_left(3325, 175))
    server.blocks.append(pipe_right(3375, 175))

    server.objects.append(coin(3325, 225))
    server.objects.append(coin(3375, 225))

    server.ornblocks.append(cave_rock(3325, 25))
    server.ornblocks.append(cave_rock(3375, 25))

    server.blocks.append(cave_rock(3525, 75))
    server.blocks.append(cave_rock(3575, 75))
    server.blocks.append(mid_left(3525, 125))
    server.blocks.append(mid_right(3575, 125))
    server.blocks.append(mid_left(3525, 175))
    server.blocks.append(mid_right(3575, 175))
    server.blocks.append(mid_left(3525, 225))
    server.blocks.append(mid_right(3575, 225))
    server.blocks.append(pipe_left(3525, 275))
    server.blocks.append(pipe_right(3575, 275))

    server.objects.append(coin(3525, 325))
    server.objects.append(coin(3575, 325))

    server.ornblocks.append(cave_rock(3525, 25))
    server.ornblocks.append(cave_rock(3575, 25))

    server.blocks.append(cave_rock(3725, 75))
    server.blocks.append(cave_rock(3775, 75))
    server.blocks.append(mid_left(3725, 125))
    server.blocks.append(mid_right(3775, 125))
    server.blocks.append(mid_left(3725, 175))
    server.blocks.append(mid_right(3775, 175))
    server.blocks.append(mid_left(3725, 225))
    server.blocks.append(mid_right(3775, 225))
    server.blocks.append(mid_left(3725, 275))
    server.blocks.append(mid_right(3775, 275))
    server.blocks.append(mid_left(3725, 325))
    server.blocks.append(mid_right(3775, 325))
    server.blocks.append(pipe_left(3725, 375))
    server.blocks.append(pipe_right(3775, 375))

    server.objects.append(coin(3725, 425))
    server.objects.append(coin(3775, 425))

    server.ornblocks.append(cave_rock(3725, 25))
    server.ornblocks.append(cave_rock(3775, 25))

    server.blocks.append(cave_rock(3925, 375))
    server.blocks.append(cave_rock(3925, 325))
    server.blocks.append(cave_rock(3925, 275))
    server.blocks.append(cave_rock(3925, 225))
    server.blocks.append(cave_rock(3925, 175))
    server.blocks.append(cave_rock(3925, 125))
    server.blocks.append(cave_rock(3925, 75))
    server.blocks.append(cave_rock(3925, 25))

    server.ornblocks.append(cave_rock(3975, 325))
    server.ornblocks.append(cave_rock(4025, 325))
    server.ornblocks.append(cave_rock(4075, 325))
    server.ornblocks.append(cave_rock(4125, 325))
    server.ornblocks.append(cave_rock(4175, 325))
    server.ornblocks.append(cave_rock(4225, 325))
    server.ornblocks.append(cave_rock(4275, 325))
    server.ornblocks.append(cave_rock(4325, 325))
    server.ornblocks.append(cave_rock(4375, 325))
    server.ornblocks.append(cave_rock(4425, 325))
    server.ornblocks.append(cave_rock(4475, 325))
    server.ornblocks.append(cave_rock(4525, 325))
    server.ornblocks.append(cave_rock(4575, 325))
    server.ornblocks.append(cave_rock(4625, 325))
    server.ornblocks.append(cave_rock(4675, 325))
    server.ornblocks.append(cave_rock(4725, 325))
    server.ornblocks.append(cave_rock(4775, 325))
    server.ornblocks.append(cave_rock(4775, 325))

    server.ornblocks.append(cave_rock(3975, 275))
    server.ornblocks.append(cave_rock(4025, 275))
    server.ornblocks.append(cave_rock(4075, 275))
    server.ornblocks.append(cave_rock(4125, 275))
    server.ornblocks.append(cave_rock(4175, 275))
    server.ornblocks.append(cave_rock(4225, 275))
    server.ornblocks.append(cave_rock(4275, 275))
    server.ornblocks.append(cave_rock(4325, 275))
    server.ornblocks.append(cave_rock(4375, 275))
    server.ornblocks.append(cave_rock(4425, 275))
    server.ornblocks.append(cave_rock(4475, 275))
    server.ornblocks.append(cave_rock(4525, 275))
    server.ornblocks.append(cave_rock(4575, 275))
    server.ornblocks.append(cave_rock(4625, 275))
    server.ornblocks.append(cave_rock(4675, 275))
    server.ornblocks.append(cave_rock(4725, 275))
    server.ornblocks.append(cave_rock(4775, 275))
    server.ornblocks.append(cave_rock(4775, 275))

    server.ornblocks.append(cave_rock(3975, 225))
    server.ornblocks.append(cave_rock(4025, 225))
    server.ornblocks.append(cave_rock(4075, 225))
    server.ornblocks.append(cave_rock(4125, 225))
    server.ornblocks.append(cave_rock(4175, 225))
    server.ornblocks.append(cave_rock(4225, 225))
    server.ornblocks.append(cave_rock(4275, 225))
    server.ornblocks.append(cave_rock(4325, 225))
    server.ornblocks.append(cave_rock(4375, 225))
    server.ornblocks.append(cave_rock(4425, 225))
    server.ornblocks.append(cave_rock(4475, 225))
    server.ornblocks.append(cave_rock(4525, 225))
    server.ornblocks.append(cave_rock(4575, 225))
    server.ornblocks.append(cave_rock(4625, 225))
    server.ornblocks.append(cave_rock(4675, 225))
    server.ornblocks.append(cave_rock(4725, 225))
    server.ornblocks.append(cave_rock(4775, 225))
    server.ornblocks.append(cave_rock(4775, 225))

    server.ornblocks.append(cave_rock(3975, 175))
    server.ornblocks.append(cave_rock(4025, 175))
    server.ornblocks.append(cave_rock(4075, 175))
    server.ornblocks.append(cave_rock(4125, 175))
    server.ornblocks.append(cave_rock(4175, 175))
    server.ornblocks.append(cave_rock(4225, 175))
    server.ornblocks.append(cave_rock(4275, 175))
    server.ornblocks.append(cave_rock(4325, 175))
    server.ornblocks.append(cave_rock(4375, 175))
    server.ornblocks.append(cave_rock(4425, 175))
    server.ornblocks.append(cave_rock(4475, 175))
    server.ornblocks.append(cave_rock(4525, 175))
    server.ornblocks.append(cave_rock(4575, 175))
    server.ornblocks.append(cave_rock(4625, 175))
    server.ornblocks.append(cave_rock(4675, 175))
    server.ornblocks.append(cave_rock(4725, 175))
    server.ornblocks.append(cave_rock(4775, 175))
    server.ornblocks.append(cave_rock(4775, 175))

    server.ornblocks.append(cave_rock(3975, 125))
    server.ornblocks.append(cave_rock(4025, 125))
    server.ornblocks.append(cave_rock(4075, 125))
    server.ornblocks.append(cave_rock(4125, 125))
    server.ornblocks.append(cave_rock(4175, 125))
    server.ornblocks.append(cave_rock(4225, 125))
    server.ornblocks.append(cave_rock(4275, 125))
    server.ornblocks.append(cave_rock(4325, 125))
    server.ornblocks.append(cave_rock(4375, 125))
    server.ornblocks.append(cave_rock(4425, 125))
    server.ornblocks.append(cave_rock(4475, 125))
    server.ornblocks.append(cave_rock(4525, 125))
    server.ornblocks.append(cave_rock(4575, 125))
    server.ornblocks.append(cave_rock(4625, 125))
    server.ornblocks.append(cave_rock(4675, 125))
    server.ornblocks.append(cave_rock(4725, 125))
    server.ornblocks.append(cave_rock(4775, 125))
    server.ornblocks.append(cave_rock(4775, 125))

    server.ornblocks.append(cave_rock(3975, 75))
    server.ornblocks.append(cave_rock(4025, 75))
    server.ornblocks.append(cave_rock(4075, 75))
    server.ornblocks.append(cave_rock(4125, 75))
    server.ornblocks.append(cave_rock(4175, 75))
    server.ornblocks.append(cave_rock(4225, 75))
    server.ornblocks.append(cave_rock(4275, 75))
    server.ornblocks.append(cave_rock(4325, 75))
    server.ornblocks.append(cave_rock(4375, 75))
    server.ornblocks.append(cave_rock(4425, 75))
    server.ornblocks.append(cave_rock(4475, 75))
    server.ornblocks.append(cave_rock(4525, 75))
    server.ornblocks.append(cave_rock(4575, 75))
    server.ornblocks.append(cave_rock(4625, 75))
    server.ornblocks.append(cave_rock(4675, 75))
    server.ornblocks.append(cave_rock(4725, 75))
    server.ornblocks.append(cave_rock(4775, 75))
    server.ornblocks.append(cave_rock(4775, 75))

    server.ornblocks.append(cave_rock(3975, 25))
    server.ornblocks.append(cave_rock(4025, 25))
    server.ornblocks.append(cave_rock(4075, 25))
    server.ornblocks.append(cave_rock(4125, 25))
    server.ornblocks.append(cave_rock(4175, 25))
    server.ornblocks.append(cave_rock(4225, 25))
    server.ornblocks.append(cave_rock(4275, 25))
    server.ornblocks.append(cave_rock(4325, 25))
    server.ornblocks.append(cave_rock(4375, 25))
    server.ornblocks.append(cave_rock(4425, 25))
    server.ornblocks.append(cave_rock(4475, 25))
    server.ornblocks.append(cave_rock(4525, 25))
    server.ornblocks.append(cave_rock(4575, 25))
    server.ornblocks.append(cave_rock(4625, 25))
    server.ornblocks.append(cave_rock(4675, 25))
    server.ornblocks.append(cave_rock(4725, 25))
    server.ornblocks.append(cave_rock(4775, 25))
    server.ornblocks.append(cave_rock(4775, 25))

    server.enemys.append(Hammer_bro(4200, 425))

    server.blocks.append(cave_rock(3975, 375))
    server.blocks.append(cave_rock(4025, 375))
    server.blocks.append(cave_rock(4075, 375))
    server.blocks.append(cave_rock(4125, 375))
    server.blocks.append(cave_rock(4175, 375))
    server.blocks.append(cave_rock(4225, 375))
    server.blocks.append(cave_rock(4275, 375))
    server.blocks.append(cave_rock(4325, 375))
    server.blocks.append(cave_rock(4375, 375))
    server.blocks.append(cave_rock(4425, 375))
    server.blocks.append(cave_rock(4475, 375))
    server.blocks.append(cave_rock(4525, 375))
    server.blocks.append(cave_rock(4575, 375))
    server.blocks.append(cave_rock(4625, 375))
    server.blocks.append(cave_rock(4675, 375))
    server.blocks.append(cave_rock(4725, 375))
    server.blocks.append(cave_rock(4775, 375))
    server.blocks.append(cave_rock(4725, 525))
    server.blocks.append(cave_rock(4775, 525))

    server.ornblocks.append(pipe_top(4725, 475))
    server.ornblocks.append(pipe_bottom(4725, 425))
    server.ornblocks.append(mid_top(4775, 475))
    server.ornblocks.append(mid_bottom(4775, 425))

    game_world.add_object(server.character, 1)
    game_world.add_objects(server.enemys, 1)
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
        if server.clear_stage <= 1:
            server.clear_stage = 2
        game_framework.change_state(select_state)
    # 이겼다 판정


def draw():
    clear_canvas()
    background.clip_draw(0, 0, 500, 304, 400, 300, 800, 600)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()




