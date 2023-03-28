import pickle
import os

SAVE_FILE = "save_data.pkl"


def save_game(player, market):
    save_data = {"player": player, "market": market}

    with open(SAVE_FILE, "wb") as save_file:
        pickle.dump(save_data, save_file)


def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as save_file:
            save_data = pickle.load(save_file)
            return save_data["player"], save_data["market"]
    else:
        return None, None
