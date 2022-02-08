class Robot:
    def __init__(self, model):
        self.__model = model

    def say(self):
        print('Я робот {}!'.format(self.__model))


class CanFly:
    def __init__(self, height, speed):
        self.__height = height
        self.__speed = speed

    def take_off(self):
        self.__height = 50
        print('Взлетаю')

    def fly(self):
        self.__speed = 160
        print('Лечу')

    def landing(self):
        self.__height = 0
        self.__speed = 0
        print('Приземляюсь')


class ReconnaissanceDrone(Robot, CanFly):
    def operate(self):
        self.fly()
        print('Веду разведку с воздуха')

    def say(self):
        super(ReconnaissanceDrone, self).say()
        print('sdf')


class WarDrone(Robot, CanFly):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon

    def operate(self):
        print('Защищаю объект с воздуха, с помощью {}'.format(self.__weapon))


def main():
    rob = ReconnaissanceDrone('Putin')
    rob.say()
    rob.take_off()
    rob.operate()
    rob2 = WarDrone('Medvedev', 'rogatka')
    rob2.say()
    rob2.landing()
    rob2.operate()


main()
