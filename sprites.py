import pyxel
from items import goods

image_positions = {}

map_1a = 10, 56, 1, 0, 0, 128, 128
map_1b = 138, 56, 1, 128, 0, 128, 128
map_1c = 10, 184, 1, 0, 128, 128, 128
map_1d = 138, 184, 1, 128, 128, 128, 128

map_2a = 266, 56, 2, 0, 0, 83, 128
map_2b = 266, 184, 2, 84, 0, 83, 128
map_2c = 10, 311, 2, 0, 128, 256, 34
map_2d = 266, 311, 2, 168, 0, 83, 34

def load_images():
    x = 0
    for good in goods.keys():
        pyxel.image(0).load(x, 0, f"assets/goods/{good.lower()}.png")
        image_positions[good] = x
        x += 16
    pyxel.image(1).load(0, 0, "assets/map/map_1a.png")
    pyxel.image(1).load(128, 0, "assets/map/map_1b.png")
    pyxel.image(1).load(0, 128, "assets/map/map_1c.png")
    pyxel.image(1).load(128, 128, "assets/map/map_1d.png")
    pyxel.image(2).load(0, 0, "assets/map/map_2a.png")
    pyxel.image(2).load(84, 0, "assets/map/map_2b.png")
    pyxel.image(2).load(0, 128, "assets/map/map_2c.png")
    pyxel.image(2).load(168, 0, "assets/map/map_2d.png")