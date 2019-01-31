from bot_interface import *
import math
import random

class StupidBot(BotBase):
    def process(self, gamestate):
        thrust = random.uniform(-1, 1);
        sideThrustFront = random.uniform(-1, 1);
        sideThrustBack = random.uniform(-1, 1);
        shoot = random.uniform(0, 3);
        return Action(
            thrust,
            sideThrustFront,
            sideThrustBack,
            shoot)

GameState(StupidBot()).connect()
