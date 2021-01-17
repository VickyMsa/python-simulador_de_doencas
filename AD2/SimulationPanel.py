#!/usr/bin/env python
# coding: UTF-8
#
# @package Simulator
#
# @author Viviane Magalhães Siqueira
# @date 18/10/2020
#

from tkinter import *
from Disease import Disease
import random


class SimulationPanel:

    def __init__(self, world, canvas):
        self.world = world
        self.canvas = canvas
        self.canvas.pack()
        self.wvmap = None
        self.width = getint(canvas.cget('width'))
        self.height = getint(canvas.cget('height'))
        self.diseases = world.getObjects()
        self.dict = {}
        self.fromCoordinates(self.diseases)
        self.raio = 0


    def fromCoordinates(self, location):
        self.dict = {(actor.getX(), actor.getY()): actor.getStrength() for actor in location}


    def draw(self):
        self.canvas.delete('all')
        color = f'#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}'
        self.canvas.create_line(0, self.height / 2, self.height, self.width / 2, fill="red", width=2)
        self.canvas.create_line(self.width / 2, 0, self.width / 2, self.height, fill="red", width=2)
        aux = 0

        for coord, raio in self.dict.items():
            x = coord[0]
            y = coord[1]
            r = raio
            X, Y = self.wvmap.windowVecToViewport(x, y)
            quad = self.diseases[aux].getQuadrant()
            if quad == 0:
                self.raio = min(X, Y, self.width / 2 - X, self.height / 2 - Y)
            elif quad == 1:
                self.raio = min(X - self.width / 2, Y, self.width - X, self.height / 2 - Y)
            elif quad == 2:
                self.raio = min(X, Y - self.height / 2, self.width / 2 - X, self.height - Y)
            elif quad == 3:
                self.raio = min(X - self.width / 2, Y - self.height / 2, self.width - X, self.height - Y)

            self.canvas.create_oval(X - r, Y - r, X + r, Y + r, fill=color)
            self.diseases[aux].act()
            self.dict[coord] = (self.diseases[aux].getStrength()) % self.raio
            aux += 1


    def resize(self, e):
        pass


    def printData(self, e):
        pass


    def mousePressed(self, e):
        x, y = self.wvmap.viewportToWindow(e.x, e.y)
        disease = Disease()
        disease.addedToWorld(self.world)
        disease.setLocation(x, y)
        quad = disease.getQuadrant()
        self.diseases.append(disease)

        if quad >= 0 or quad <= 3:
            disease.setGrowthCondition(self.world.getTemp(quad) - 1, self.world.getTemp(quad) + 1, 2.0)
            self.dict[(round(disease.getX()), round(disease.getY()))] = disease.getStrength()
