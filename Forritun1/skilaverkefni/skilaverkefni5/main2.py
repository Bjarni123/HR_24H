import random
from card import Card
from deck import Deck
from hand import Hand

def main():
    """The main program for testing the classes Card, Deck and Hand."""

    random.seed(10)
    test_cards()

    deck = Deck()
    print("The deck:")
    print(deck)
    deck.shuffle()
    print("The deck after shuffling:")
    print(deck)

    test_hands(deck)
    print("The deck after dealing:")
    print(deck)


def test_cards():
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
    
def test_hands(deck):
    hands_list = [Hand(), Hand(), Hand(), Hand()]
    print("The hands:")
    print_hands(hands_list)

    deal_hands(deck, hands_list)
    print("The hands after dealing:")
    print_hands(hands_list)


def print_hands(hands_list):
    """Prints each hand in the list."""
    for hand in hands_list:
        print(hand)
    

def deal_hands(deck, hands):
    """Deals cards for the hands."""
    for _ in range(Hand.NUMBER_OF_CARDS):
        for hand in hands:
            hand.add_card(deck.deal())


if __name__ == "__main__":
    main()