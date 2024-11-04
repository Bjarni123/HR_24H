class Card:
    def __init__(self, rank, suit) -> None:
        # Create dictionaries to convert face value to rank and vice versa
        self._face_to_rank_dir = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self._rank_to_face_dir = {rank: face for face, rank in self._face_to_rank_dir.items()}
        
        # Create self.suit
        self.suit = suit

        # if rank is int, we set the value of it into self.rank
        if type(rank) == int:
            self.rank = rank
        # else if the rank is in the face to rank directory, we convert it accordingly
        # and set the value to self.rank
        elif rank in self._face_to_rank_dir:
            self.rank = self._face_to_rank_dir[rank]
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
            return self._rank_to_face_dir[self.rank]
        

    def __str__(self) -> str:
        # return the the card with the appropiate spacing
        return f'{self.rank_to_str().rjust(2)}{self.suit.ljust(1)}'
