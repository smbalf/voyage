import pyxel

class TextInput:
    def __init__(self):
        self.text = ""
        self.typing = False
        self.allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789 "
        self.key_map = {pyxel.KEY_0: "0", pyxel.KEY_1: "1", pyxel.KEY_2: "2", pyxel.KEY_3: "3", pyxel.KEY_4: "4",
                        pyxel.KEY_5: "5", pyxel.KEY_6: "6", pyxel.KEY_7: "7", pyxel.KEY_8: "8", pyxel.KEY_9: "9"}

        for i, char in enumerate(self.allowed_characters):
            self.key_map[pyxel.KEY_A + i] = char

    def update(self):
        if not self.typing:
            return

        for key, character in self.key_map.items():
            if pyxel.btnp(key):
                if pyxel.btn(pyxel.KEY_SHIFT) and character in self.shifted_mapping:
                    self.text += self.shifted_mapping[character]
                else:
                    self.text += character

        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.text = self.text[:-1]

    def reset_typing(self):
        self.typing = False
        self.text = ""
