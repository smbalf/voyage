import pyxel
import random

from game_tick import game_tick
from world import game_world
from player import player
from ships import ship_types
from crew import units
from main_display import get_crew_stats


price = random.randint(1, 5)


def display_crew_ui():
    yheader = 60
    xunit = 20
    xcost = 80
    xatt = 100
    xdef = 120
    xsail = 140
    xhire = 164
    ytext = 75
    xroster = 202
    yrostertext = 75
    xstats = 290
    xfire = 258
    ystats = 75

    if player["is_sailing"] == False:
        pyxel.text(xunit, yheader, "UNIT", 0)
        pyxel.text(xcost, yheader, "COST", 0)
        pyxel.text(xatt, yheader, "ATT", 0)
        pyxel.text(xdef, yheader, "DEF", 0)
        pyxel.text(xsail, yheader, "SAIL", 0)
        
        for unit, stats in units.items():
            pyxel.text(xunit, ytext, f"{unit}", 0)
            pyxel.text(xcost, ytext, f"{stats['cost']}", 0)
            pyxel.text(xatt, ytext, f"{stats['attack']}", 0)
            pyxel.text(xdef, ytext, f"{stats['defence']}", 0)
            pyxel.text(xsail, ytext, f"{stats['sailing']}", 0)
            pyxel.text(xhire, ytext, "HIRE", 0)
            pyxel.rectb(xhire-3, ytext-3, 21, 11, 0)
            ytext += 20
        
        

        def get_crew():
            if xhire-2 <= pyxel.mouse_x <= xhire+17:
                if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 72 <= pyxel.mouse_y <= 82):
                    hire_crew("Novice")
                elif (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 92 <= pyxel.mouse_y <= 102):
                    hire_crew("Sailor")
                elif (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 112 <= pyxel.mouse_y <= 122):
                    hire_crew("Corsair")

            elif xfire-2 <= pyxel.mouse_x <= xfire+17:
                if player['crew'] != {}:
                    if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 72 <= pyxel.mouse_y <= 82 and 'Novice' in player["crew"]):
                        fire_crew("Novice")
                    elif (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 92 <= pyxel.mouse_y <= 102 and 'Sailor' in player["crew"]):
                        fire_crew("Sailor")
                    elif (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 112 <= pyxel.mouse_y <= 122 and 'Corsair' in player["crew"]):
                        fire_crew("Corsair")

        get_crew()
    else:
        pyxel.text(xcost-20, ytext+20, "Sailing on the open seas...", 13)

    if player['crew'] != {}:
        pyxel.text(xroster, yheader, "CREW ROSTER", 0)
        pyxel.text(xstats, yheader, "FLEET STATS", 0)
        crew_counts, aggregate_stats = get_crew_stats(player, units)
        for unit_name, unit_count in crew_counts.items():
            if unit_name == "Novice":
                pyxel.text(xroster, yrostertext, f"{unit_name}", 0)
                pyxel.text(xroster+35, yrostertext, f"{unit_count}", 0)
                if player["is_sailing"] == False:
                    pyxel.text(xfire, yrostertext, "FIRE", 0)
                    pyxel.rectb(xfire-3, yrostertext-3, 21, 11, 0)
            elif unit_name == "Sailor":
                pyxel.text(xroster, yrostertext+20, f"{unit_name}", 0)
                pyxel.text(xroster+35, yrostertext+20, f"{unit_count}", 0)
                if player["is_sailing"] == False:
                    pyxel.text(xfire, yrostertext+20, "FIRE", 0)
                    pyxel.rectb(xfire-3, yrostertext+17, 21, 11, 0)
            elif unit_name == "Corsair":
                pyxel.text(xroster, yrostertext+40, f"{unit_name}", 0)
                pyxel.text(xroster+35, yrostertext+40, f"{unit_count}", 0)
                if player["is_sailing"] == False:
                    pyxel.text(xfire, yrostertext+40, "FIRE", 0)
                    pyxel.rectb(xfire-3, yrostertext+37, 21, 11, 0)
        for stat_name, stat_value in aggregate_stats.items():
            pyxel.text(xstats, ystats, f"{stat_name}: {stat_value}", 0)
            ystats += 20
    else:
        pyxel.text(218, 88, "YOU HAVE NO CREW CAPTAIN!", 13)

def display_stores_ui():
    if player["is_sailing"] == False:
        max_stores = ship_types[player["ship"]]["stores"]
        xtext = 20
        ytext = 136
        xbuy = 275
        
        def get_stores():
                max_stores = ship_types[player["ship"]]["stores"]
                current_stores = player["stores"]
                qmax = max_stores - current_stores
                if (
                pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 
                272 <= pyxel.mouse_x <= 290 and 
                133 <= pyxel.mouse_y <= 144):
                    buy_stores(1)
                elif (
                pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 
                298 <= pyxel.mouse_x <= 334 and 
                133 <= pyxel.mouse_y <= 144):
                    buy_stores(qmax)

        if player["stores"] < max_stores:
            get_stores()
            pyxel.text(xtext, ytext, f"Ship stores cost {price} gold. We have {player['stores']} in our inventory, captain.", 0)
            pyxel.rectb(xbuy-3, ytext-3, 18, 11, 0)
            pyxel.text(xbuy, ytext, "BUY", 0)

            pyxel.rectb(xbuy+23, ytext-3, 36, 11, 0)
            pyxel.text(xbuy+27, ytext, "BUY MAX", 0)
        else:
            pyxel.text(xtext+75, ytext, f"We are fully stocked up on stores, captain.", 0)
    else:
        pass

