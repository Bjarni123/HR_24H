from shape import Shape

class Square(Shape):
    def __init__(self, x):
        # Create parent class
        super().__init__()

        # Create area and perimeter
        self.area = x * x
        self.perimeter = 4 * x
