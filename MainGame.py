import arcade
import math
from MainGameTracker import GameTracker

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class MainGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.gameTracker = GameTracker()
        self.arrow_up_texture = arcade.load_texture("images/arrow_up.png")
        self.arrow_down_texture = arcade.load_texture("images/arrow_down.png")
        self.arrow_left_texture = arcade.load_texture("images/arrow_left.png")
        self.arrow_right_texture = arcade.load_texture("images/arrow_right.png")
        self.block_unknown_texture = arcade.load_texture("images/block_unknown.png")
        self.arrow_texture_size = 50
        self.block_unknown_texture_size = 50

    def on_key_press(self, key, key_modifiers):
        self.gameTracker.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.gameTracker.on_key_release(key, key_modifiers)

    def animate(self, delta_time):
        self.gameTracker.update(delta_time)

    def on_draw(self):
        arcade.start_render()
        self.draw_btn()
        self.draw_score()
        self.draw_combo()
        self.draw_phase()

    def draw_btn(self):
        player_1_btn_position_x = 70
        player_1_btn_position_y = 400
        player_2_btn_position_x = 520
        player_2_btn_position_y = 400
        player_btn_x_offset = 60

        for i in range(self.gameTracker.playerBtnInfo.MAX_QUEUE):
            self.draw_arrow(self.gameTracker.playerBtnInfo.player_1_btn[i]
                , player_1_btn_position_x + (i * player_btn_x_offset)
                , player_1_btn_position_y)
            self.draw_arrow(self.gameTracker.playerBtnInfo.player_2_btn[i]
                , player_2_btn_position_x + (i * player_btn_x_offset)
                , player_2_btn_position_y)

            if(i < self.gameTracker.playerBtnInfo.BLOCK_QUEUE
                and self.gameTracker.phaseTracker.current_phase == self.gameTracker.phaseTracker.PHASE_PLAY):
                self.draw_block_unknown(player_1_btn_position_x + (i * player_btn_x_offset)
                    , player_1_btn_position_y)
                self.draw_block_unknown(player_2_btn_position_x + (i * player_btn_x_offset)
                    , player_2_btn_position_y)

    def draw_arrow(self, arrow, x, y):
        if arrow == self.gameTracker.playerBtnInfo.BTN_UP:
            arcade.draw_texture_rectangle(x, y, self.arrow_texture_size
            , self.arrow_texture_size, self.arrow_up_texture)
        elif arrow == self.gameTracker.playerBtnInfo.BTN_LEFT:
            arcade.draw_texture_rectangle(x, y, self.arrow_texture_size
            , self.arrow_texture_size, self.arrow_left_texture)
        elif arrow == self.gameTracker.playerBtnInfo.BTN_RIGHT:
            arcade.draw_texture_rectangle(x, y, self.arrow_texture_size
            , self.arrow_texture_size, self.arrow_right_texture)
        elif arrow == self.gameTracker.playerBtnInfo.BTN_DOWN:
            arcade.draw_texture_rectangle(x, y, self.arrow_texture_size
            , self.arrow_texture_size, self.arrow_down_texture)

    def draw_block_unknown(self, x, y):
        arcade.draw_texture_rectangle(x, y, self.block_unknown_texture_size
        , self.block_unknown_texture_size, self.block_unknown_texture)

    def draw_score(self):
        player_1_score_position_x = 400
        player_1_score_text_position_x = 50
        player_1_score_position_y = 300

        player_2_score_position_x = 850
        player_2_score_text_position_x = 500
        player_2_score_position_y = 300

        score_font_size = 40

        arcade.draw_text("Score : "
            , player_1_score_text_position_x, player_1_score_position_y
            , arcade.color.BLACK, score_font_size, align="left"
            , anchor_x="left", anchor_y="center")
        arcade.draw_text("Score : "
            , player_2_score_text_position_x, player_1_score_position_y
            , arcade.color.BLACK, score_font_size, align="left"
            , anchor_x="left", anchor_y="center")

        arcade.draw_text(str(self.gameTracker.playerScoreInfo.player_1_score)
            , player_1_score_position_x, player_1_score_position_y
            , arcade.color.BLACK, score_font_size, align="right"
            , anchor_x="right", anchor_y="center")
        arcade.draw_text(str(self.gameTracker.playerScoreInfo.player_2_score)
            , player_2_score_position_x, player_2_score_position_y
            , arcade.color.BLACK, score_font_size, align="right"
            , anchor_x="right", anchor_y="center")

    def draw_combo(self):
        player_1_combo_position_x = 400
        player_1_combo_text_position_x = 50
        player_1_combo_position_y = 240
        player_1_combo_color = self.get_combo_color(self.gameTracker.playerScoreInfo.player_1_combo)
        player_1_combo_size = self.get_combo_size(self.gameTracker.playerScoreInfo.player_1_combo)

        player_2_combo_position_x = 850
        player_2_combo_text_position_x = 500
        player_2_combo_position_y = 240
        player_2_combo_color = self.get_combo_color(self.gameTracker.playerScoreInfo.player_2_combo)
        player_2_combo_size = self.get_combo_size(self.gameTracker.playerScoreInfo.player_2_combo)

        arcade.draw_text("Combo : "
            , player_1_combo_text_position_x, player_1_combo_position_y
            , player_1_combo_color, player_1_combo_size, align="left"
            , anchor_x="left", anchor_y="center")
        arcade.draw_text("Combo : "
            , player_2_combo_text_position_x, player_2_combo_position_y
            , player_2_combo_color, player_2_combo_size, align="left"
            , anchor_x="left", anchor_y="center")

        arcade.draw_text(str(self.gameTracker.playerScoreInfo.player_1_combo)
            , player_1_combo_position_x, player_1_combo_position_y
            , player_1_combo_color, player_1_combo_size, align="right"
            , anchor_x="right", anchor_y="center")
        arcade.draw_text(str(self.gameTracker.playerScoreInfo.player_2_combo)
            , player_2_combo_position_x, player_2_combo_position_y
            , player_2_combo_color, player_2_combo_size, align="right"
            , anchor_x="right", anchor_y="center")

    def get_combo_color(self, combo):
        if combo < 10:
            return arcade.color.BLACK
        elif combo < 20:
            return arcade.color.ORANGE
        elif combo % 2 == 0:
            return arcade.color.RED
        else:
            return arcade.color.CADMIUM_RED
    def get_combo_size(self, combo):
        if combo < 10:
            return 20
        elif combo < 20:
            return 30
        else:
            return 40

    def draw_phase(self):
        if self.gameTracker.phaseTracker.current_phase == self.gameTracker.phaseTracker.PHASE_PREP:
            self.draw_phase_prep()
        elif self.gameTracker.phaseTracker.current_phase == self.gameTracker.phaseTracker.PHASE_PLAY:
            self.draw_phase_play()
        elif self.gameTracker.phaseTracker.current_phase == self.gameTracker.phaseTracker.PHASE_TIMEOUT:
            self.draw_phase_timeout()
        elif self.gameTracker.phaseTracker.current_phase == self.gameTracker.phaseTracker.PHASE_GAMEOVER:
            self.draw_phase_gameover()

    def draw_phase_prep(self):
        self.draw_timer(self.gameTracker.phaseTracker.current_phase)

    def draw_phase_play(self):
        self.draw_timer(self.gameTracker.phaseTracker.current_phase)

    def draw_phase_timeout(self):
        arcade.draw_text("Time's up", 450, 500, arcade.color.RED, 50
            , align="center", anchor_x="center", anchor_y="center")

    def draw_phase_gameover(self):
        arcade.draw_text("Game Over", 450, 500, arcade.color.BLACK, 50
            , align="center", anchor_x="center", anchor_y="center")

    def draw_timer(self, phase):
        timer_position_x = 450
        timer_position_y = 500
        timer_size = 50
        time_remain = self.get_time_remain()
        timer_color = self.get_timer_color(time_remain)

        arcade.draw_text(str(math.ceil(time_remain)), timer_position_x, timer_position_y
            , timer_color, timer_size, align="center"
            , anchor_x="center", anchor_y="center")

    def get_time_remain(self):
        time_remain = self.gameTracker.phaseTracker.PHASE_TIME[self.gameTracker.phaseTracker.current_phase + 1] - self.gameTracker.phaseTracker.time_from_start
        if time_remain < 0.0:
            time_remain = 0.0

        return time_remain

    def get_timer_color(self, time_remain):
        if time_remain > 30 :
            return arcade.color.BLACK
        elif time_remain > 20 :
            return arcade.color.GIANTS_ORANGE
        elif time_remain > 10 :
            return arcade.color.ORANGE_RED
        elif time_remain > 5 :
            return arcade.color.RED
        else :
            return arcade.color.RED_DEVIL


if __name__=='__main__':
    window = MainGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
