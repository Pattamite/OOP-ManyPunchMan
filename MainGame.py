import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class MainGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

if __name__=='__main__':
    window = MainGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
