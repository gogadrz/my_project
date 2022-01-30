# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель,
# и каждый может сделать два действия: сообщить свою модель и идти по воде.
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля.
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
# Реализуйте классы грузового и военного кораблей.
# Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование.
# Не забудьте про функцию super в дочерних классах.

class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'Модель корабля {self.__model}'

    def run(self):
        print('Корабль {model} поплыл.'.format(model=self.__model))


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.__tonnage = 0

    def load(self):
        self.__tonnage += 1
        print('load, tonnage = {}'.format(self.__tonnage))

    def put_off(self):
        self.__tonnage -= 1
        print('put off, tonnage = {}'.format(self.__tonnage))

    def to_run(self):
        super(CargoShip, self).run()


class WarShip(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon

    def run(self):
        super(WarShip, self).run()

    def attack(self):
        print('корабль {} стреляет из {}'.format(super.__name__, self.__weapon))

cargo = CargoShip('titanic')
print(cargo)
cargo.to_run()
cargo.load()
cargo.put_off()

war = WarShip('avrora', 'rogatka')
print(war)
war.run()
war.attack()
