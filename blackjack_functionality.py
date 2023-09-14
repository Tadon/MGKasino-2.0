from card_functions import CardFunctions
import random

dealer_value = 0
player_value = 0
random_int = 0
hand_in_progress = True
bj_deck = CardFunctions.deck_generator(CardFunctions.card_deck)
dealer_hand = []
player_hand = []
while hand_in_progress:
    player_info = ""
    dealer_info = ""
    dealer_hand.append(bj_deck.pop())
    player_hand.append(bj_deck.pop())
    player_hand.append(bj_deck.pop())
    for i in dealer_hand:
        dealer_info += i['number'] + i['suit'] + ''
        if i['number'] == '[A ' and i['value2'] + dealer_value < 22:
            dealer_value += i['value2']
        else:
            dealer_value += i['value']
    for i in player_hand:
        player_info += i['number']+i['suit'] + ''
        if i['number'] == '[A ' and i['value2'] + player_value < 22:
            player_value += i['value2']
        else:
            player_value += i['value']

    hand_in_progress = False
print(f'Dealer\'s hand: {dealer_info} with a value of {dealer_value}')
print(f'Player\'s hand: {player_info} with a value of {player_value}')