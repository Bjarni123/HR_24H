import math

class Vector:

    CLOSE_ENOUGH = 0.0000001

    def __init__(self, num1 = 0, num2 = 0, num3 = 0):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __str__(self):
        return f'[[ {self.num1} {self.num2} {self.num3} ]]'
    
    def __abs__(self):
        return math.sqrt(self.num1 ** 2 + self.num2 ** 2 + self.num3 ** 2)
    
    def __add__(self, other: "Vector"):
        new_num1 = self.num1 + other.num1
        new_num2 = self.num2 + other.num2
        new_num3 = self.num3 + other.num3
        return Vector(new_num1, new_num2, new_num3)
    
    def __sub__(self, other: "Vector"):
        num1 = self.num1 - other.num1
        num2 = self.num2 - other.num2
        num3 = self.num3 - other.num3
        return Vector(num1, num2, num3)

    def __eq__(self, other: "Vector"):
        new_vector = self - other
        if new_vector.__abs__() < Vector.CLOSE_ENOUGH:
            return True
        else:
            return False
        
    def __mul__(self, scalar):
        num1 = self.num1 * scalar
        num2 = self.num2 * scalar
        num3 = self.num3 * scalar
        new_vector = Vector(num1, num2, num3)
        return new_vector
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.num1}, {self.num2}, {self.num3})'

    def __gt__(self, other: "Vector"):
        placement_vector = Vector(self.num1, self.num2, self.num3)
        placement_length = abs(placement_vector)
        other_length = abs(other)
        length = placement_length - other_length
        return length > 0
    
    def __ge__(self, other: "Vector"):
        return self > other or self == other
    
    def __lt__(self, other: "Vector"):
        return not (self >= other)
    
    def __le__(self, other: "Vector"):
        return not(self > other)
    
    def dot(self, other: "Vector"):
        num1 = self.num1 * other.num1
        num2 = self.num2 * other.num2
        num3 = self.num3 * other.num3
        return num1 + num2 + num3
    
    def cross(self, other: "Vector"):
        num1 = (self.num2 * other.num3) - (self.num3 * other.num2)
        num2 = (self.num3 * other.num1) - (self.num1 * other.num3)
        num3 = (self.num1 * other.num2) - (self.num2 * other.num1)
        return Vector(num1, num2, num3)

    

