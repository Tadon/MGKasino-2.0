card_deck = {

    #hearts
    1: {'number': '2', 'suit':'♥', 'value': 2 }, 2: {'number': '3', 'suit':'♥','value': 3 }, 3: {'number': '4', 'suit':'♥','value': 4 }, 4: {'number': '5', 'suit':'♥','value': 5 }, 5: {'number': '6', 'suit':'♥','value': 6 },
    6: {'number': '7', 'suit':'♥','value': 7 }, 7: {'number': '8', 'suit':'♥','value': 8 }, 8: {'number': '9', 'suit':'♥','value': 9 }, 9: {'number': '10', 'suit':'♥','value': 10 }, 10: {'number': 'J', 'suit':'♥','value': 10 },
    11: {'number': 'Q', 'suit':'♥','value': 10 }, 12:{'number': 'K', 'suit':'♥','value': 10 }, 13:{'number': 'A', 'suit':'♥','value1': 1,'value11': 11 },

    #diamonds
    14: {'number': '2', 'suit':'♦', 'value': 2 }, 15: {'number': '3', 'suit':'♦','value': 3 }, 16: {'number': '4', 'suit':'♠','value': 4 }, 17: {'number': '5' , 'suit':'♦','value': 5 }, 18: {'number': '6', 'suit':'♦','value': 6 },
    19: {'number': '7', 'suit':'♦', 'value': 7 }, 20: {'number': '8', 'suit':'♦','value': 8 }, 21: {'number': '9', 'suit':'♠','value': 9 }, 22: {'number': '10', 'suit':'♦','value': 10}, 23: {'number': 'J', 'suit':'♦','value': 10},
    24: {'number': 'Q', 'suit':'♦','value': 10 }, 25: {'number': 'K', 'suit':'♦','value': 10}, 26: {'number': 'A', 'suit':'♠','value1': 1,'value11': 11 },

    #spades
    27: {'number': '2', 'suit':'♠', 'value': 2 }, 28: {'number': '3', 'suit':'♠','value': 3 }, 29: {'number': '4', 'suit':'♠','value': 4 }, 30: {'number': '5' , 'suit':'♠','value': 5 }, 31: {'number': '6', 'suit':'♠','value': 6 },
    32: {'number': '7', 'suit':'♠', 'value': 7 }, 33: {'number': '8', 'suit':'♠','value': 8 }, 34: {'number': '9', 'suit':'♠','value': 9 }, 35: {'number': '10', 'suit':'♠','value': 10}, 36: {'number': 'J', 'suit':'♠','value': 10},
    37: {'number': 'Q', 'suit':'♠','value': 10 }, 38: {'number': 'K', 'suit':'♠','value': 10}, 39: {'number': 'A', 'suit':'♠','value1': 1,'value11': 11 },

    #clubs
    40: {'number': '2', 'suit':'♣', 'value': 2 }, 41: {'number': '3', 'suit':'♣','value': 3 }, 42: {'number': '4', 'suit':'♣','value': 4 }, 43: {'number': '5' , 'suit':'♣','value': 5 }, 44: {'number': '6', 'suit':'♣','value': 6 },
    45: {'number': '7', 'suit':'♣', 'value': 7 }, 46: {'number': '8', 'suit':'♣','value': 8 }, 47: {'number': '9', 'suit':'♣','value': 9 }, 48: {'number': '10', 'suit':'♣','value': 10}, 49: {'number': 'J', 'suit':'♣','value': 10},
    50: {'number': 'Q', 'suit':'♣','value': 10 }, 51: {'number': 'K', 'suit':'♣','value': 10}, 52: {'number': 'A', 'suit':'♣','value1': 1,'value11': 11 }

    


}

for key, info in card_deck.items():
    print(f"card #{key} is the [{info['number']}{info['suit']}]")

'♥' '♦' '♣' '♠'