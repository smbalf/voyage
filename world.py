game_world = {
    "Genoa": {
        "price_tier": "high",
        "nearby_ports": {
            "Marseille": 4,  
            "Roma": 5,       
            "Palma": 8,      
            "Cagliari": 7,   
            "Barcelona": 7   
        }
    },
    "Cagliari": {
        "price_tier": "med",
        "nearby_ports": {
            "Genoa": 7,      
            "Tunis": 2,      
            "Roma": 4        
        }
    },
    "Roma": {
        "price_tier": "med",
        "nearby_ports": {
            "Genoa": 5,      
            "Siracusa": 6,   
            "Cagliari": 4    
        }
    },
    "Marseille": {
        "price_tier": "med",
        "nearby_ports": {
            "Genoa": 4,      
            "Palma": 5,      
            "Barcelona": 4,  
            "Cagliari": 5    
        }
    },
    "Barcelona": {
        "price_tier": "high",
        "nearby_ports": {
            "Marseille": 4,  
            "Valencia": 3,   
            "Palma": 3,      
            "Genoa": 7       
        }
    },
    "Valencia": {
        "price_tier": "med",
        "nearby_ports": {
            "Algiers": 4,    
            "Palma": 2,      
            "Barcelona": 3,  
            "Cadiz": 12      
        }
    },
    "Palma": {
        "price_tier": "med",
        "nearby_ports": {
            "Valencia": 3,   
            "Algiers": 3,    
            "Marseille": 5,  
            "Barcelona": 3   
        }
    },
    "Cadiz": {
        "price_tier": "med",
        "nearby_ports": {
            "Valencia": 12,
            "Algiers": 12,
            "Lisbon": 6
        }
    },
    "Algiers": {
        "price_tier": "low",
        "nearby_ports": {
            "Valencia": 4,
            "Palma": 3,
            "Tunis": 5,
            "Cadiz": 12
        }
    },
    "Tunis": {
        "price_tier": "low",
        "nearby_ports": {
            "Algiers": 5,
            "Siracusa": 3,
            "Malta": 2,
            "Cagliari": 2,
            "Tripoli": 3
        }
    },
    "Siracusa": {
        "price_tier": "med",
        "nearby_ports": {
            "Tunis": 2,
            "Roma": 6,
            "Malta": 1,
            "Taranto": 3,
            "Corfu": 4
        }
    },
    "Malta": {
        "price_tier": "med",
        "nearby_ports": {
            "Siracusa": 1,
            "Tunis": 2,
            "Tripoli": 2
        }
    },
    "Tripoli": {
        "price_tier": "low",
        "nearby_ports": {
            "Malta": 2,
            "Tunis": 3,
            "Benghazi": 3
        }
    },
    "Benghazi": {
        "price_tier": "low",
        "nearby_ports": {
            "Tripoli": 3,
            "Alexandria": 6
        }
    },
    "Taranto": {
        "price_tier": "med",
        "nearby_ports": {
            "Siracusa": 3,
            "Corfu": 2,
            "Durres": 3
        }
    },
    "Durres": {
        "price_tier": "med",
        "nearby_ports": {
            "Taranto": 3,
            "Corfu": 2,
            "Ragusa": 5,
            "Ancona": 5
        }
    },
    "Ragusa": {
        "price_tier": "med",
        "nearby_ports": {
            "Venice": 3,
            "Ancona": 2,
            "Durres": 5
        }
    },
    "Ancona": {
        "price_tier": "med",
        "nearby_ports": {
            "Venice": 3,
            "Ragusa": 2,
            "Durres": 5
        }
    },
    "Venice": {
        "price_tier": "high",
        "nearby_ports": {
            "Ancona": 3,
            "Ragusa": 3
        }
    },
    "Corfu": {
        "price_tier": "med",
        "nearby_ports": {
            "Durres": 2,
            "Taranto": 2,
            "Kalamata": 3,
            "Siracusa": 4
        }
    },
    "Kalamata": {
        "price_tier": "med",
        "nearby_ports": {
            "Corfu": 3,
            "Athens": 3,
            "Heraklion": 3
        }
    },
    "Athens": {
        "price_tier": "med",
        "nearby_ports": {
            "Kalamata": 3,
            "Smyrna": 4,
            "Thessaloniki": 5,
            "Heraklion": 5
        }
    },
    "Thessaloniki": {
        "price_tier": "med",
        "nearby_ports": {
            "Athens": 5,
            "Smyrna": 6,
            "Constantinople": 10
        }
    },
    "Constantinople": {
        "price_tier": "high",
        "nearby_ports": {
            "Thessaloniki": 10,
            "Smyrna": 8,
            "Caffa": 12,
            "Trebizond": 8
        }
    },
    "Smyrna": {
        "price_tier": "med",
        "nearby_ports": {
            "Constantinople": 8,
            "Thessaloniki": 6,
            "Athens": 4,
            "Rhodes": 4
        }
    },
    "Heraklion": {
        "price_tier": "med",
        "nearby_ports": {
            "Kalamata": 5,
            "Athens": 5,
            "Rhodes": 5,
            "Alexandria": 12
        }
    },
    "Rhodes": {
        "price_tier": "med",
        "nearby_ports": {
            "Smyrna": 4,
            "Heraklion": 5,
            "Side": 6,
            "Famagusta": 8,
            "Alexandria": 14
        }
    },
    "Side": {
        "price_tier": "low",
        "nearby_ports": {
            "Rhodes": 6,
            "Famagusta": 5,
            "Antioch": 6
        }
    },
    "Famagusta": {
        "price_tier": "med",
        "nearby_ports": {
            "Alexandria": 10,
            "Side": 5,
            "Rhodes": 8,
            "Antioch": 5,
            "Tortosa": 6
        }
    },
    "Antioch": {
        "price_tier": "low",
        "nearby_ports": {
            "Side": 6,
            "Famagusta": 5,
            "Tortosa": 6
        }
    },
    "Tortosa": {
        "price_tier": "med",
        "nearby_ports": {
            "Antioch": 6,
            "Famagusta": 6,
            "Acre": 3,
            "Alexandria": 10
        }
    },
    "Acre": {
        "price_tier": "low",
        "nearby_ports": {
            "Tortosa": 3,
            "Alexandria": 8
        }
    },
    "Alexandria": {
        "price_tier": "low",
        "nearby_ports": {
            "Acre": 8,
            "Tortosa": 10,
            "Famagusta": 10,
            "Rhodes": 14,
            "Heraklion": 12,
            "Benghazi": 6
        }
    },
    "Caffa": {
        "price_tier": "low",
        "nearby_ports": {
            "Constantinople": 12,
            "Trebizond": 8
        }
    },
    "Trebizond": {
        "price_tier": "med",
        "nearby_ports": {
            "Caffa": 8,
            "Constantinople": 10
        }
    },
    "Lisbon": {
        "price_tier": "high",
        "nearby_ports": {
            "Cadiz": 6,
            "Santiago": 8
        }
    },
    "Santiago": {
        "price_tier": "med",
        "nearby_ports": {
            "Lisbon": 8,
            "Bordeaux": 6
        }
    },
    "Bordeaux": {
        "price_tier": "med",
        "nearby_ports": {
            "Santiago": 6,
            "Nantes": 5
        }
    },
    "Southampthon": {
        "price_tier": "med",
        "nearby_ports": {
            "Nantes": 5,
            "London": 5
        }
    },
    "Nantes": {
        "price_tier": "med",
        "nearby_ports": {
            "Bordeaux": 5,
            "Southampton": 5,
            "London": 10
        }
    },
    "London": {
        "price_tier": "high",
        "nearby_ports": {
            "Nantes": 10,
            "Southampton": 5,
            "Bruges": 6,
            "Amsterdam": 9
        }
    },
    "Amsterdam": {
        "price_tier": "med",
        "nearby_ports": {
            "London": 9,
            "Bruges": 3,
            "Lubeck": 5
        }
    },
    "Bruges": {
        "price_tier": "med",
        "nearby_ports": {
            "London": 6,
            "Amsterdam": 3,
            "Lubeck": 6
        }
    },
    "Lubeck": {
        "price_tier": "high",
        "nearby_ports": {
            "Bruges": 6,
            "Amsterdam": 5,
            "Danzig": 4
        }
    },
    "Danzig": {
        "price_tier": "med",
        "nearby_ports": {
            "Lubeck": 4,
            "Riga": 7
        }
    },
    "Riga": {
        "price_tier": "low",
        "nearby_ports": {
            "Danzig": 7,
            "Novgorod": 12
        }
    },
    "Novgorod": {
        "price_tier": "low",
        "nearby_ports": {
            "Riga": 12
        }
    }
}

