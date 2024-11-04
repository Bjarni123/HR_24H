import random

from card import Card

class Deck:
    
    def __init__(self) -> None:
        # Create the deck as a list
        self.deck = []

        # loop through all possible suits
        for suit in ['H', 'S', 'D', 'C']:
            # loop through every single value between 2-14
            for rank in range(2, 15):
                # Create the card with the suit and rank
                card = Card(rank, suit)
                # add the card to the deck
                self.deck.append(card)


    def __str__(self) -> str:
        # Create the return string (Could be bad practise to have string to hold it)
        return_string = ''

        # Create a counter for the newline
        newline_counter = 0
        # Loop throught the deck
        for card in self.deck:
            # add the card to the string
            return_string += str(card)
            # add to the counter
            newline_counter += 1

            # if the newline counter is divisable by 13, we have newline
            # (There's no newline in the beginning since we add to the newline counter before the print
            # so when first card goes to here, the counter has already become 1)
            if newline_counter % 13 == 0 and card != self.deck[-1]:
                return_string += ' \n'
            # Otherwise we have a space
            else:
                return_string += ' '
        
        
        return return_string

    def shuffle(self):
        """ Shuffle the deck """
        random.shuffle(self.deck)
    
    def deal(self):
        """ takes out the first card, removes it from the deck and returns it """
        return self.deck.pop(0)