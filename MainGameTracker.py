import arcade
import random

class GameTracker:

    def __init__(self):
        self.playerBtnInfo = PlayerBtnInfo()

class PlayerBtnInfo:

    def __init__(self):
        self.MAX_QUEUE = 6
        self.BTN_LEFT = 0
        self.BTN_RIGHT = 1
        self.BTN_UP = 2
        self.BTN_DOWN = 3

        self.player_1_btn = []
        self.player_2_btn = []

        for i in range(self.MAX_QUEUE):
            self.player_1_btn.append(random.randrange(4))
            self.player_2_btn.append(random.randrange(4))
