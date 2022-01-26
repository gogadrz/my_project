import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def do_intersect(self, other):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return abs(self.radius - other.radius) <= dist <= self.radius + other.radius


circle = Circle(1, 1, 2)
circle2 = Circle(4, 2, 2)
print(circle.do_intersect(circle2))
