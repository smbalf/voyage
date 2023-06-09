import pyxel
import random
from player import player
from items import goods
from sprites import image_positions
from world import game_world
from global_store import text_input
from player_saving import save_game


trading_ui_active = False
selected_good = None
selected_quality = None
selected_trade_type = None
selected_price = None



def generate_market(goods, price_tier):
    global market
    market = {}
    
    for good, qualities in goods.items():
        price_range = qualities[price_tier]
        current_price = price_range["price"]
        if current_price < 40:
            price_change = random.triangular(-5, 5, 0)
        elif 41 < current_price < 100:
            price_change = random.triangular(-0.1, 0.1, 0) * current_price
        else:
            price_change = random.triangular(-0.05, 0.05, 0) * current_price
        new_price = current_price + price_change
        new_price = max(price_range["min"], min(price_range["max"], new_price))
        price_range["price"] = int(new_price)
    return market

def get_market():
    global market
    return market

def get_vwap(good):
    if good not in player["cargo"]:
        return 0
    total_cost = sum(transaction["cost"] for transaction in player["cargo"][good])
    total_quantity = sum(transaction["quantity"] for transaction in player["cargo"][good])
    return total_cost / total_quantity

def get_market_price(good, location):
    price_tier = game_world[location]['price_tier']
    return goods[good][price_tier]['price']


def market_prices_ui():
    location = player['location']
    pyxel.rect(10, 41, 340, 12, 0)
    pyxel.text(163, 44, "MARKET", 1)
    # coordinates
    ximg = 22 # image placeholder
    xgood = 50 # name of good
    xprice = 90 # price of good
    xbuy = 118 # buy button
    xsell = 147 # sell button
    yimg = 58 # ycoord of image
    ytext = 65 # ycoord of text

    def get_trade(x, y, good, quality, trade_type):
        global trading_ui_active
        global selected_good
        global selected_quality
        global selected_trade_type
        if (
        pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 
        x <= pyxel.mouse_x <= x + 25 and 
        y - 3 <= pyxel.mouse_y <= y + 11):
            trading_ui_active = True
            selected_good = good
            selected_quality = quality
            selected_trade_type = trade_type
            item_trade_ui(selected_good, selected_quality, selected_trade_type)
    
    for good, qualities in goods.items():
        quality = game_world[player["location"]]["price_tier"]
        price = get_market_price(good, location)

        pyxel.rectb(ximg-2, yimg-1, 21, 18, 0) # image placeholder
        pyxel.text(xgood, ytext, f"{good}", 0) # name of good
        pyxel.text(xprice, ytext, f"{price}", 0) # price of good
        pyxel.blt(ximg, yimg, 0, image_positions[good], 0, 16, 16) #THE IMAGE

        pyxel.rectb(xbuy-3, ytext-3, 25, 11, 0) # buy button borders
        pyxel.text(xbuy+4, ytext, "Buy", 0) # buy button
        get_trade(xbuy - 3, ytext - 3, good, quality, "buy")

        pyxel.rectb(xsell-3, ytext-3, 25, 11, 0) # sell button borders
        pyxel.text(xsell+2, ytext, "Sell", 0) # sell button
        get_trade(xsell - 3, ytext - 3, good, quality, "sell")

        yimg += 20
        ytext += 20

        if good == "Ingots": # create second column
            ximg += 165
            xgood += 165
            xprice += 165
            xbuy += 165
            xsell += 165
            yimg = 58
            ytext = 65

# FACILITATES BUYING AND SELLING OF ITEMS
def item_trade_ui(good, quality, trade_type):
    global trading_ui_active
    global selected_price
    can_buy = int(player['money']/get_market_price(good, player['location']))

    location = player['location']
    price = get_market_price(good, location)
    selected_price = price

    if trading_ui_active:
        pyxel.rectb(90, 50, 174, 12, 0)
        pyxel.text(150, 53, "TRADE AGREEMENT", 0)
        pyxel.text(250, 53, "[X]", 0) 
        pyxel.rectb(90, 62, 174, 153, 0)
        if good[-1] == "s":
            pyxel.text(100, 70, f"{good.upper()} are currently exchanged for the \n\nsum of {price} gold.", 0)
        else:
            pyxel.text(100, 70, f"{good.upper()} is currently exchanged for the \n\nsum of {price} gold.", 0)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 250 <= pyxel.mouse_x <= 258 and 50 <=pyxel.mouse_y <= 55:
            trading_ui_active = False

        if trade_type == "buy":
            if can_buy > 0:
                text_input.typing = True
                quantity = text_input.text
                pyxel.text(100, 100, f"You can afford {can_buy}, captain. \n\nHow many would you like to purchase?", 0)
                pyxel.text(100, 140, "Quantity:", 0)
                pyxel.text(140, 140, quantity, 0)
                pyxel.text(100, 160, "Cost:", 0)
                if quantity != "":
                    pyxel.text(140, 160, f"{int(quantity) * price}", 0)
                pyxel.line(100, 157, 247, 157, 0)
                pyxel.line(100, 167, 247, 167, 0)
                
                pyxel.rectb(150, 180, 60, 12, 0)
                pyxel.text(153, 183, "SIGN AGREEMENT", 0)

                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 150 <= pyxel.mouse_x <= 210 and 180 <=pyxel.mouse_y <= 192:
                    try:
                        quantity = int(quantity)
                    except ValueError:
                        pass
                    text_input.reset_typing()
                    buy_good(good, price, quantity)
            else:
                pyxel.text(100, 100, f"You can't afford to buy any captain!", 0)

        elif trade_type == "sell":
            if good in player["cargo"]:
                quantity = sum(transaction["quantity"] for transaction in player["cargo"][good])
                if quantity > 0: 
                    text_input.typing = True
                    sell_amount = text_input.text
                    pyxel.text(100, 100, f"You have {quantity} to sell, captain. \n\nHow much would you like to sell?", 0)
                    pyxel.text(100, 140, "Quantity:", 0)
                    pyxel.text(140, 140, sell_amount, 0)
                    pyxel.text(100, 160, "Value:", 0)
                    if sell_amount != "":
                        pyxel.text(140, 160, f"{int(sell_amount) * price}", 0)
                    pyxel.line(100, 157, 247, 157, 0)
                    pyxel.line(100, 167, 247, 167, 0)
                    
                    pyxel.rectb(150, 180, 60, 12, 0)
                    pyxel.text(153, 183, "SIGN AGREEMENT", 0)

                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 150 <= pyxel.mouse_x <= 210 and 180 <=pyxel.mouse_y <= 192:
                        if sell_amount != "":
                            sell_amount = int(sell_amount)
                        text_input.reset_typing()
                        if isinstance(sell_amount, int):
                            sell_good(good, price, sell_amount)
            else:
                pyxel.text(100, 140, "You've nought to sell captain.", 0)


