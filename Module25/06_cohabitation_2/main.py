import random


def show_info(*args):
    for i_arg in args:
        i_arg.info()


def live_the_day(husband, wife, child, cats, house, report):
    random_action = random.randint(1, 6)

    house.set_dirt_state(5)
    if house.get_dirt_state() > 90:
        husband.set_happiness(-10)
        wife.set_happiness(-10)
        child.set_happiness(-10)

    print('Что делали люди:')
    # жена
    if wife.get_ate_state() < 20:
        wife.to_eat()
        report['Съедено еды:'] += 25
        print('{}\tпоела.'.format(wife.get_name()))

    elif house.get_foods() < 50:
        wife.buy_food()
        print('{}\tсходила в магазин за продуктами.'.format(wife.get_name()))

    elif house.get_cat_foods() < 20:
        wife.buy_food_for_cat()
        print('{}\tкупила продукты для кота.'.format(wife.get_name()))

    elif house.get_dirt_state() > 80:
        wife.clean_house(80)
        print('{}\tсделала уборку.'.format(wife.get_name()))

    elif house.get_money() > 300:
        wife.buy_fur_coat()
        report['Куплено шуб:'] += 1
        print('{}\tкупила шубу!'.format(wife.get_name()))

    else:
        wife.pet_the_cat()
        print('{}\tпогладила кота.'.format(wife.get_name()))

    # муж
    if husband.get_ate_state() < 20:
        husband.to_eat()
        report['Съедено еды:'] += 25
        print('{}\tпоел.'.format(husband.get_name()))

    elif house.get_money() < 50:
        husband.go_to_work()
        report['Заработано денег:'] += 150
        print('{}\tсходил на работу.'.format(husband.get_name()))

    elif random_action == 1 or random_action == 2:
        husband.go_to_work()
        report['Заработано денег:'] += 150
        print('{}\tсходил на работу. (random action)'.format(husband.get_name()))

    elif random_action == 3 or random_action == 4:
        husband.to_eat()
        report['Съедено еды:'] += 25
        print('{}\tпоел. (random action)'.format(husband.get_name()))
    else:
        husband.play()
        print('{}\tпоиграл в компьютер.'.format(husband.get_name()))

    # ребенок
    random_action = random.randint(1, 6)
    if child.get_happiness() < 30:
        child.sleep()
        print('{}\tпоспал.'.format(child.get_name()))

    elif child.get_ate_state() < 20:
        child.to_eat()
        print('{}\tпокормили.'.format(child.get_name()))

    elif random_action == 1:
        child.cry()
        husband.set_happiness(-20)
        wife.set_happiness(-20)
        print('{}\tплакал.'.format(child.get_name()))
    elif random_action == 2:
        child.peed()
        husband.set_happiness(-20)
        wife.set_happiness(-20)
        print('{}\tиспортил подгузник'.format(child.get_name()))
    else:
        child.play()
        print('{}\tпоиграл'.format(child.get_name()))

    print()
    print('Что делали коты:')
    # коты
    for cat in cats:
        if cat.get_eat_status() < 10:
            cat.to_eat()
            print('{}\tпоел.'.format(cat.get_name()))

        elif random.randint(1, 2) == 1:
            cat.to_sleep()
            print('{}\tпоспал.'.format(cat.get_name()))

        else:
            cat.scratch_wallpaper()
            print('{}\tподрал обои.'.format(cat.get_name()))

    print()


class People:
    def __init__(self, name):
        self.__name = name
        self.__ate_state = 30
        self.__happiness = 100
        self.__home = []
        self.__alive = True

    def get_ate_state(self):
        return self.__ate_state

    def set_ate_state(self, value):
        if self.__alive:
            self.__ate_state += value
            if self.__ate_state < 0:
                self.__alive = False
                self.__ate_state = 0
                self.__happiness = 0
                self.__home.clear()

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, value):
        if self.__alive:
            self.__happiness += value
            if self.__happiness < 10:
                self.__alive = False
                self.__ate_state = 0
                self.__happiness = 0
                self.__home.clear()

    def get_home(self):
        if self.__alive:
            return self.__home[0]

    def get_name(self):
        return self.__name

    def add_home(self, home):
        self.__home.append(home)

    def to_eat(self, value=25):
        if self.__alive:
            self.__home[0].set_foods(-value)
            self.__ate_state += value

    def pet_the_cat(self):
        if self.__alive:
            self.__happiness += 5
            self.__ate_state -= 10

    def get_alive(self):
        return self.__alive

    def info(self):
        print('{name}\t'.format(name = self.__name), end = '')
        if self.__alive:
            print('Степень сытности: {ate_state}, Степень счастья: {happiness}'.format(
                        ate_state=self.__ate_state,
                        happiness=self.__happiness
            ))

            # if self.__alive:
            #     print('Жизненный статус: жив')
            # else:
            #     print('Жизненный статус: умер')
        else:
            print('- ' * 5, 'умер')


