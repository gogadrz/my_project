import math
from typing import Union, List


class Square:
    """
    Базовый класс квадрат.

    :param side: длина стороны квадрата
    :type int:
    """
    def __init__(self, side: int) -> None:
        self.__side = side

    @property
    def side(self) -> int:
        return self.__side

    @side.setter
    def side(self, value: int) -> None:
        self.__side = value

    def perimeter(self) -> int:
        return 4 * self.side

    def area_2d(self) -> int:
        return self.side ** 2


class Triangle:
    """
    Базовый класс треугольник.

    :param base: длина основания треугольника
    :type int:
    :param height: высота треугольника
    :type int:
    """
    def __init__(self, base: int, height: int) -> None:
        self.__base = base
        self.__height = height

    @property
    def base(self) -> int:
        return self.__base

    @base.setter
    def base(self, value: int) -> None:
        self.__base = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        self.__height = value

    def perimetr(self) -> float:
        side = math.sqrt((self.base / 2) ** 2 + self.height ** 2)
        return self.base + side + side

    def area_2d(self) -> float:
        return self.base * self.height / 2


class AreaMixin:
    """
    Mixin
    Класс вычисляющий площадь 3D фигур

    :param data: список квадратов или треугольников, для вычисления площади.
    :type List[Square] or List[Triangle]:
    """
    def __init__(self, data: Union[List[Square], List[Triangle]]) -> None:
        self._2d_data = data

    def area(self) -> Union[int, float]:
        result = 0
        for i_square in self._2d_data:
            result += i_square.area_2d()

        return result


class Cube(Square, AreaMixin):
    """
    Класс куб.

    Хранит свою поверхность в виде списка квадратов
    """
    def __init__(self, side: int) -> None:
        super().__init__(side)
        self._2d_data = [Square(side) for _ in range(6)]


class Pyramid(Triangle, AreaMixin):
    """
    Класс пирамидка

    Хранит свою поверхность в виде треугольников и квадрата.
    """
    def __init__(self, base: int, height: int) -> None:
        super().__init__(base, height)
        self._2d_data = [Triangle(base=base, height=height) if index < 4 else Square(side=base) for index in range(5)]


def main():
    # Куб возьмем со стороной 10
    side = 10

    # Основание пирамидки 4, высота 6
    base = 4
    height = 6

    my_cube = Cube(side=side)
    print('Площадь поверхности куба со стороной {side} == {area}'.format(
        side=10,
        area=my_cube.area()
    ))

    my_pyramid = Pyramid(base=4, height=6)
    print('Площадь поверхности пирамидки с основанием {base} и высотой {height} == {area}'.format(
        base=base,
        height=height,
        area=my_pyramid.area()
    ))


main()
