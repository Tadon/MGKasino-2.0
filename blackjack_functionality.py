from card_functions import CardFunctions
from user_information import UserInformation
import random
import time

balance = 10000

class BlackJack:

    def __init__(self, balance):
        self.balance = balance

    def play_blackjack(balance):
        balance = balance
        playing_blackjack = True
        print('Welcome to MGBlackjack! Where the odds are always in our favor.')
        while playing_blackjack:
            
            ##Required variables to hold blackjack hand information        
            dealer_value, player_value = 0, 0 #holding the numerical value of player and dealer hands
            dealer_hand, player_hand = [], [] #holding dictionary info pulled from actual card deck, information here is used to add  value to value variables and concantenate onto info variables so we can display the cards to user
            dealer_info, player_info = "", "" #adding number and suit values from dealer/player hand variables to these strings, concantenating them so the user can visibly see the cards in their hand
            initial_hand = ""
            wager_amount = 0
            hand_in_progress = True
            pre_hand = True

            playing_blackjack, wager_amount, pre_hand, hand_in_progress = BlackJack.get_wager(balance)
            
            while pre_hand:
                #dealing 4 initial cards before hand begins
                dealer_hand.append(BlackJack.deal_card())
                player_hand.append(BlackJack.deal_card())
                dealer_hand.append(BlackJack.deal_card())
                player_hand.append(BlackJack.deal_card())

                #adding first card dealt to dealer hand to dealer value and info
                first_card = dealer_hand[0]
                second_card = dealer_hand[1]
                dealer_value = dealer_value + first_card['value'] + second_card['value']
                dealer_info += first_card['number'] + first_card['suit'] + '' + second_card['number'] + second_card ['suit'] + ''
                initial_hand += first_card['number'] + first_card['suit'] + '[ ? ]'
                

                #adding both initial player dealt cards to player info and value      
                for i in player_hand:
                    player_info += i['number']+i['suit'] + ''
                    if i['number'] == '[A ' and i['value2'] + player_value < 22:
                        player_value += i['value2']
                    else:
                        player_value += i['value']

                #displaying initially dealt hands               
                print(f'Dealer\'s hand: {initial_hand} with a value of {first_card["value"]}')
                print(f'Player\'s hand: {player_info} with a value of {player_value}')
                if dealer_value == 21 and player_value == 21:
                    print('Double blackjack! Push!')
                    hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                
                if dealer_value == 21:
                    print('Dealer blackjack! You lose')
                    hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                    balance -= wager_amount
                    
                #if player is dealt a blackjack, player wins and hand ends
                if player_value == 21:
                    print('Blackjack! You win!')
                    hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                    balance += (wager_amount * 1.5)
                
                pre_hand = False

            #while loop that keeps player in individual hand until it ends
            while hand_in_progress:
                
                #taking in choice from user as a string, so that we can use strip method to make sure we can read the input, then converting string to int
                user_choice = input('1: hit 2: stay: ').strip()
                #user_choice = int(user_choice)

                while user_choice != '1' and user_choice != '2':
                    user_choice = input('Invalid Selection. please type 1 for hit or 2 for stay: ').strip()
                
                

                if user_choice == '1' and player_value < 21:

                    new_card = BlackJack.deal_card()
                    player_hand.append(new_card)
                    if new_card['number'] == '[A ':
                        player_value += 11
                    else:
                        player_value += new_card['value']
                    player_info += new_card['number'] + new_card['suit'] + ''

                    
                    while player_value > 21 and '[A ' in player_info:
                        player_value -= 10
                        player_info = player_info.replace('[A ', '[ A')

                    print(f'Dealer\'s hand: {initial_hand}')
                    print(f'Player\'s hand: {player_info}')

                    if player_value == 21:
                        continue
                    
                    if player_value > 21:
                        print('Busted!')
                        hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                        balance -= wager_amount
                                                           
                elif user_choice == '2' or player_value == 21:
                    print(f'Dealer\'s Hand: {dealer_info}')
                    while dealer_value < 17:
                        time.sleep(1)
                        new_card = BlackJack.deal_card()
                        dealer_hand.append(new_card)
                        if new_card['number'] == '[A ' and new_card['value2'] + dealer_value < 22:
                            dealer_value += new_card['value2']
                        else:
                            dealer_value += new_card['value']
                        dealer_info += new_card['number']+ new_card['suit'] + ''
                        print(f'Dealer\'s hand: {dealer_info} with a value of {dealer_value}')
                    
                    if dealer_value > 21:
                        print('Dealer Busts! You Win!')
                        hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                        balance += wager_amount
                    
                    elif dealer_value < 22 and dealer_value > player_value:
                        print(f'Dealer wins with a value of {dealer_value}')
                        hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                        balance -= wager_amount

                    elif player_value < 22 and player_value > dealer_value:
                        print(f'You win with a value of {player_value}')
                        hand_in_progress, playing_blackjack = BlackJack.end_of_hand()
                        balance += wager_amount
        return balance
    
    def end_of_hand():
        

        user_choice = input('Play again? 1: yes 2: no: ').strip()
        

        while user_choice != '1' and user_choice != '2':
            user_choice = input('invalid choice. please type 1 for yes or 2 for no: ').strip()
        
        if user_choice == '1':
            playing_blackjack = True
            hand_in_progress = False
        
        if user_choice == '2':
            hand_in_progress = False
            playing_blackjack = False              

        return hand_in_progress, playing_blackjack

    def deal_card():
        card_list = list(CardFunctions.card_deck.values())
        return random.choice(card_list)
                    
    def get_wager(balance):
        valid_wager = 0
        hand_in_progress = True
        playing_blackjack = True
        pre_game = True
        if balance < 1:
            pre_game = False
            hand_in_progress = False
            playing_blackjack = False
            print(f'Your balance is {balance}! Please deposit before playing.')
            return playing_blackjack, valid_wager, pre_game, hand_in_progress
        wager_amount = input('Enter wager amount or type exit to exit: ').strip().lower()
        if wager_amount == 'exit':
            pre_game = False
            hand_in_progress = False
            playing_blackjack = False   
        if wager_amount.isdigit():
            valid_wager = float(wager_amount)
        while valid_wager > balance:
            valid_wager = float(input(f'You can\'t bet more than your wager! Please make sure your bet is not higher than {balance}: '))
                     
        return playing_blackjack, valid_wager, pre_game, hand_in_progress        
            



