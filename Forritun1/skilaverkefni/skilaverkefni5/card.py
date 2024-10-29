class Card:
    def __init__(self, rank, suit) -> None:
        # Create 2 private variables to convert rank to face and face to rank
        self._face_to_rank_dir = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self._rank_to_face_dir = {rank: face for face, rank in self._face_to_rank_dir.items()}
        
        # Attempt to 
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