#!/usr/bin/env python
# coding: UTF-8
#
# @package Simulator
#
# @author Viviane Magalhães Siqueira (based on Professor Paulo Roma's work)
# @date 10/08/2020
#

from Actor import Actor
from MyWorld import MyWorld
from World import World
from sys import argv


def main(args=None):
    numItr = 5
    if len(args) > 1:
        numItr = (args[1])
    print('Simulation of MyWorld')
    world = MyWorld()
    for x in range(numItr):
        world.act()
        obj = world.getObjects()
        for each in obj:
            each.act()
    print('Simulation of World')
    world = World(100, 100)
    world.addObject(Actor(), 10, 10)
    world.addObject(Actor(), 90, 90)
    for x in range(numItr):
        world.act()
        obj = world.getObjects()
        for each in obj:
            each.act()


if __name__ == '__main__':
    main(argv)
