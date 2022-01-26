import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def increase(self, k):
        self.r *= k

    def is_circles_intersect(self, other_circle):
        dist = ((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2) ** 0.5
        return abs(self.r - other_circle.r) <= dist <= self.r + other_circle.r

    def show_imfo(self):
        print('Координаты: X: {}, Y: {}, радиус: {}, площадь: {}, периметр: {}'.format(
            self.x,
            self.y,
            self.r,
            self.area(),
            self.perimeter()
        ))


print('Первая окружность:')
circle = Circle(2, 1, 2)
circle.show_imfo()
print()
print('Увеличим её в 2 раза')
circle.increase(2)
circle.show_imfo()
print()
print('Вторая окружность:')
circle_2 = Circle(5, 6, 2)
circle_2.show_imfo()

print()
if circle.is_circles_intersect(circle_2):
    print('Окружности пересекаются.')
else:
    print('Окружности не пересекаются.')
