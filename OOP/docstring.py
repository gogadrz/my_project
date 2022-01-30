class CanFly:
    """
    Базовый класс описывает все что летает.

    __height: высота полета
    __speed: скорость полета

    Args:
        height (int) можно задать высоту полета
        speed (int) можно задать скорость полета

    Attributes
        нет
    """
    def __init__(self, height=0, speed=0):
        self.__height = height
        self.__speed = speed

    def __str__(self):
        return 'Speed = {speed}, Height = {height}'.format(
            speed=self.__speed,
            height=self.__height
        )

    def take_off(self):
        pass

    def landing(self):
        self.__height = 0
        self.__speed = 0

    def get_speed(self):
        """
        Геттер для установки скорости

        :return: __speed
        :rtype: int
        """
        return self.__speed

    def get_height(self):
        return self.__height

    def set_speed(self, speed):
        """
        Сеттер для установки скорости

        :param speed скорость
        :type speed int

        :raise Exception если скорость вне диапазона 0..180 (это для примера исключения здесь нет)
        """
        self.__speed = speed

    def set_height(self, height):
        self.__height = height


class Butterfly(CanFly):
    """
    Класс бабочка, родитель CanFly
    дальше так же как и в родителе
    """
    def __init__(self, height=1, speed=.5):
        super(Butterfly, self).__init__(height=height, speed=speed)

    def __str__(self):
        return 'Butterfly, h={}, s={}'.format(
            self.get_height(),
            self.get_speed()
        )


class Rocket(CanFly):
    def __init__(self, height=500, speed=1000):
        super().__init__(height, speed)

    def __str__(self):
        return 'Rocket, h={height}, s={speed}'.format(
            speed=self.get_speed(),
            height=self.get_height()
        )


b = Butterfly()
print(b)
b.landing()
print(b)


r = Rocket()
print(r)
r.landing()
print(r)

print()
print(CanFly.__doc__)
print(Butterfly.__doc__)
