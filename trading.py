import pyxel
from player import player
from items import goods
import random
from sprites import image_positions


market = {}

trading_ui_active = False
buying_ui_active = False
selling_ui_active = False
selected_good = None

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
    pyxel.text(160, 47, "MARKET", 7)
    # coordinates
    ximg = 22 # image placeholder
    xgood = 50 # name of good
    xprice = 90 # price of good
    xtrade = 130 # trade button
    yimg = 58 # ycoord of image
    ytext = 65 # ycoord of text

    def get_trade(x, y, good):
        global trading_ui_active
        global selected_good
        global selected_price
        if (
        pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 
        x <= pyxel.mouse_x <= x + 25 and 
        y - 3 <= pyxel.mouse_y <= y + 11):
            trading_ui_active = True
            selected_good = good
            selected_price = price

    for good, price in market.items():
        get_trade(xtrade - 3, ytext - 3, good)
        
        pyxel.rectb(ximg-2, yimg-1, 21, 18, 0) # image placeholder
        pyxel.text(xgood, ytext, f"{good}", 0) # name of good
        pyxel.text(xprice, ytext, f"{price}", 0) # price of good
        pyxel.blt(ximg, yimg, 0, image_positions[good], 0, 16, 16) #THE IMAGE

        pyxel.rectb(xtrade-3, ytext-3, 25, 11, 0) # trade button borders
        pyxel.text(xtrade, ytext, "Trade", 0) # trade buttons

        yimg += 20
        ytext += 20

        if good == "Ingots": # create second column
            ximg += 160
            xgood += 160
            xprice += 160
            xtrade += 160
            yimg = 58
            ytext = 65

# FACILITATES BUYING AND SELLING OF ITEMS
def item_trade_ui(good, price):
    global buying_ui_active
    global selling_ui_active
    if trading_ui_active:
        pyxel.rectb(90, 50, 170, 12, 0)
        pyxel.text(150, 53, "TRADE AGREEMENT", 0)
        pyxel.text(247, 53, "[X]", 0)  # GIVE THIS FUNCTIONALITY TO CLOSE AND RETURN TO TRADE INTERFACE
        pyxel.rectb(90, 62, 170, 153, 0)
        pyxel.text(100, 70, f"{good.upper()} are hereby exchanged for the \n\nsum of {price} gold.", 0)
        pyxel.text(100, 100, f"Would you care to buy or sell {good.lower()}?", 0)

        pyxel.rectb(125, 115, 24, 16, 0)
        pyxel.text(131, 120, "BUY", 0)
        pyxel.rectb(190, 115, 24, 16, 0)
        pyxel.text(195, 120, "SELL", 0)
        

        #make some if statement to set buying_ui_active
        """
        pyxel.rect(91, 115, 168, 50, 1)
        pyxel.text(100, 120, f"How many would you like to buy? \n\nYou can afford {int(player['money']/price)}.", 0)
        # input box for buying 
        # confirmation
        
        """
        #make some if statement to set selling_ui_active


    
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
        item_trade_ui(selected_good, selected_price)
        ship_cargo_ui()
    
    elif buying_ui_active:
        pass
    
    elif selling_ui_active:
        pass
    else:
        market_prices_ui()
        ship_cargo_ui()

        

