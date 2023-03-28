from player_saving import load_game
from player import player
from trading import generate_market
from world import game_world
from items import goods

def initialise_game():
    generate_market(goods, game_world[player["location"]]["price_tier"])

    loaded_player, loaded_market = load_game()
    if loaded_player is not None and loaded_market is not None:
        player.update(loaded_player)
        market = loaded_market
    else:
        pass
