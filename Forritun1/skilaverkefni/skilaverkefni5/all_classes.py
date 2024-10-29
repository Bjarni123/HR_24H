import random

class Card:
    def __init__(self, rank, suit) -> None:
        self._face_to_rank_dir = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self._rank_to_face_dir = {rank: face for face, rank in self._face_to_rank_dir.items()}
        
        try:
            self.rank = int(rank)
        except:
            self.rank = self._face_to_rank_dir[rank]
        
        self.suit = suit

    def __str__(self) -> str:
        if self.rank <= 10:
            return f'{str(self.rank).rjust(2)}{self.suit.ljust(1)}'
        else:
            rank_num = self._rank_to_face_dir[self.rank]

            return f'{str(rank_num).rjust(2)}{self.suit.ljust(1)}'



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
                return_string += ' \n'
            else:
                return_string += ' '
        
        
        return return_string

    def shuffle(self):
        # Shuffle the deck
        # Not random.seed
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop(0)
    
    

class Hand:
        
    NUMBER_OF_CARDS = 13

    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        # Empty / all cards with space between
        if self.cards:
            """ return_value = ''
            for card in self.cards:
                return_value += ' ' + str(card)

            return return_value """

            return " ".join([str(card) for card in self.cards]) + " "
        else:
            return "Empty"

    def add_card(self, card):
        # add card to hand if there are not 13 cards already
        if len(self.cards) < 13:
            self.cards.append(card)