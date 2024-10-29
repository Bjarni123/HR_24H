class Shape:
    def __init__(self):
        # Create variables, store them as None
        self.area = None
        self.perimeter = None

    def get_perimeter(self):
        # return the perimeter
        return self.perimeter
        
    def get_area(self):
        # Return the area
        return self.area

    def __str__(self):
        # Print out the sentence with all variables, max 2 decimals
        return '{} with area of {:.2f} and perimeter of {:.2f}'.format(self.__class__.__name__, self.get_area(), self.get_perimeter())