nearby_ports = {
    "Genoa":            {"map_x": 165, "map_y": 194},
    "Cagliari":         {"map_x": 162, "map_y": 246},
    "Roma":             {"map_x": 178, "map_y": 210},
    "Marseille":        {"map_x": 139, "map_y": 199},
    "Barcelona":        {"map_x": 116, "map_y": 222},
    "Valencia":         {"map_x": 103, "map_y": 240},
    "Palma":            {"map_x": 121, "map_y": 239},
    "Sevilla":          {"map_x": 59, "map_y": 260},
    "Algiers":          {"map_x": 133, "map_y": 270},
    "Tunis":            {"map_x": 173, "map_y": 267},
    "Siracusa":         {"map_x": 207, "map_y": 262},
    "Malta":            {"map_x": 203, "map_y": 281},
    "Tripoli":          {"map_x": 185, "map_y": 310},
    "Benghazi":         {"map_x": 238, "map_y": 318},
    "Taranto":          {"map_x": 223, "map_y": 238},
    "Durres":           {"map_x": 240, "map_y": 224},
    "Ragusa":            {"map_x": 217, "map_y": 201},
    "Ancona":           {"map_x": 192, "map_y": 197},
    "Venice":           {"map_x": 196, "map_y": 187},
    "Corfu":            {"map_x": 240, "map_y": 244},
    "Kalamata":         {"map_x": 254, "map_y": 263},
    "Athens":           {"map_x": 264, "map_y": 255},
    "Thessaloniki":     {"map_x": 260, "map_y": 233},
    "Constantinople":   {"map_x": 294, "map_y": 233},
    "Smyrna":           {"map_x": 292, "map_y": 250},
    "Heraklion":        {"map_x": 269, "map_y": 278},
    "Rhodes":           {"map_x": 291, "map_y": 261},
    "Side":             {"map_x": 308, "map_y": 252},
    "Famagusta":        {"map_x": 327, "map_y": 278},
    "Antioch":    {"map_x": 346, "map_y": 252},
    "Tortosa":          {"map_x": 346, "map_y": 281},
    "Acre":             {"map_x": 342, "map_y": 314},
    "Alexandria":       {"map_x": 298, "map_y": 329},
}

