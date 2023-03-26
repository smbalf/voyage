import pyxel
from world import game_world
from player import player
from ships import ship_types
from sprites import map_1a, map_1b, map_1c, map_1d, map_2a, map_2b, map_2c, map_2d

def get_nearest_ports():
    distances = game_world[player["location"]]
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    nearest_ports = {port: distance for port, distance in sorted_distances}
    return nearest_ports


def display_ports_ui():
    pyxel.text(14, 46, f"Port: {player['location']}", 0)
    pyxel.text(120, 46, f"Destination: Constantinople", 0)
    pyxel.text(280, 46, f"ETA: 6 days", 0)
    pyxel.line(10, 55, 349, 55, 0)

    pyxel.blt(*map_1a)
    pyxel.blt(*map_1b)
    pyxel.blt(*map_1c)
    pyxel.blt(*map_1d)
    pyxel.blt(*map_2a)
    pyxel.blt(*map_2b)
    pyxel.blt(*map_2c)
    pyxel.blt(*map_2d)
    

def fleet():
    display_ports_ui()