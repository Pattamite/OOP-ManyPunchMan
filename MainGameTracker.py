import arcade
import random

class PlayerBtnInfo:

    def __init__(self):
        self.MAX_QUEUE = 6
        self.player_1_btn = []
        self.player_2_btn = []
        for i in range(self.MAX_QUEUE):
            self.player_1_btn.append(random.randrange(4))
            self.player_2_btn.append(random.randrange(4))
