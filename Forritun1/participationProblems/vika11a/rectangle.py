from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y):
        # Create parent class
        super().__init__()

        # Create area and perimeter
        self.area = x*y
        self.perimeter = 2*x + 2*y

    