# -*- coding: cp1252 -*-
from bot_interface import *
import math
import random

EPS = 10**-4
BACK = .8
FORTH = .6
LEFT = .8
RIGHT = .4

class StupidBot(BotBase):
    def process(self, gamestate):
        back = BACK
        forth = FORTH
        left = LEFT
        right = RIGHT

        for uid, rock in gamestate.rocks.items():
            if self.samedir(rock):
                if random.random() < .5:
                    left *= 1.6
                else:
                    right *= 1.6

        thrust = random.uniform(-back, forth)
        sideThrust = random.uniform(-left, right)
        shoot = random.uniform(0, 3)
        
        return Action(
            thrust,
            sideThrust,
            sideThrust,
            shoot)

    def aimToPoint(self, x, y):
        pass

    def getSlope(self):
        return math.tan(math.atan(self.y/self.x)-self.ang)

    def goto(self, x1, y1):
        x0 = self.posx
        y0 = self.poxy
        dx = x1-x0
        dy = y1-y0

    def samedir(self, obj):
        xa, ya = self.posx, self.posy
        xb, yb = obj.posx, obj.posy
        a1 = xa-xb
        b1 = ya-yb
        a2 = obj.velx
        b2 = obj.vely
        return (a1*b2-a2*b1) < EPS

    def distTo(self, obj):
        x0, y0 = self.posx, self.posy
        x1, y1 = obj.posx, obj.posy
        dx = abs(x1-x0)
        dy = abs(y1-y0)
        return math.sqrt(dx+dy)

    def distTo(self, x1, y1):
        x0, y0 = self.posx, self.posy
        dx = abs(x1-x0)
        dy = abs(y1-y0)
        return math.sqrt(dx+dy)

    def changeSides(self):
        left, right = right, left
        

GameState(StupidBot()).connect()
