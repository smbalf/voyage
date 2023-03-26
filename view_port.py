from trading import trading
from shipwright import shipwright
from sailing import fleet

interface_draw_functions = {
    'trading': trading,
    'shipwright': shipwright,
    'fleet': fleet
    # Add more interfaces here
}

class GameInterface:
    current_interface = None

    def close_interfaces():
        GameInterface.current_interface = None

    def switch_interface(interface_name):
        GameInterface.current_interface = interface_name

    
