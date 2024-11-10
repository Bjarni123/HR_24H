from stored_number import StoredNumber

class ManyStoredNumbers:
    def __init__(self):
        self.numbers = []
    
    def add_stored_number(self, number):
        self.numbers.append(number)

    def __str__(self):
        return_string = 'these are the numbers:\n'
        for number in self.numbers:
            return_string += str(number) + '\n'
        return return_string.strip()
    
if __name__ == '__main__':
    many_stored = ManyStoredNumbers()
    many_stored.add_stored_number(StoredNumber(4.6))
    many_stored.add_stored_number(StoredNumber(-3))
    print(many_stored)
    many_stored.add_stored_number(StoredNumber(9.0))
    print(many_stored)