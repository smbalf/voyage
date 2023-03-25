import pyxel

KEY_MAP = {
    "KEY_0": pyxel.KEY_0,
    "KEY_1": pyxel.KEY_1,
    "KEY_2": pyxel.KEY_2,
    "KEY_3": pyxel.KEY_3,
    "KEY_4": pyxel.KEY_4,
    "KEY_5": pyxel.KEY_5,
    "KEY_6": pyxel.KEY_6,
    "KEY_7": pyxel.KEY_7,
    "KEY_8": pyxel.KEY_8,
    "KEY_9": pyxel.KEY_9,

    "KEY_A": pyxel.KEY_A,
    "KEY_B": pyxel.KEY_B,
    "KEY_C": pyxel.KEY_C,
    "KEY_D": pyxel.KEY_D,
    "KEY_E": pyxel.KEY_E,
    "KEY_F": pyxel.KEY_F,
    "KEY_G": pyxel.KEY_G,
    "KEY_H": pyxel.KEY_H,
    "KEY_I": pyxel.KEY_I,
    "KEY_J": pyxel.KEY_J,
    "KEY_K": pyxel.KEY_K,
    "KEY_L": pyxel.KEY_L,
    "KEY_M": pyxel.KEY_M,
    "KEY_N": pyxel.KEY_N,
    "KEY_O": pyxel.KEY_O,
    "KEY_P": pyxel.KEY_P,
    "KEY_Q": pyxel.KEY_Q,
    "KEY_R": pyxel.KEY_R,
    "KEY_S": pyxel.KEY_S,
    "KEY_T": pyxel.KEY_T,
    "KEY_U": pyxel.KEY_U,
    "KEY_V": pyxel.KEY_V,
    "KEY_W": pyxel.KEY_W,
    "KEY_X": pyxel.KEY_X,
    "KEY_Y": pyxel.KEY_Y,
    "KEY_Z": pyxel.KEY_Z,

    "KEY_BACKSPACE": pyxel.KEY_BACKSPACE,
    "KEY_TAB": pyxel.KEY_TAB,
    "KEY_RETURN": pyxel.KEY_RETURN,
}

def handle_input(user_input):
    for key_name, key_code in KEY_MAP.items():
        if pyxel.btnp(key_code):
            user_input = process_key_input(key_name, user_input)
    return user_input


def process_key_input(key_name, user_input):
    if key_name.startswith("KEY_"):
        user_input += key_name[-1]
    elif key_name == "KEY_BACKSPACE":
        user_input = user_input[:-1]
    return user_input
