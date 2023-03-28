import pyxel
import os

from global_store import text_input

from main_display import main_display
from view_port import GameInterface, interface_draw_functions
from buttons import buttons
from items import goods
from trading import generate_market
from sprites import load_images
from sailing import draw_sailing_progress
from world import game_world
from player import player
os.system('cls')


generate_market(goods, game_world[player["location"]]["price_tier"])

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


class App:
    def __init__(self):
        pyxel.init(360, 380, title="Merchant's Voyage")
        load_images()
        global text_input
        self.text_input = text_input
        pyxel.run(self.update, self.draw)

    def update(self):      
        self.text_input.update()

    def draw(self):
        pyxel.cls(1)
        main_display()
        buttons()

        if GameInterface.current_interface:
            interface_draw_functions[GameInterface.current_interface]()
            if GameInterface.current_interface == 'fleet':
                draw_sailing_progress()
        pyxel.text(320, 372, f"{pyxel.mouse_x}, {pyxel.mouse_y}", 0)
        pyxel.mouse(visible=True)
App()
