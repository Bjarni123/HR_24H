class StoredNumber():
    def __init__(self, nr):
        self.nr = nr

    def __str__(self):
        return (f'The number: {self.nr}')

    def get_number(self):
        return self.nr
    
    def set_number(self, nr):
        self.nr = nr
