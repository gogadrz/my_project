import math
from typing import Union


class MyMath:
    """
    Класс вычисляющий:
    - длину окружности
    - площадь окружности
    - объём куба
    - площадь поверхности сферы
    """

    __result = 0

    @classmethod
    def circle_len(cls, radius: Union[int, float]) -> Union[int, float]:
        cls.__result = 2 * math.pi * radius
        return cls.__result

    @classmethod
    def circle_sq(cls, radius: Union[int, float]) -> Union[int, float]:
        cls.__result = math.pi * radius ** 2
        return cls.__result

    @classmethod
    def cube_vol(cls, radius: Union[int, float]) -> Union[int, float]:
        cls.__result = radius ** 3
        return cls.__result

    @classmethod
    def sphere_area(cls, radius: Union[int, float]) -> Union[int, float]:
        cls.__result = 4 * math.pi * radius ** 2
        return cls.__result


def main():

    res_1 = MyMath.circle_len(radius=5)
    res_2 = MyMath.circle_sq(radius=6)
    print(res_1)
    print(res_2)


main()
