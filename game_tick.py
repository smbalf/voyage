from datetime import timedelta
from trading import market, generate_market
from player import player
#from banking import update_daily_interest

def game_tick():
    global market
    market = generate_market()
    
    #update_daily_interest()
    player["date"] += timedelta(days=1)
    player["food"] -= 1
    player["water"] -= 1


