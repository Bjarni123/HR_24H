class Card:
    def __init__(self, rank, suit) -> None:
        self.face_to_rank_dir = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.rank_to_face_dir = {rank: face for face, rank in self.face_to_rank_dir.items()}
        
        try:
            self.rank = int(rank)
        except:
            self.rank = self.face_to_rank_dir[rank]
        """ 
        if type(rank) == str:
            self.rank = self.face_to_rank_dir[rank]
        else:
            self.rank = int(rank)
        """
        self.suit = suit

    def __str__(self) -> str:
        if self.rank <= 10:
            return f'{self.rank}{self.suit}'
        else:
            rank_num = self.rank_to_face_dir[self.rank]

            return f'{rank_num}{self.suit}'