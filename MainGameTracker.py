import arcade
import random

class GameTracker:
    def __init__(self):
        self.playerBtnInfo = PlayerBtnInfo()
        self.playerScoreInfo = PlayerScoreInfo()
        self.userInputHandlerInGame = UserInputHandlerInGame(self.playerBtnInfo
            , self.playerScoreInfo)
        self.phaseTracker = PhaseTracker()

    def on_key_press(self, key, key_modifiers):
        if(self.phaseTracker.current_phase == self.phaseTracker.PHASE_PLAY):
            self.userInputHandlerInGame.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        if(self.phaseTracker.current_phase == self.phaseTracker.PHASE_PLAY):
            self.userInputHandlerInGame.on_key_release(key, key_modifiers)

    def update(self, delta_time):
        self.phaseTracker.update(delta_time)
        self.userInputHandlerInGame.update(delta_time)

class PlayerBtnInfo:
    def __init__(self):
        self.MAX_QUEUE = 6
        self.BLOCK_QUEUE = 2
        self.BTN_TOTAL = 4
        self.BTN_UP = 0
        self.BTN_LEFT = 1
        self.BTN_DOWN = 2
        self.BTN_RIGHT = 3

        self.player_1_btn = []
        self.player_2_btn = []

        for i in range(self.MAX_QUEUE):
            self.player_1_btn.append(random.randrange(self.BTN_TOTAL))
            self.player_2_btn.append(random.randrange(self.BTN_TOTAL))

    def delete_front(self, player):
        if player == 1:
            del self.player_1_btn[0]
            self.player_1_btn.append(random.randrange(self.BTN_TOTAL))
        elif player == 2:
            del self.player_2_btn[0]
            self.player_2_btn.append(random.randrange(self.BTN_TOTAL))

class PlayerScoreInfo:
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_1_combo = 0
        self.player_2_combo = 0

        self.score_1_combo = 100
        self.score_10_combo = 150
        self.score_20_combo = 200

    def update(self, player, isCorrect):
        self.edit_combo(player, isCorrect)
        if isCorrect:
            self.edit_score(player)

    def edit_combo(self, player, isCorrect):
        if player == 1:
            if isCorrect:
                self.player_1_combo += 1
            else:
                self.player_1_combo = 0
        elif player == 2:
            if isCorrect:
                self.player_2_combo += 1
            else:
                self.player_2_combo = 0

    def edit_score(self, player):
        if player == 1:
            if self.player_1_combo < 10:
                self.player_1_score += self.score_1_combo
            elif self.player_1_combo < 20:
                self.player_1_score += self.score_10_combo
            else:
                self.player_1_score += self.score_20_combo
        elif player == 2:
            if self.player_2_combo < 10:
                self.player_2_score += self.score_1_combo
            elif self.player_2_combo < 20:
                self.player_2_score += self.score_10_combo
            else:
                self.player_2_score += self.score_20_combo

class UserInputHandlerInGame:
    def __init__(self, btnInfo, scoreInfo):
        self.INCORRECT_PAUSE_TIME = 1.5
        self.btnInfo = btnInfo
        self.scoreInfo = scoreInfo
        self.player_1_btn_ready = True
        self.player_2_btn_ready = True
        self.player_1_pause_time = 0.0
        self.player_2_pause_time = 0.0

    def update(self, delta_time):
        if self.player_1_pause_time:
            self.player_1_pause_time -= delta_time
            if self.player_1_pause_time < 0:
                self.player_1_pause_time = 0
        if self.player_2_pause_time:
            self.player_2_pause_time -= delta_time
            if self.player_2_pause_time < 0:
                self.player_2_pause_time = 0


    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.W and self.player_1_btn_ready
            and self.player_1_pause_time <= 0.0):
            self.player_1_btn_ready = False
            self.checkInput(1, self.btnInfo.BTN_UP)
        elif (key == arcade.key.A and self.player_1_btn_ready
            and self.player_1_pause_time <= 0.0):
            self.player_1_btn_ready = False
            self.checkInput(1, self.btnInfo.BTN_LEFT)
        elif (key == arcade.key.S and self.player_1_btn_ready
            and self.player_1_pause_time <= 0.0):
            self.player_1_btn_ready = False
            self.checkInput(1, self.btnInfo.BTN_DOWN)
        elif (key == arcade.key.D and self.player_1_btn_ready
            and self.player_1_pause_time <= 0.0):
            self.player_1_btn_ready = False
            self.checkInput(1, self.btnInfo.BTN_RIGHT)

        if (key == arcade.key.UP and self.player_2_btn_ready
            and self.player_2_pause_time <= 0.0):
            self.player_2_btn_ready = False
            self.checkInput(2, self.btnInfo.BTN_UP)
        elif (key == arcade.key.LEFT and self.player_2_btn_ready
            and self.player_2_pause_time <= 0.0):
            self.player_2_btn_ready = False
            self.checkInput(2, self.btnInfo.BTN_LEFT)
        elif (key == arcade.key.DOWN and self.player_2_btn_ready
            and self.player_2_pause_time <= 0.0):
            self.player_2_btn_ready = False
            self.checkInput(2, self.btnInfo.BTN_DOWN)
        elif (key == arcade.key.RIGHT and self.player_2_btn_ready
            and self.player_2_pause_time <= 0.0):
            self.player_2_btn_ready = False
            self.checkInput(2, self.btnInfo.BTN_RIGHT)

    def on_key_release(self, key, modifiers):
        if (key == arcade.key.W or key == arcade.key.A
            or key == arcade.key.S or key == arcade.key.D):
                self.player_1_btn_ready = True
        elif (key == arcade.key.UP or key == arcade.key.LEFT
            or key == arcade.key.DOWN or key == arcade.key.RIGHT):
                self.player_2_btn_ready = True

    def checkInput(self, player, input):
        if player == 1:
            if self.btnInfo.player_1_btn[0] == input:
                self.scoreInfo.update(1, True)
                self.btnInfo.delete_front(1)
            else:
                self.scoreInfo.update(1, False)
                self.player_1_pause_time = self.INCORRECT_PAUSE_TIME
        elif player == 2:
            if self.btnInfo.player_2_btn[0] == input:
                self.scoreInfo.update(2, True)
                self.btnInfo.delete_front(2)
            else:
                self.scoreInfo.update(2, False)
                self.player_2_pause_time = self.INCORRECT_PAUSE_TIME
    def get_player_1_pause_time(self):
        return self.player_1_pause_time / self.INCORRECT_PAUSE_TIME

    def get_player_2_pause_time(self):
        return self.player_2_pause_time / self.INCORRECT_PAUSE_TIME

class PhaseTracker:
    def __init__(self):
        self.PHASE_PREP = 0
        self.PHASE_PLAY = 1
        self.PHASE_TIMEOUT = 2
        self.PHASE_GAMEOVER = 3
        self.PHASE_TIME = [0.0, 10.0, 70.0, 74.0]

        self.time_from_start = 0.0
        self.current_phase = self.PHASE_PREP

    def update(self, delta_time):
        self.time_from_start += delta_time
        if self.current_phase < self.PHASE_GAMEOVER:
            if self.time_from_start > self.PHASE_TIME[self.current_phase + 1]:
                self.current_phase += 1
