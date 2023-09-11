from card_functions import CardFunctions

for i, card_info in CardFunctions.card_deck.items():
    
    print (f"card #{i} is a [{card_info['number']}{card_info['suit']}] which has a value of {card_info['value']}")