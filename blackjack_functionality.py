from card_functions import CardFunctions
import random

dealer_value = 0
player_value = 0
random_int = 0
hand_in_progress = True
while hand_in_progress == True:
    bj_deck = CardFunctions.deck_generator(CardFunctions.card_deck)
    dealer_hand = []
    dealer_hand.append(bj_deck.pop())
    print(dealer_hand[0]['number']['suit'])
    hand_in_progress = False
    
