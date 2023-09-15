from card_functions import CardFunctions
from user_information import UserInformation
import random

class BlackJack:

    def __init__(self, balance):
        self.balance = balance

    def play_blackjack():
        playing_blackjack = True
        print('Welcome to MGBlackjack! Where the odds are always in our favor.')
        while playing_blackjack:
            dealer_value, player_value = 0, 0
            dealer_hand, player_hand = [], []
            dealer_info, player_info = "", ""
            hand_in_progress = True
            dealer_hand.append(random.choice(CardFunctions.card_deck))
            player_hand.append(random.choice(CardFunctions.card_deck))
            player_hand.append(random.choice(CardFunctions.card_deck))

            first_card = dealer_hand[0]
            dealer_value += first_card['value']
            dealer_info += first_card['number'] + first_card['suit'] + ''                
            for i in player_hand:
                player_info += i['number']+i['suit'] + ''
                if i['number'] == '[A ' and i['value2'] + player_value < 22:
                    player_value += i['value2']
                else:
                    player_value += i['value']
                
            print(f'Dealer\'s hand: {dealer_info} with a value of {dealer_value}')
            print(f'Player\'s hand: {player_info} with a value of {player_value}')
            
            while hand_in_progress:
                user_choice = input('1: hit 2: stay: ').strip()

                while user_choice not in ['1', '2']:
                    user_choice = int(input('Invalid Selection. please type 1 for hit or 2 for stay: '))
                
                user_choice = int(user_choice)

                if user_choice == 1 and player_value < 21:

                    new_card = random.choice(CardFunctions.card_deck)
                    player_hand.append(new_card)
                    if new_card['number'] == '[A ':
                        player_value += 11
                    else:
                        player_value += new_card['value']
                    player_info += new_card['number'] + new_card['suit'] + ''

                    
                    while player_value > 21 and '[A ' in player_info:
                        player_value -= 10
                        player_info = player_info.replace('[A ', '[ A')

                    print(f'Dealer\'s hand: {dealer_info} with a value of {dealer_value}')
                    print(f'Player\'s hand: {player_info} with a value of {player_value}')
                    
                    if player_value > 21:
                        print('Busted!')
                        hand_in_progress = False
                                                           
                elif user_choice == 2 or player_value == 21:
                    while dealer_value < 17:
                        new_card = random.choice(CardFunctions.card_deck)
                        dealer_hand.append(new_card)
                        if new_card['number'] == '[A ' and new_card['value2'] + dealer_value < 22:
                            dealer_value += new_card['value2']
                        else:
                            dealer_value += new_card['value']
                        dealer_info += new_card['number']+ new_card['suit'] + ''
                        print(f'Dealer\'s hand: {dealer_info} with a value of {dealer_value}')
                    
                    if dealer_value > 21:
                        print('Dealer Busts! You Win!')
                
                    hand_in_progress = False
                
                        


                    
                
                
            


print(BlackJack.play_blackjack())
