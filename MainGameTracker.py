import arcade
import random

class GameTracker:
    def __init__(self):
        self.playerBtnInfo = PlayerBtnInfo()
        self.playerScoreInfo = PlayerScoreInfo()

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

class PlayerScoreInfo:
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0

    def edit_Score(self, player, score):
        if player == 1:
            self.player_1_score += score
        elif player == 2:
            self.player_2_score += score
