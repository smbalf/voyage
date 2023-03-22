import pyxel
import os
from main_display import main_display
from view_port import GameInterface, interface_draw_functions
from buttons import buttons
from trading import generate_market
from sprites import load_images

os.system('cls')

generate_market()


BLACK = 0x222323
WHITE = 0xf0f6f0

pyxel.colors[0] = BLACK
pyxel.colors[1] = WHITE


class App:
    def __init__(self):
        pyxel.init(360, 340)
        load_images()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit() 

    def draw(self):
        pyxel.cls(1)
        main_display()
        buttons()
        
        if GameInterface.current_interface:
            interface_draw_functions[GameInterface.current_interface]()

        pyxel.text(320, 332, f"{pyxel.mouse_x}, {pyxel.mouse_y}", 0)
        pyxel.text(pyxel.mouse_x, pyxel.mouse_y, ".", 0)
App()
