# JSON SAVING METHOD
import json
import os
from datetime import datetime

SAVE_FILE = "save_data.json"

def datetime_to_str(date_obj):
    return date_obj.strftime('%Y-%m-%d')

def str_to_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

def save_game(player, market):
    # Convert datetime to string before saving
    player_copy = player.copy()
    player_copy["date"] = datetime_to_str(player_copy["date"])

    save_data = {"player": player_copy, "market": market}

    with open(SAVE_FILE, "w") as save_file:
        json.dump(save_data, save_file)

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as save_file:
            save_data = json.load(save_file)
            
            # Convert date string back to datetime object after loading
            save_data["player"]["date"] = str_to_datetime(save_data["player"]["date"])

            return save_data["player"], save_data["market"]
    else:
        return None, None


"""
#PICKLE SAVING METHOD
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
"""