def buy_stores(quantity):
    max_stores = ship_types[player["ship"]]["stores"]
    current_stores = player["stores"]
    cost = quantity * price

    if player["money"] >= cost and (quantity + current_stores) <= max_stores:
        player["money"] -= cost
        player["stores"] += quantity

def hire_crew(selected_unit):
    max_crew = ship_types[player["ship"]]["crew"]
    current_crew = sum(player["crew"].values())
    cost = units[selected_unit]["cost"]
    
    if player["money"] >= cost and (current_crew + 1) <= max_crew:
            player["money"] -= cost
            player["crew"][selected_unit] = player["crew"].get(selected_unit, 0) + 1

def fire_crew(selected_unit):
    min_crew = 0
    current_crew = sum(player["crew"].values())
    
    if current_crew - 1 >= min_crew:
        player["crew"][selected_unit] = player["crew"].get(selected_unit, 0) - 1
        
        if player["crew"][selected_unit] == 0:
            del player["crew"][selected_unit]

def get_nearest_ports():
    distances = game_world[player["location"]]["nearby_ports"]
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    nearest_ports = {port: distance for port, distance in sorted_distances}
    return nearest_ports

def display_ports_ui():
    destinations = {}
    nearest_ports = get_nearest_ports()
    xport = 20
    xdays = 80
    yheader = 170
    ytext = 185
    xsetsail = 120
    pyxel.text(xport, yheader, "PORT", 0)
    pyxel.text(xdays, yheader, "TIME", 0)
    pyxel.text(30, 315, f"Make sure we have enough stores and crew, captain!", 0)
    for port, distance in nearest_ports.items():
        destinations[port] = {"distance": distance, "ytext": ytext}
        pyxel.text(xport, ytext, f"{port}", 0)
        pyxel.text(xdays, ytext, f"{distance} days", 0)
        pyxel.text(xsetsail, ytext, "SAIL", 0)
        pyxel.rectb(xsetsail - 3, ytext - 3, 21, 11, 0)

        if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and
            xsetsail - 3 <= pyxel.mouse_x <= xsetsail + 18 and
            ytext - 3 <= pyxel.mouse_y <= ytext + 8):

            if player["stores"] >= distance and sum(player["crew"].values()) >= (ship_types[player["ship"]]["crew"] / 2):
                set_sail(port, distance)
            else:
                pass
        ytext+=20

def set_sail(port, distance):
    time_factor = 30 * 4
    player["destination"] = port
    player["is_sailing"] = True
    player["sailing_start_time"] = pyxel.frame_count
    player["sailing_duration"] = distance * time_factor
    player["sailing_eta"] = player["sailing_duration"] // 30
    player["sailing_days"] = distance

def draw_sailing_progress():
    port = player["location"]
    destination = player["destination"]
    if player["is_sailing"]:
        elapsed_time = pyxel.frame_count - player["sailing_start_time"]
        progress = min(300 * elapsed_time / player["sailing_duration"], 300)
        eta_seconds = max(0, player["sailing_eta"] - elapsed_time // 30)
        day_in_secs = player["sailing_eta"] // (player["sailing_duration"]/30/4)

        if 'next_game_tick_time' not in player:
            player['next_game_tick_time'] = player["sailing_start_time"] + day_in_secs * 30
        
        pyxel.rect(29, 312, 200, 10, 1)
        pyxel.text(30, 315, f"Sailing from {port.upper()} to {destination.upper()}. ETA: {eta_seconds} seconds.", 0)
        pyxel.rect(30, 326, int(progress), 10, 0)

        if pyxel.frame_count >= player['next_game_tick_time']:
            game_tick()
            player['next_game_tick_time'] += day_in_secs * 30

        if elapsed_time >= player["sailing_duration"]:
            player["is_sailing"] = False
            player["location"] = player["destination"]
            del player['next_game_tick_time']


def progress_bar():
    pyxel.rectb(29, 325, 300, 12, 0)

def main_sailing_ui():
    pyxel.rect(10, 41, 340, 12, 0)
    pyxel.text(148, 44, "FLEET MANAGEMENT", 1)

    pyxel.line(11, 130, 348, 130, 13)
    pyxel.line(192, 60, 192, 122, 13)

    pyxel.line(11, 148, 348, 148, 13)
    pyxel.rect(11, 148, 338, 16, 0)
    pyxel.text(148, 154, "NEXT DESTINATION", 1)

    pyxel.line(11, 299, 348, 299, 13)


def fleet():
    main_sailing_ui()
    display_crew_ui()
    display_ports_ui()
    display_stores_ui()
    progress_bar()