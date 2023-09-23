from card_functions import CardFunctions
import random
import time

class BlackJack:
    def __init__(self, balance):
        self.balance = balance
        self.dealer_hand , self.player_hand = [], []
        self.dealer_value, self.player_value = 0, 0
        self.dealer_info, self.player_info = "", ""
        self.playing_blackjack = True
        self.initial_hand = ''
        self.pre_hand = True
        self.hand_in_play = True
        self.wager_amount = 0
        self.double_down = False
    
    #are you seated at the table
    def play_blackjack(self):
        print(f'Welcome to Blackjack! Where the odds are always in our favor.')
        while self.playing_blackjack:

            print(f'Current balance: {self.balance}')
            self.dealer_hand , self.player_hand = [], []
            self.dealer_value, self.player_value = 0, 0
            self.dealer_info, self.player_info = "", ""
            self.playing_blackjack = True
            self.pre_hand = True
            self.hand_in_play = True
            self.wager_amount = 0
            self.double_down = False


            self.get_wager()

            self.start_hand()
            
            self.play_hand()
            
            self.finish_hand()

        return self.balance

    

    #how much would you like to bet
    def get_wager(self):
        
        
        if self.balance < 1:
            self.pre_hand = False
            self.hand_in_play = False
            self.playing_blackjack = False
            print(f'Your balance is {self.balance}! Please deposit more credits before playing.')
            return None
        
        self.wager_amount = input('Enter wager amount or type exit to exit: ').strip().lower()

        while not (self.wager_amount.isdigit() or self.wager_amount == 'exit'):
            self.wager_amount = input('Invalid input. Please enter a number value or type exit to exit').strip().lower()

        if self.wager_amount == 'exit':
            self.pre_hand = False
            self.hand_in_play = False
            self.playing_blackjack = False
            return None

        while float(self.wager_amount) > self.balance:
            self.wager_amount = input(f'Invalid input. You can\'t bet more than your balance! Your current balance is {self.balance}. Type exit to exit: ').strip().lower()

            while not (self.wager_amount.isdigit() or self.wager_amount == 'exit'):
                self.wager_amount = input('Invalid input. Please enter a number value or type exit to exit: ').strip().lower()

            if self.wager_amount == 'exit':
                self.pre_hand = False
                self.hand_in_play = False
                self.playing_blackjack = False
                return None
            
        
        self.wager_amount = float(self.wager_amount)
        self.balance = self.balance - self.wager_amount
        return None
    
    #dealing initial part of the hand
    def start_hand(self):
        while self.pre_hand:
            self.hand_in_play = True
            #dealing player and dealer initial hands
            self.dealer_hand.append(self.deal_card())
            self.player_hand.append(self.deal_card())
            self.dealer_hand.append(self.deal_card())
            self.player_hand.append(self.deal_card())

            #adding first two cards to dealer hand, plus adding logic so player cannot see dealer's undercard
            first_card = self.dealer_hand[0]
            self.initial_hand = first_card['number'] + first_card['suit'] + '[ ? ]'
            for i in self.dealer_hand:
                self.dealer_info += i['number'] + i['suit'] + ''
                if i['number'] == '[A ' and i['value2'] + self.dealer_value < 22:
                    self.dealer_value += i['value2']
                else:
                    self.dealer_value += i['value']

            #adding two initial cards to player info and value
            for i in self.player_hand:
                self.player_info += i['number']+i['suit'] + ''
                if i['number'] == '[A ' and i['value2'] + self.player_value < 22:
                    self.player_value += i['value2']
                else:
                    self.player_value += i['value']
            
            #displaying initially dealt hands
            print(f'Dealer\'s hand: {self.initial_hand} with a value of {first_card["value"]}.')
            print(f"Player\'s hand: {self.player_info} with a value of {self.player_value}.")

            #insurance logic
            if first_card['number'] == '[A ':
                if self.balance < (self.wager_amount / 2):
                    print('Sorry! Not enough balance to take insurance.')
                
                else:
                    user_choice = input('Insurance? 1 for yes or 2 for no: ').strip()
                    while user_choice != '1' and user_choice != '2':
                        user_choice = input('Invalid input. Please enter 1 to take insurance, or 2 to not take insurance.').strip()
                    
                    if user_choice == '1' and self.dealer_value == 21:
                        print('Dealer Blackjack! Insurance pays 2 to 1')
                        self.hand_in_play = False
                        self.pre_hand = False
                        self.balance += self.wager_amount
                        return None
                    
                    elif (user_choice == '1' or user_choice == '2') and self.dealer_value != 21:
                        print('No blackjack!')
                        self.balance -= self.wager_amount / 2
                
            
            #double blackjack
            if self.dealer_value == 21 and self.player_value == 21:
                print('Double Blackjack! Push!')
                self.balance += self.wager_amount
                self.finish_hand()

            elif self.dealer_value == 21 and self.player_value != 21:
                print('Dealer Blackjack! You lose')
                self.finish_hand()

            elif self.player_value == 21 and self.dealer_value != 21:
                print('Blackjack! You win!')
                self.balance += self.wager_amount * 2.5
                self.finish_hand()

            self.pre_hand = False

    #actual hand being played by player
    def play_hand(self):
        while self.hand_in_play:
            user_choice = input('1: hit 2: stay: 3: double down ').strip()

            while user_choice != '1' and user_choice != '2' and user_choice != '3':
                user_choice = input('Invalid selections, please type 1 for hit or 2 for stay: ')

            if user_choice == '3':
                if self.balance < self.wager_amount:
                    print('Insufficient funds!')
                else:
                    self.double_down = True
                    print('Double down! Good luck!')
                    self.balance = self.balance - self.wager_amount
                    self.wager_amount = self.wager_amount * 2
                    new_card = self.deal_card()
                    self.player_hand.append(new_card)
                    self.player_info += new_card['number']+ new_card['suit'] + ''
                    self.player_value += new_card['value']

                    while self.player_value > 21 and '[A ' in self.player_info:
                        self.player_value -= 10
                        self.player_info = self.player_info.replace('[A ', '[ A')
                    print(f'{self.player_info} with a value of {self.player_value}!')

                    if self.player_value > 21:
                        print('Busted! Better luck next time.')
                        self.finish_hand()

            if user_choice == '1'and self.player_value < 21:
                new_card = self.deal_card()
                self.player_hand.append(new_card)
                if new_card['number'] == '[A ':
                    self.player_value += new_card['value2']
                else:
                    self.player_value += new_card['value']
                self.player_info += new_card['number'] + new_card['suit'] + ''

                while self.player_value > 21 and '[A ' in self.player_info:
                    self.player_value -= 10
                    self.player_info = self.player_info.replace('[A ', '[ A')
                
                print(f'Dealer\'s hand: {self.initial_hand}.')
                print(f'Player\'s hand: {self.player_info} with a value of {self.player_value}')

                if self.player_value == 21:
                    print('Player has 21! Nice!')
                    break

                if self.player_value > 21:
                    print('Busted!')
                    self.finish_hand()
            

            elif (user_choice == '2' or self.player_value == 21 or self.double_down) and self.hand_in_play:
                print(f'Dealer\'s hand: {self.dealer_info} with a value of {self.dealer_value}')

                while self.dealer_value < 17:
                    time.sleep(1)
                    new_card = self.deal_card()
                    self.dealer_hand.append(new_card)

                    if (new_card['number'] == '[A ') and (new_card['value2'] + self.dealer_value < 22):
                        self.dealer_value += new_card['value2']
                    
                    else:
                        self.dealer_value += new_card['value']
                    while self.player_value > 21 and '[A ' in self.player_info:
                        self.dealer_value -= 10
                        self.dealer_value = self.player_info.replace('[A ', '[ A')
                    self.dealer_info += new_card['number'] + new_card['suit'] + ''
                    print(f'Dealer\'s hand: {self.dealer_info} with a value of {self.dealer_value}')

                if self.dealer_value > 21:
                    print('Dealer Busts! You win!')
                    self.balance += (self.wager_amount * 2)
                    self.finish_hand()
                
                elif self.dealer_value < 22 and self.dealer_value > self.player_value:
                    print(f'Dealer wins with a {self.dealer_value}. Good luck next time!')
                    self.finish_hand()
                
                elif self.player_value < 22 and self.player_value > self.dealer_value:
                    print(f'You win {self.wager_amount}!')
                    self.balance += (self.wager_amount * 2)
                    self.finish_hand()
                
                elif self.player_value == self.dealer_value:
                    print(f'Push!')
                    self.balance += self.wager_amount
                    self.finish_hand()

    #when the hand ends
    def finish_hand(self):
        while self.hand_in_play:
            user_choice = input('Play again? 1 for yes or 2 for no: ').strip()

            while user_choice != '1' and user_choice != '2':
                user_choice = input('Invalid choice. Enter 1 to play again, or 2 to exit: ').strip()
            
            if user_choice == '1':
                self.playing_blackjack = True
                self.hand_in_play = False
                return None
            
            elif user_choice == '2':
                self.playing_blackjack = False
                self.hand_in_play = False
                self.pre_hand = False
                return None

            return None

    #dealing a card
    def deal_card(self):
        card_list = list(CardFunctions.card_deck.values())
        return random.choice(card_list)    
