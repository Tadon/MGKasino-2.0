import random

class CardFunctions:
    

    card_deck = {

    #hearts
    1: {'number': '[2 ', 'suit':'♥]', 'value': 2, 'value2': 0 }, 2: {'number': '[3 ', 'suit':'♥]','value': 3, 'value2': 0 }, 3: {'number': '[4 ', 'suit':'♥]','value': 4, 'value2': 0 }, 4: {'number': '[5 ', 'suit':'♥]','value': 5, 'value2': 0 }, 5: {'number': '[6 ', 'suit':'♥]','value': 6, 'value2': 0 },
    6: {'number': '[7 ', 'suit':'♥]','value': 7, 'value2': 0 }, 7: {'number': '[8 ', 'suit':'♥]','value': 8, 'value2': 0 }, 8: {'number': '[9 ', 'suit':'♥]','value': 9, 'value2': 0 }, 9: {'number': '[10', 'suit':'♥]','value': 10, 'value2': 0 }, 10: {'number': '[J ', 'suit':'♥]','value': 10, 'value2': 0 },
    11: {'number': '[Q ', 'suit':'♥]','value': 10, 'value2': 0 }, 12:{'number': '[K ', 'suit':'♥]','value': 10, 'value2': 0 }, 13:{'number': '[A ', 'suit':'♥]','value': 1, 'value2': 11},

    #diamonds
    14: {'number': '[2 ', 'suit':'♦]', 'value': 2, 'value2': 0 }, 15: {'number': '[3 ', 'suit':'♦]','value': 3, 'value2': 0 }, 16: {'number': '[4 ', 'suit':'♠]','value': 4, 'value2': 0 }, 17: {'number': '[5 ' , 'suit':'♦]','value': 5, 'value2': 0 }, 18: {'number': '[6 ', 'suit':'♦]','value': 6, 'value2': 0 },
    19: {'number': '[7 ', 'suit':'♦]', 'value': 7, 'value2': 0 }, 20: {'number': '[8 ', 'suit':'♦]','value': 8, 'value2': 0 }, 21: {'number': '[9 ', 'suit':'♠]','value': 9, 'value2': 0 }, 22: {'number': '[10', 'suit':'♦]','value': 10, 'value2': 0}, 23: {'number': '[J ', 'suit':'♦]','value': 10, 'value2': 0},
    24: {'number': '[Q ', 'suit':'♦]','value': 10, 'value2': 0 }, 25: {'number': '[K ', 'suit':'♦]','value': 10, 'value2': 0}, 26: {'number': '[A ', 'suit':'♠]','value': 1, 'value2': 11},

    #spades
    27: {'number': '[2 ', 'suit':'♠]', 'value': 2, 'value2': 0 }, 28: {'number': '[3 ', 'suit':'♠]','value': 3, 'value2': 0 }, 29: {'number': '[4 ', 'suit':'♠]','value': 4, 'value2': 0 }, 30: {'number': '[5 ' , 'suit':'♠]','value': 5, 'value2': 0 }, 31: {'number': '[6 ', 'suit':'♠]','value': 6, 'value2': 0 },
    32: {'number': '[7 ', 'suit':'♠]', 'value': 7, 'value2': 0 }, 33: {'number': '[8 ', 'suit':'♠]','value': 8, 'value2': 0 }, 34: {'number': '[9 ', 'suit':'♠]','value': 9, 'value2': 0 }, 35: {'number': '[10', 'suit':'♠]','value': 10, 'value2': 0}, 36: {'number': '[J ', 'suit':'♠]','value': 10, 'value2': 0},
    37: {'number': '[Q ', 'suit':'♠]','value': 10, 'value2': 0 }, 38: {'number': '[K ', 'suit':'♠]','value': 10, 'value2': 0}, 39: {'number': '[A ', 'suit':'♠]','value': 1, 'value2': 11},

    #clubs
    40: {'number': '[2 ', 'suit':'♣]', 'value': 2, 'value2': 0 }, 41: {'number': '[3 ', 'suit':'♣]','value': 3, 'value2': 0 }, 42: {'number': '[4 ', 'suit':'♣]','value': 4, 'value2': 0 }, 43: {'number': '[5 ' , 'suit':'♣]','value': 5, 'value2': 0 }, 44: {'number': '[6 ', 'suit':'♣]','value': 6, 'value2': 0 },
    45: {'number': '[7 ', 'suit':'♣]', 'value': 7, 'value2': 0 }, 46: {'number': '[8 ', 'suit':'♣]','value': 8, 'value2': 0 }, 47: {'number': '[9 ', 'suit':'♣]','value': 9, 'value2': 0 }, 48: {'number': '[10', 'suit':'♣]','value': 10, 'value2': 0}, 49: {'number': '[J ', 'suit':'♣]','value': 10, 'value2': 0},
    50: {'number': '[Q ', 'suit':'♣]','value': 10, 'value2': 0 }, 51: {'number': '[K ', 'suit':'♣]','value': 10, 'value2': 0}, 52: {'number': '[A ', 'suit':'♣]','value': 1, 'value2': 11}

    


}

    #stack datastructure used to build card decks
    class DeckBuilder:
        def __init__(self):
            self.deck = []
        
        def is_empty(self):
            return len(self.deck) == 0
        
        def push(self, card):
            self.deck.append(card)
        
        def pop(self):
            if not self.is_empty():
                return self.deck.pop()
            else:
                print('Empty deck!')
        
        def size(self):
            return len(self.deck)

    
    #method to generate a deck
    def deck_generator(card_deck, num_decks = 1): 
        counter = 52 * num_decks
        pre_shuffled = list(range(1,53)) * num_decks
        post_shuffled = []
        shuffled_deck = CardFunctions.DeckBuilder()
        while counter > 0:
            random_ind = random.randint(0, counter - 1)
            random_num = pre_shuffled.pop(random_ind)
            post_shuffled.append(random_num)
            counter -= 1
        for i in post_shuffled:
            shuffled_deck.push(card_deck[i])

        return shuffled_deck
    
    def get_card():
        return CardFunctions.card_deck[random.randint(1, len(CardFunctions.card_deck))]

        

'''while counter < (52 * CardFunctions.num_decks) +1 :
    card = new_deck.pop()
    print(f"Your # {counter} {card['number']}{card['suit']}, which has a value of {card['value']}.")
    counter += 1'''



    