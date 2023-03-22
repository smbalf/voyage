import pyxel
from items import goods

image_positions = {}


def load_images():
    x = 0
    for good in goods.keys():
        pyxel.image(0).load(x, 0, f"assets/{good.lower()}.png")
        image_positions[good] = x
        x += 16
    
    print(image_positions)

