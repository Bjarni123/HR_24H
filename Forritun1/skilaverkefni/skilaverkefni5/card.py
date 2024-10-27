class Card:
    def __init__(self, rank, suit) -> None:
        self.sortDict = {'Q': }
        if type(rank) == str:
            match rank:
                case 'J':
                    self.rank = 11
                case 'Q':
                    self.rank = 12
                case 'K':
                    self.rank = 13
                case 'A':
                    self.rank = 14
        else:
            self.rank = rank

        self.suit = suit

    def __str__(self) -> str:
        return f'{self.rank}{self.suit}'