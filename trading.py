import pyxel
import random
from player import player
from items import goods
from sprites import image_positions
from input_handling import handle_input


market = {}

trading_ui_active = False
selected_good = None
user_input = ""

def generate_market():
    for good, price_range in goods.items():
        current_price = price_range["price"]
        if current_price < 50:
            price_change = random.triangular(-0.3, 0.35, 0.02) * current_price
        else:
            price_change = random.triangular(-0.15, 0.165, 0.02) * current_price
        new_price = current_price + price_change
        new_price = max(price_range["min"], min(price_range["max"], new_price))
        market[good] = int(new_price)
        price_range["price"] = new_price
    return market

def get_vwap(good):
    if good not in player["cargo"]:
        return 0
    total_cost = sum(transaction["cost"] for transaction in player["cargo"][good])
    total_quantity = sum(transaction["quantity"] for transaction in player["cargo"][good])
    return total_cost / total_quantity

def market_prices_ui():
    pyxel.text(160, 47, "MARKET", 0)
    # coordinates
    ximg = 22 # image placeholder
    xgood = 50 # name of good
    xprice = 90 # price of good
    xbuy = 118 # buy button
    xsell = 147 # sell button
    yimg = 58 # ycoord of image
    ytext = 65 # ycoord of text

    def get_trade(x, y, good, trade_type):
        global trading_ui_active
        global selected_good
        global selected_price
        global selected_trade_type
        if (
        pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 
        x <= pyxel.mouse_x <= x + 25 and 
        y - 3 <= pyxel.mouse_y <= y + 11):
            trading_ui_active = True
            selected_good = good
            selected_price = price
            selected_trade_type = trade_type
            item_trade_ui(selected_good, selected_price, selected_trade_type)
    
    for good, price in market.items():
        
        pyxel.rectb(ximg-2, yimg-1, 21, 18, 0) # image placeholder
        pyxel.text(xgood, ytext, f"{good}", 0) # name of good
        pyxel.text(xprice, ytext, f"{price}", 0) # price of good
        pyxel.blt(ximg, yimg, 0, image_positions[good], 0, 16, 16) #THE IMAGE

        pyxel.rectb(xbuy-3, ytext-3, 25, 11, 0) # buy button borders
        pyxel.text(xbuy+4, ytext, "Buy", 0) # buy button
        get_trade(xbuy - 3, ytext - 3, good, "buy")
        
        pyxel.rectb(xsell-3, ytext-3, 25, 11, 0) # sell button borders
        pyxel.text(xsell+2, ytext, "Sell", 0) # sell button
        get_trade(xsell - 3, ytext - 3, good, "sell")
        
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
def item_trade_ui(good, price, trade_type):
    global trading_ui_active
    global user_input
    can_buy = int(player['money']/price)

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
                print("buying")
                qty = handle_input(user_input)
                if qty.isdigit():
                    pyxel.text(100, 100, f"You can afford {can_buy}, captain. \n\nHow many would you like to purchase?", 0)
                    pyxel.text(100, 140, "Quantity:", 0)
                    pyxel.text(140, 140, qty, 0) # CUSTOM INPUT HANDLER SHOULD GO HERE
                    pyxel.text(100, 160, "Cost:", 0)
                    pyxel.text(140, 160, f"{qty * price}", 0)
                    pyxel.line(100, 157, 247, 157, 0)
                    pyxel.line(100, 167, 247, 167, 0)
                    
                    pyxel.rectb(150, 180, 60, 12, 0)
                    pyxel.text(153, 183, "SIGN AGREEMENT", 0)

                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 150 <= pyxel.mouse_x <= 210 and 180 <=pyxel.mouse_y <= 192:
                        print("got clicked sign agreement")
                        return good, price
            else:
                pyxel.text(100, 90, f"You can't afford to buy any captain!", 0)

        elif trade_type == "sell":
            if good in player["cargo"]:
                qty = sum(transaction["quantity"] for transaction in player["cargo"][good])
                if qty > 0:    
                    pyxel.text(100, 100, f"You have {qty} to sell, captain. \n\nHow much would you like to sell?", 0)
                    pyxel.text(100, 140, "Quantity:", 0)
                    pyxel.text(140, 140, "100", 0) # CUSTOM INPUT HANDLER SHOULD GO HERE
                    pyxel.text(100, 160, "Value:", 0)
                    pyxel.text(140, 160, "800", 0)
                    pyxel.line(100, 157, 247, 157, 0)
                    pyxel.line(100, 167, 247, 167, 0)
                    
                    pyxel.rectb(150, 180, 60, 12, 0)
                    pyxel.text(153, 183, "SIGN AGREEMENT", 0)

                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 150 <= pyxel.mouse_x <= 210 and 180 <=pyxel.mouse_y <= 192:
                        print("got clicked sign agreement")
                        return good, price
            else:
                pyxel.text(100, 140, "You've nought to sell captain.", 0)


def ship_cargo_ui():
    pyxel.line(10, 226, 348, 226, 0)
    pyxel.rect(150, 219, 53, 10, 1)
    pyxel.text(153, 224, "CARGO LEDGER", 0)

    if player["cargo"] != {}:
        pyxel.line(121, 246, 121, 296, 13)
        pyxel.line(236, 246, 236, 296, 13)

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

            if ytext > 290:
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

def buy_good(good, quantity):
    price = market[good]
    cost = quantity * price
    if player["money"] >= cost:
        player["money"] -= cost
        if good not in player["cargo"]:
            player["cargo"][good] = []
        player["cargo"][good].append({"quantity": quantity, "cost": cost})
        return True
    else:
        return False

def sell_good(good):
    print("Trying to sell:" + good)