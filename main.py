import pyxel
import os

from main_display import main_display
from view_port import GameInterface, interface_draw_functions
from buttons import buttons
from trading import generate_market
from sprites import load_images
from player_keylogging import PlayerKeys as p
from player_keylogging import CAPTION
from sailing import draw_sailing_progress
os.system('cls')


generate_market()


BLACK = 0x222323
WHITE = 0xf0f6f0
BLUE = 0x1875cc
ORANGE = 0xcd5f2a
RED = 0x96181e

pyxel.colors[0] = BLACK
pyxel.colors[1] = WHITE
pyxel.colors[2] = BLUE
pyxel.colors[3] = ORANGE
pyxel.colors[4] = RED

title = CAPTION

class App:
    def __init__(self):
        pyxel.init(360, 380, title=title)
        load_images()
        p.register_key_listeners()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit() 

    def draw(self):
        pyxel.cls(1)
        main_display()
        buttons()
        draw_sailing_progress()

        if GameInterface.current_interface:
            interface_draw_functions[GameInterface.current_interface]()

        pyxel.text(320, 372, f"{pyxel.mouse_x}, {pyxel.mouse_y}", 0)
        pyxel.mouse(visible=True)
App()
