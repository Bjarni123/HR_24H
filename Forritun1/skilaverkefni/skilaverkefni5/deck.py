import random

from card import Card

class Deck:
    
    def __init__(self) -> None:
        # only deck is supposed to be public instance, maybe take this out
        self.suits_list = ['H', 'S', 'D', 'C']
        self.ranks_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        self.deck = []

        for suit in self.suits_list:
            for rank in self.ranks_list:
                card = Card(rank, suit)
                self.deck.append(card)

        # sort by suit (heart, spades, diamonds, club)  

    def __str__(self) -> str:
        return_string = ''
        counter = 0
        for card in self.deck:
            return_string += str(card)
            counter += 1

            if counter % 13 == 0 and card not in [self.deck[-1]]:
                return_string += '-\n'
            else:
                return_string += '-'
        
        
        return return_string

    def shuffle(self):
        # Shuffle the deck
        # Not random.seed
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop(0)
