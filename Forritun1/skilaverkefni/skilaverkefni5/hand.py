class Hand:
        
    NUMBER_OF_CARDS = 13

    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        # Empty / all cards with space between
        if self.cards:
            return "-".join([str(card) for card in self.cards]) + "-"
        else:
            return "Empty"

    def add_card(self, card):
        # add card to hand if there are not 13 cards already
        if len(self.cards) < self.NUMBER_OF_CARDS:
            self.cards.append(card)