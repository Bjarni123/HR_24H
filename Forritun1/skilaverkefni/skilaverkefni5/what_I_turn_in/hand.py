class Hand:
        
    # This is the max number of cards a hand is allowed to have
    NUMBER_OF_CARDS = 13

    def __init__(self) -> None:
        # list of card on the hand
        self.cards = []

    def __str__(self) -> str:
        # If there's any cards in the hand
        if self.cards:
            # We print them out with space between
            return " ".join([str(card) for card in self.cards]) + " "
        else:
            # Otherwise, we return "Empty"
            return "Empty"

    def add_card(self, card):
        """ add card to hand if there are not 13 cards already """
        if len(self.cards) < Hand.NUMBER_OF_CARDS:
            self.cards.append(card)