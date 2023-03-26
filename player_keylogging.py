import keyboard
import utils

CAPTION = "Merchant's Voyage"


class PlayerKeys:
    text = ""

    typing = False

    @classmethod
    def record_keys(cls, key):
        special_keys = ["space", "tab", "backspace", "enter"]
        hidden_keys = keyboard.all_modifiers

        if not utils.Utilities.app_is_open(CAPTION):
            return

        if not PlayerKeys.typing:
            return

        if key.name == "backspace":
            PlayerKeys.text = PlayerKeys.text[:-1]
        elif key.name == "space":
            PlayerKeys.text += " "
        elif key.name == "enter":
            PlayerKeys.text += "\n"
        elif len(PlayerKeys.text) > 1 and len(PlayerKeys.text) % 28 == 0:
            PlayerKeys.text += "\n"
        else:
            if key.name not in special_keys:
                if key.name not in hidden_keys:
                    PlayerKeys.text += key.name

    @classmethod
    def register_key_listeners(cls):
        keyboard.on_press(PlayerKeys.record_keys)

    @classmethod
    def reset_typing(cls):
        PlayerKeys.typing = False
        PlayerKeys.text = ""


PlayerKeys()