import arcade
from MainGameTracker import PlayerBtnInfo

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class MainGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.playerBtnInfo = PlayerBtnInfo()

    def on_draw(self):
        player_1_btn_position_x = 100
        player_1_btn_position_y = 400
        player_2_btn_position_x = 550
        player_2_btn_position_y = 400
        player_btn_x_offset = 50

        arcade.start_render()
        for i in range(6):
            arcade.draw_text(str(self.playerBtnInfo.player_1_btn[i]),
                player_1_btn_position_x + (i * player_btn_x_offset),
                player_1_btn_position_y, arcade.color.BLACK, 30);
            arcade.draw_text(str(self.playerBtnInfo.player_2_btn[i]),
                player_2_btn_position_x + (i * player_btn_x_offset),
                player_2_btn_position_y, arcade.color.BLACK, 30);


if __name__=='__main__':
    window = MainGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
