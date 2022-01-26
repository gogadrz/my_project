class Water:
    def __init__(self, name='Вода'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earch):
            return Dirt()
        else:
            return Error()


class Air:
    def __init__(self, name='Воздух'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earch):
            return Dust()
        else:
            return Error()


class Fire:
    def __init__(self, name='Огонь'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Earch):
            return Lava()
        else:
            return Error()


class Storm:
    def __init__(self, name='Шторм'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Steam:
    def __init__(self, name='Пар'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Dirt:
    def __init__(self, name='Грязь'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Earch:
    def __init__(self, name='Земля'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Lightning:
    def __init__(self, name='Молния'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Dust:
    def __init__(self, name='Пыль'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Lava:
    def __init__(self, name='Лава'):
        self.name = name

    def answer(self):
        print('сложили два класса и вывели {}'.format(self.name))


class Error:
    def __init__(self, name='Ошибка'):
        self.name = name

    def answer(self):
        print('Эти классы не складываются')
