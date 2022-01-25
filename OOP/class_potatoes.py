class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    def print_state(self):
        print('Картошка {} в стадии {}'.format(self.index, Potato.states[self.state]))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает...')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Вся картошка созрела.')
        else:
            print('Картошка еще не созрела')


my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
my_garden.grow_all()
my_garden.are_all_ripe()
my_garden.grow_all()
my_garden.are_all_ripe()
my_garden.grow_all()
my_garden.are_all_ripe()