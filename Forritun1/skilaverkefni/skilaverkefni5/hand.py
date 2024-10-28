class Hand:
        
    NUMBER_OF_CARDS = 13

    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        # Empty / all cards with space between
        if self.cards:

            # Here a space is always before each card in hand
            return_value = ''
            for card in self.cards:
                return_value += ' ' + str(card)

            return return_value

            # Here there are no spaces
            # return " ".join([str(card) for card in self.cards])
        else:
            return "Empty"

    def add_card(self, card):
        # add card to hand
        self.cards.append(card)