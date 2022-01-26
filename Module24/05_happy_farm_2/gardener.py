from garden import PotatoGarden


class Gardener:
    def __init__(self, name, garden_line = None):
        self.name = name
        self.garden_line = garden_line or PotatoGarden(garden_line)
        print('Садовник {} посадил в свою грядку {} картошин.'.format(self.name, self.garden_line.potatoes_count()))

    def service_garden_line(self):
        self.garden_line.grow_all()

    def show_info(self):
        if self.garden_line.are_all_ripe():
            return True
        else:
            return False

    def harvest_all_potatoes(self):
        print('Садовник собрал урожай.')
        self.garden_line.harvest_potatoes()
