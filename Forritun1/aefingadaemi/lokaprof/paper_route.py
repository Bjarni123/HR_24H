
# Hægt að halda áfram og gera mismunandi hús

class Doors:
    def __init__(self):
        self.doors = dict()

    def __str__(self):
        return_string = ''
        for door_number, paper_amount in self.doors.items():
            return_string += (f'{door_number}\t{paper_amount}\n')
        return return_string.strip()

    def add_door(self, paper_amount):
        door_length = len(self.doors)
        self.doors[door_length + 1] = paper_amount

    def edit_door(self):
        print(self)
        door_nr = int(input('Enter number of door: '))
        if door_nr:
            paper_amount = int(input('Enter paper amount: '))
            self.doors[door_nr] = paper_amount

def main():
    doors_class = Doors()
    choice = 0

    while choice != 9:
        print('1. Add a door')
        print('2. View doors')
        print('3. Edit doors')
        print('9. Quit')

        choice = int(input('What would you like to do: '))

        match choice:
            case 1:
                paper_amount = int(input('How many papers should the door have: '))
                doors_class.add_door(paper_amount)
            case 2:
                print(doors_class)
            case 3:
                doors_class.edit_door()
            case 9:
                print('Thank you for your time!')
            case _:
                print('Please enter a valid number!')



if __name__ == '__main__':
    main()