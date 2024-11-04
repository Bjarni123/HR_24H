class Card:

    # Create dictionaries to convert face value to rank and vice versa
    FACE_TO_RANK = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    RANK_TO_FACE = {rank: face for face, rank in FACE_TO_RANK.items()}

    def __init__(self, rank, suit) -> None:
        
        # Create self.suit
        self.suit = suit

        # if rank is int, we set the value of it into self.rank
        if type(rank) == int:
            self.rank = rank
        # else if the rank is in the face to rank directory, we convert it accordingly
        # and set the value to self.rank
        elif rank in Card.FACE_TO_RANK:
            self.rank = Card.FACE_TO_RANK[rank]
        # Else the rank is an int in the type string('2') and then we make self.rank = int(rank)
        else:
            self.rank = int(rank)

    def rank_to_str(self) -> str:
        """Return self.rank in a printing format. f.x. 'Q' -> 12, 10 -> '10'"""
        # If the rank is 10 or less we return self.rank as a string
        if self.rank <= 10:
            return str(self.rank)
        # Else we return the appropriate face value
        else:
            return Card.RANK_TO_FACE[self.rank]
        

    def __str__(self) -> str:
        # return the the card with the appropiate spacing
        return f'{self.rank_to_str().rjust(2)}{self.suit.ljust(1)}'
