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
from mapper import mapper
from SimulationPanel import SimulationPanel
from Timer import Timer
from tkinter import *
import sys


def main():
    wsizex = 512
    wsizey = 512
    margin = 10
    root = Tk()
    root.title(" Simulador de Doenças ")
    world = MyWorld()
    # maps the world rectangle onto a viewport of wsizex x wsizey pixels .
    canvas = Canvas(root, width=512, height=512, background='dark grey')
    sp = SimulationPanel(world, canvas)
    sp.wvmap = mapper([0, 0, world.getWidth() - 1, world.getHeight() - 1], [margin, margin, wsizex - margin, wsizey - margin], False, False)
    print([0, 0, world.getWidth() - 1, world.getHeight() - 1], [margin, margin, wsizex - margin, wsizey - margin])
    poll = Timer(root, sp.draw, 500)
    canvas.bind("<Configure>", sp.resize)
    root.bind("<Escape>", lambda _: root.destroy())
    root.bind("s", lambda _: poll.stop())
    root.bind("r", lambda _: poll.restart())
    root.bind("p", sp.printData)
    root.bind("<Button-1>", lambda e: sp.mousePressed(e))
    poll.run()
    root.mainloop()

main()

if __name__ == ' __main__ ':
    sys.exit(main())