class Husband(People):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        if self.get_alive():
            self.set_happiness(20)
            self.set_ate_state(-10)

    def go_to_work(self):
        if self.get_alive():
            self.get_home().set_money(150)
            self.set_ate_state(-10)


class Child(People):
    def __init__(self, name):
        super().__init__(name)

    def cry(self):
        self.set_happiness(-5)
        self.set_ate_state(-5)

    def peed(self):
        self.set_happiness(-5)
        self.set_ate_state(-5)

    def sleep(self):
        self.set_happiness(10)

    def to_eat(self, value=10):
        super(Child, self).to_eat(value)

    def play(self):
        self.set_happiness(10)
        self.set_ate_state(-5)


class Wife(People):
    def __init__(self, name):
        super().__init__(name)

    def buy_food(self):
        if self.get_alive():
            self.get_home().set_foods(60)
            self.get_home().set_money(-60)
            self.set_ate_state(-10)

    def buy_food_for_cat(self):
        if self.get_alive():
            self.get_home().set_cat_foods(60)
            self.get_home().set_money(-60)
            self.set_ate_state(-10)

    def buy_fur_coat(self):
        if self.get_alive():
            self.get_home().set_money(-350)
            self.set_happiness(60)
            self.set_ate_state(-10)

    def clean_house(self, value=50):
        if self.get_alive():
            self.get_home().set_dirt_state(-value)
            self.set_ate_state(-10)


class Cat:
    def __init__(self, name):
        self.__name = name
        self.__eat_status = 30
        self.__home = []
        self.__alive = True

    def get_eat_status(self):
        return self.__eat_status

    def get_name(self):
        return self.__name

    def add_home(self, home):
        self.__home.append(home)

    def to_eat(self, value=10):
        if self.__alive:
            self.__eat_status += value * 2
            self.__home[0].set_cat_foods(-value)
            if self.__eat_status < 0:
                self.__alive = False
                self.__eat_status = 0
                self.__home.clear()

    def to_sleep(self):
        if self.__alive:
            self.__eat_status -= 10

    def scratch_wallpaper(self):
        if self.__alive:
            self.__home[0].set_dirt_state(5)
            self.__eat_status -= 10

    def info(self):
        print('{name}\t'.format(name = self.__name), end = '')
        if self.__alive:
            print('Степень сытности: {eat_state}'.format(
                        name=self.__name,
                        eat_state=self.__eat_status
            ))
            # if self.__alive:
            #     print('Жизненный статус: Жив.')
            # else:
            #     print('Жизненный статус: Умер.')
        else:
            print('- ' * 5, 'умер')


class House:
    def __init__(self):
        self.__money_in_nightstand = 100
        self.__foods_in_cool_box = 50
        self.__cat_food = 30
        self.__dirt_state = 0

    def get_dirt_state(self):
        return self.__dirt_state

    def set_dirt_state(self, value):
        self.__dirt_state += value

    def set_cat_foods(self, value):
        self.__cat_food += value

    def get_cat_foods(self):
        return self.__cat_food

    def set_foods(self, value):
        self.__foods_in_cool_box += value

    def get_foods(self):
        return self.__foods_in_cool_box

    def get_money(self):
        return self.__money_in_nightstand

    def set_money(self, value):
        self.__money_in_nightstand += value

    def info(self):
        print('\nДеньги в тумбочке: {money}, Еда в холодильнике: {food}, Кошачья еда: {pet_food}, '
              'Количество грязи: {dust_level}'.format(
                    money=self.__money_in_nightstand,
                    food=self.__foods_in_cool_box,
                    pet_food=self.__cat_food,
                    dust_level=self.__dirt_state
        ))


def main():
    life_report = {
        'Заработано денег:': 0,
        'Съедено еды:': 0,
        'Куплено шуб:': 0
    }

    days = 365
    house = House()

    husband = Husband('Karl')
    husband.add_home(house)

    wife = Wife('Klara')
    wife.add_home(house)

    child = Child('vitalik')
    child.add_home(house)

    cats = list()

    cat = Cat('Garfield')
    cat.add_home(house)
    cats.append(cat)

    cat2 = Cat('Matvey')
    cat2.add_home(house)
    cats.append(cat2)

    cat3 = Cat('Tom')
    cat3.add_home(house)
    cats.append(cat3)

    for day in range(1, days + 1):
        print('-' * 50)
        print('День {}\n'.format(day))
        live_the_day(husband, wife, child, cats, house, life_report)

        show_info(wife, husband, child)
        print()
        show_info(cat, cat2, cat3, house)

    print('\nИтого зa {} дней:'.format(days))

    for key, value in life_report.items():
        print('{key} {value}'.format(key=key, value=value))


main()
