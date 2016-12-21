import arcade
from MainGameTracker import GameTracker

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class MainGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.gameTracker = GameTracker()


    def on_draw(self):
        arcade.start_render()
        self.draw_btn()
        self.draw_score()

    def draw_btn(self):
        player_1_btn_position_x = 100
        player_1_btn_position_y = 400
        player_2_btn_position_x = 550
        player_2_btn_position_y = 400
        player_btn_x_offset = 50

        for i in range(6):
            arcade.draw_text(str(self.gameTracker.playerBtnInfo.player_1_btn[i]),
                player_1_btn_position_x + (i * player_btn_x_offset),
                player_1_btn_position_y, arcade.color.BLACK, 30);
            arcade.draw_text(str(self.gameTracker.playerBtnInfo.player_2_btn[i]),
                player_2_btn_position_x + (i * player_btn_x_offset),
                player_2_btn_position_y, arcade.color.BLACK, 30);

    def draw_score(self):
        player_1_score_position_x = 235
        player_1_score_position_y = 300
        player_2_score_position_x = 685
        player_2_score_position_y = 300

        arcade.draw_text(str(self.gameTracker.playerScoreInfo.player_1_score),
            player_1_score_position_x, player_1_score_position_y,
            arcade.color.BLACK, 50, align="center",
            anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.gameTracker.playerScoreInfo.player_2_score),
            player_2_score_position_x, player_2_score_position_y,
            arcade.color.BLACK, 50, align="center",
            anchor_x="center", anchor_y="center")


if __name__=='__main__':
    window = MainGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
