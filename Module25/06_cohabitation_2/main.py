class People:
    def __init__(self, name):
        self.__name = name
        self.__ate_state = 30
        self.__happiness = 100
        self.home = []

    def add_home(self, home):
        self.home.append(home)

    def get_money_in_nightstand(self):
        return self.home[0].get_money_in_nightstand(self)

    def to_eat(self):
        # if
        pass

    def pet_the_cat(self):
        self.__happiness += 5


class Husband(People):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        pass

    def go_to_work(self):
        pass


class Wife(People):
    def __init__(self, name):
        super().__init__(name)

    def buy_food(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


class Cat:
    def __init__(self, name):
        self.__name = name
        self.__eat_status = 30

    def to_eat(self):
        pass

    def to_sleep(self):
        pass

    def scratch_wallpaper(self):
        pass


class House:
    def __init__(self):
        self.__money_in_nightstand = 100
        self.__foods_in_cool_box = 50
        self.__cat_food = 30
        self.__dirt_state = 0

    def get_money_in_nightstand(self):
        return self.__money_in_nightstand

    def add_money_in_nightstand(self, value):
        self.__money_in_nightstand += value

    def get_foods_in_cool_box(self):
        return self.__foods_in_cool_box

    def add_foods_in_cool_box(self, value):
        self.__foods_in_cool_box += value

    def get_cat_food(self):
        return self.__cat_food

    def add_cat_food(self, value):
        self.__cat_food += value

    def get_dirt_state(self):
        return self.__dirt_state

    def add_dirt_state(self, value):
        self.__dirt_state += value


# husband = Husband('Karl')
# wife = Wife('Klara')
# cat = Cat('Garfield')
husband = Husband('Karl')
house = House()
husband.add_home(house)

pass
# print(husband.get_money_in_nightstand())

