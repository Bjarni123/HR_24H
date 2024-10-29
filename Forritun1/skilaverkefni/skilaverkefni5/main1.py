import random

# from all_classes import Card, Deck, Hand


from card import Card
from deck import Deck
from hand import Hand


def main():
    """The main program for testing the classes Card, Deck and Hand."""
    random.seed(10)
    card1 = Card(5,'S')
    print(card1)
    card2 = Card('Q','D')
    print(card2)
    card3 = Card(13, 'H')
    print(card3)
    card4 = Card(2, 'C')
    print(card4)
    card6 = Card('A', 'S')
    print(card6)
    card7 = Card(10, 'D')
    print(card7)

    print(card1,card2,card3,card4,card6)
    

    print()
    deck = Deck()
    deck.shuffle()
    print(deck)
    print()


    
    hand = Hand()
    for _ in range(Hand.NUMBER_OF_CARDS):
        hand.add_card(deck.deal())
    print(hand)
    print()
   
    print(deck)


    
if __name__ == "__main__":
    main()
