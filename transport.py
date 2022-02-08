from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color, speed):
        self.__color = color
        self.__speed = speed

    @abstractmethod
    def move(self):
        print('abs_moving')

    def signal(self):
        print('bi-bi')


class AudioMixin:
    def play_music(self):
        print('Музыка орет - спасу нет!')

    def stop_music(self):
        print('Музыка выключена. Наконец то, тишина.')


class Auto(Transport):
    def __init__(self, model, color, speed):
        super().__init__(color, speed)
        self.__model = model

    def move(self):
        print('Автомобиль {model} движется'.format(model=self.__model))



class Boat(Transport):
    def move(self):
        print('Катер поплыл!')


class Amphibian(Transport, AudioMixin):
    def move(self):
        print('Амфибия и плывет и едет!')


runx = Auto('Toyota', 'Gray', 160)
runx.move()
runx.signal()
solar = Boat('Gray', 40)
solar.move()
solar.signal()
brdm = Amphibian('Green', 15)
brdm.move()
brdm.play_music()
brdm.stop_music()




















# У нас есть парк транспорта.
# У каждого транспорта есть цвет и скорость,
# и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
#
#     Автомобили. Они могут ездить только по земле.
#     Лодки. Ездят только по воде.
#     Амфибии. Могут перемещаться и по земле, и по воде.
#
# Напишите код, который реализует соответствующие классы и методы.
# Класс «Транспорт» должен быть абстрактным
# и содержать абстрактные методы.
#
# Также добавьте класс-примесь,
# в котором реализован функционал проигрывания музыки.
# «Замешайте» этот класс в «Амфибию»
#
