from datetime import timedelta
from trading import generate_market
from items import goods
from player import player
from world import game_world
#from banking import update_daily_interest

def game_tick():
    tier = game_world[player["location"]]["price_tier"]
    generate_market(goods, tier)

    # update_daily_interest()

    player["date"] += timedelta(days=1)
    player["stores"] -= 1
