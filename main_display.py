import pyxel
from player import player
from ships import ship_types


player = player

title_bg_width = len(player['location'])*5 if len(player['location']) <= 8 else len(player['location'])*4.4
flags = {}

def main_display():

    # Game border
    pyxel.rectb(0, 0, 360, 380, 0)

    # Main display border
    pyxel.rectb(10, 10, 340, 360, 0)

    # City location title
    pyxel.rect(162, 5, title_bg_width, 10, 0)
    pyxel.text(165, 8, f"{player['location'].upper()}", 1)

    # Displays date and player gold
    pyxel.text(14, 17, f"{player['date'].strftime('%d %b %Y')}", 0)
    pyxel.text(290, 17, f"Gold: {player['money']}", 0)
    
    # Displays player ship stats
    pyxel.text(14, 32, f"Hull HP: {get_current_hitpoints()}", 0)
    pyxel.text(85, 32,  f"Cannons: {get_current_cannons()}", 0)
    pyxel.text(148, 32, f"Stores: {get_current_stores()}", 0)
    pyxel.text(208, 32, f"Cargohold: {get_current_cargo()}", 0)
    pyxel.text(290, 32, f"Crew: {get_current_crew()}", 0)

    # Game viewport
    pyxel.rectb(10, 40, 340, 306, 0)
    

def get_current_cargo():
    total_cargo = sum(subitem["quantity"] for item in player["cargo"].values() for subitem in item)
    max_cargo = ship_types[player["ship"]]["capacity"]
    return f"{total_cargo}/{max_cargo}"

def get_current_crew():
    total_crew = sum(player["crew"].values())
    max_crew = ship_types[player["ship"]]["crew"]
    return f"{total_crew}/{max_crew}"

def get_current_cannons():
    total_cannon = player["cannon"]
    max_cannons = ship_types[player["ship"]]["cannon"]
    return f"{total_cannon}/{max_cannons}"

def get_current_stores():
    total_stores = player["stores"]
    max_stores = ship_types[player["ship"]]["stores"]
    return f"{total_stores}/{max_stores}"

def get_current_hitpoints():
    total_hitpoints = player["hitpoints"]
    max_hitpoints = ship_types[player["ship"]]["hitpoints"]
    return f"{total_hitpoints}/{max_hitpoints}"