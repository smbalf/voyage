import pyxel
from player import player

player = player

title_bg_width = len(player['location'])*5 if len(player['location']) <= 8 else len(player['location'])*4.4
flags = {}

def main_display():

    # Game border
    pyxel.rectb(0, 0, 360, 340, 0)

    # Main display border
    pyxel.rectb(10, 10, 340, 320, 0)

    # City location title
    pyxel.rect(162, 5, title_bg_width, 10, 0)
    pyxel.text(165, 8, f"{player['location'].upper()}", 1)

    # Displays date and player gold
    pyxel.text(14, 17, f"{player['date'].strftime('%d %b %Y')}", 0)
    pyxel.text(290, 17, f"Gold: {player['money']}", 0)
    
    # Displays player ship stats
    # pyxel.rect(11, 29, 338, 11, 13)
    pyxel.text(14, 32, "Hull HP: 500/500", 0)
    pyxel.text(85, 32,  "Cannons: 60/60", 0)
    pyxel.text(148, 32, "Stores: 30/30", 0)
    pyxel.text(208, 32, "Cargohold:2000/2000", 0)
    pyxel.text(290, 32, "Crew: 120/120", 0)

    # Game viewport
    pyxel.rectb(10, 40, 340, 266, 0)
    