def ship_cargo_ui():
    pyxel.line(10, 226, 348, 226, 0)
    pyxel.rect(150, 219, 53, 10, 1)
    pyxel.text(153, 224, "CARGO LEDGER", 0)

    if player["cargo"] != {}:
        pyxel.line(121, 246, 121, 336, 13)
        pyxel.line(236, 246, 236, 336, 13)

        xgood = 22 #50
        xquantity = 60 #87
        xvwap = 93 #109
        ytext = 248

        # Ledger column headers
        pyxel.text(xgood, 236, "ITEM", 13)
        pyxel.text(xquantity, 236, "QTY", 13)
        pyxel.text(xvwap, 236, "PRICE", 13)
        pyxel.text(xgood + 115, 236, "ITEM", 13)
        pyxel.text(xquantity + 115, 236, "QTY", 13)
        pyxel.text(xvwap + 115, 236, "PRICE", 13)
        pyxel.text(xgood + 230, 236, "ITEM", 13)
        pyxel.text(xquantity + 230, 236, "QTY", 13)
        pyxel.text(xvwap + 230, 236, "PRICE", 13)

        for good, cargo_data in player["cargo"].items():
            vwap = int(get_vwap(good))
            quantity = sum(transaction["quantity"] for transaction in cargo_data)
            pyxel.text(xgood, ytext, f"{good}", 0)
            pyxel.text(xquantity, ytext, f"{quantity}", 0)
            pyxel.text(xvwap, ytext, f"{vwap}", 0)

            ytext += 20

            if ytext > 330:
                xgood += 115
                xquantity += 115
                xvwap += 115
                ytext = 248
    
    else: 
        pyxel.text(144, 260, "CARGO HOLD EMPTY!", 13)
           

def trading():
    if trading_ui_active:
        item_trade_ui(selected_good, selected_price, selected_trade_type)
        ship_cargo_ui()

    else:
        market_prices_ui()
        ship_cargo_ui()

def buy_good(good, price, quantity):
    global trading_ui_active
    cost = quantity * price
    try:
        if player["money"] >= cost:
            player["money"] -= cost
            if good not in player["cargo"]:
                player["cargo"][good] = []
            player["cargo"][good].append({"quantity": quantity, "cost": cost})
            trading_ui_active = False
            save_game(player, market)

        else:
            return False
    except (TypeError, ValueError):
        pass

def sell_good(good, price, sell_amount):
    global trading_ui_active
    cargo_data = [transaction for transaction in player["cargo"][good]]
    total_quantity = sum(transaction["quantity"] for transaction in cargo_data)
    transactions = cargo_data

    if total_quantity >= sell_amount:
        remaining_quantity = total_quantity - sell_amount
        original_quantity_to_sell = sell_amount  # Store the original quantity_to_sell

        # Remove transactions until the remaining quantity is accounted for
        while sell_amount > 0:
            transaction = transactions[0]
            if transaction["quantity"] <= sell_amount:
                sell_amount -= transaction["quantity"]
                transactions.pop(0)
            else:
                transaction["quantity"] -= sell_amount
                transaction["cost"] -= sell_amount * transaction["cost"] / (transaction["quantity"] + sell_amount)
                sell_amount = 0

        # Update the player's cargo
        player["cargo"][good] = transactions  # Update with remaining transactions

        if remaining_quantity == 0:
            del player["cargo"][good]
        income = original_quantity_to_sell * price  # Use the original quantity_to_sell
        player["money"] += income
        trading_ui_active = False
        save_game(player, market)
