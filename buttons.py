import pyxel

from view_port import GameInterface

def buttons():
    # Trading
    pyxel.rect(14, 310, 50, 15, 0)
    pyxel.text(25, 315, "TRADING", 1)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 14 <= pyxel.mouse_x <= 64 and pyxel.mouse_y >= 310:
        pyxel.rect(14, 310, 50, 15, 1)
        pyxel.text(25, 315, "TRADING", 0)
        GameInterface.switch_interface('trading')

    # Shipwright
    pyxel.rect(70, 310, 50, 15, 0)
    pyxel.text(75, 315, "SHIPWRIGHT", 1)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 70 <= pyxel.mouse_x <= 120 and pyxel.mouse_y >= 310:
        pyxel.rect(70, 310, 50, 15, 1)
        pyxel.text(75, 315, "SHIPWRIGHT", 0)
        GameInterface.switch_interface('shipwright')

    # Fleet
    pyxel.rect(126, 310, 50, 15, 0)
    pyxel.text(141, 315, "FLEET", 1)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 126 <= pyxel.mouse_x <= 176 and pyxel.mouse_y >= 310:
        pyxel.rect(126, 310, 50, 15, 1)
        pyxel.text(141, 315, "FLEET", 0)

    # Warehouse
    pyxel.rect(182, 310, 50, 15, 0)
    pyxel.text(189, 315, "WAREHOUSE", 1)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 182 <= pyxel.mouse_x <= 232 and pyxel.mouse_y >= 310:
        pyxel.rect(182, 310, 50, 15, 1)
        pyxel.text(189, 315, "WAREHOUSE", 0)

    # Banking
    pyxel.rect(238, 310, 50, 15, 0)
    pyxel.text(249, 315, "BANKING", 1)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 238 <= pyxel.mouse_x <= 288 and pyxel.mouse_y >= 310:
        pyxel.rect(238, 310, 50, 15, 1)
        pyxel.text(249, 315, "BANKING", 0)

    # Stay Idle
    pyxel.rect(294, 310, 50, 15, 0)
    pyxel.text(301, 315, "STAY IDLE", 1)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 294 <= pyxel.mouse_x <= 344 and pyxel.mouse_y >= 310:
        pyxel.rect(294, 310, 50, 15, 1)
        pyxel.text(301, 315, "STAY IDLE", 0)