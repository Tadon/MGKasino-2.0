from card_functions import CardFunctions
import random

dealer_value = 0
player_value = 0
random_int = 0
hand_in_progress = True
while hand_in_progress == True:
    dealer_hand = []
    player_hand = []
    next_card = CardFunctions.get_card()
    print(f"{next_card['number']}{next_card['suit']}{next_card['value']}")