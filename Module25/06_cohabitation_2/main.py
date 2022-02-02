import random


def show_info(*args):
    for i_arg in args:
        i_arg.info()


def live_the_day(husband, wife, child, cats, house, report):
    # wife_action = random.randint(1, 6)
    husband_action = random.randint(1, 4)
    cats_action = random.randint(1, 2)

    house.set_dirt_state(5)
    if house.get_dirt_state() > 90:
        husband.set_happiness(-10)
        wife.set_happiness(-10)
        child.set_happiness(-10)

    print('Что делали люди:')
    print('----------------')
    # жена
    if wife.get_alive():
        if wife.get_ate_state() < 25:
            wife.to_eat()
            report['Съедено еды:'] += 25
            print('{wife:<10}поела.'.format(wife=wife.get_name()))

        elif house.get_foods() < 65:
            wife.buy_food()
            print('{wife:<10}сходила в магазин за продуктами.'.format(wife=wife.get_name()))

        elif house.get_cat_foods() < 55:
            wife.buy_food_for_cat()
            print('{wife:<10}купила продукты для кота.'.format(wife=wife.get_name()))

        elif house.get_dirt_state() > 80:
            wife.clean_house(80)
            print('{wife:<10}сделала уборку.'.format(wife=wife.get_name()))

        elif house.get_money() > 300:
            wife.buy_fur_coat()
            report['Куплено шуб:'] += 1
            print('{wife:<10}купила шубу!'.format(wife=wife.get_name()))

        else:
            wife.pet_the_cat()
            print('{wife:<10}погладила кота.'.format(wife=wife.get_name()))

    # муж
    if husband.get_alive():
        if husband.get_ate_state() < 25:
            husband.to_eat()
            report['Съедено еды:'] += 25
            print('{husband:<10}поел.'.format(husband=husband.get_name()))

        elif house.get_money() < 50:
            husband.go_to_work()
            report['Заработано денег:'] += 150
            print('{husband:<10}сходил на работу.'.format(husband=husband.get_name()))

        elif husband_action in range(1, 3):
            husband.go_to_work()
            report['Заработано денег:'] += 150
            print('{husband:<10}сходил на работу. (random action)'.format(husband=husband.get_name()))

        elif husband_action in range(4, 5):
            husband.to_eat()
            report['Съедено еды:'] += 25
            print('{husband:<10}поел. (random action)'.format(husband=husband.get_name()))
        else:
            husband.play()
            print('{husband:<10}поиграл в компьютер.'.format(husband=husband.get_name()))

    # ребенок
    random_action = random.randint(1, 7)
    if child.get_alive():
        if child.get_happiness() < 30:
            child.sleep()
            print('{child:<10}поспал.'.format(child=child.get_name()))

        elif child.get_ate_state() < 20:
            child.to_eat()
            print('{child:<10}поел.'.format(child=child.get_name()))

        elif random_action == 1:
            child.cry()
            husband.set_happiness(-20)
            wife.set_happiness(-20)
            print('{child:<10}плакал.'.format(child=child.get_name()))
        elif random_action == 2:
            child.peed()
            husband.set_happiness(-20)
            wife.set_happiness(-20)
            print('{child:<10}испортил подгузник'.format(child=child.get_name()))
        else:
            child.play()
            wife.set_happiness(5)
            husband.set_happiness(5)
            print('{child:<10}поиграл'.format(child=child.get_name()))

    print()
    print('Что делали коты:')
    print('----------------')
    # коты
    for cat in cats:
        if cat.get_alive():
            if cat.get_eat_status() < 20:
                cat.to_eat()
                print('{cat:<10}поел.'.format(cat=cat.get_name()))

            elif cats_action == 1:
                cat.to_sleep()
                print('{cat:<10}поспал.'.format(cat=cat.get_name()))

            else:
                cat.scratch_wallpaper()
                print('{cat:<10}подрал обои.'.format(cat=cat.get_name()))

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
                self.death()

    def death(self):
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
        if self.__alive and self.__home[0].get_foods() > value:
            self.__home[0].set_foods(-value)
            self.__ate_state += value

    def pet_the_cat(self):
        if self.__alive:
            self.__happiness += 5
            self.__ate_state -= 10

    def get_alive(self):
        return self.__alive

    def info(self):
        print('{name:<10}'.format(name = self.__name), end = '')
        if self.__alive:
            print('Степень сытности: {ate_state}, Степень счастья: {happiness}'.format(
                ate_state=self.__ate_state,
                happiness=self.__happiness
            ))

        else:
            print('умер')


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
        if self.get_alive():
            self.set_happiness(-5)
            self.set_ate_state(-5)

    def peed(self):
        if self.get_alive():
            self.set_happiness(-5)
            self.set_ate_state(-5)

    def sleep(self):
        if self.get_alive():
            self.set_happiness(10)
            self.set_ate_state(-5)

    def to_eat(self, value=10):
        if self.get_alive():
            super(Child, self).to_eat(value)

    def play(self):
        if self.get_alive():
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

    def get_alive(self):
        return self.__alive

    def get_name(self):
        return self.__name

    def add_home(self, home):
        self.__home.append(home)

    def to_eat(self, value=10):
        if self.__alive:
            if self.__home[0].get_cat_foods() >= value:
                self.__eat_status += value * 2
                self.__home[0].set_cat_foods(-value)

            else:
                self.death()

            if self.__eat_status < 0:
                self.death()

    def death(self):
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
        print('{name:<10}'.format(name=self.__name), end='')
        if self.__alive:
            print('Степень сытности: {eat_state}'.format(
                name=self.__name,
                eat_state=self.__eat_status
            ))

        else:
            print('умер')


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
        if self.__money_in_nightstand < 0:
            self.__money_in_nightstand = 0

    def info(self):
        print('\n{home:<10}Деньги: {money}, Еда: {food}, Кошачья еда: {pet_food}, '
              'Грязь: {dust_level}'.format(
                    home='Дом',
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

    husband = Husband('Муж')
    husband.add_home(house)

    wife = Wife('Жена')
    wife.add_home(house)

    child = Child('Ребенок')
    child.add_home(house)

    cats = list()

    cat = Cat('Гав')
    cat.add_home(house)
    cats.append(cat)

    cat2 = Cat('Том')
    cat2.add_home(house)
    cats.append(cat2)

    cat3 = Cat('Пух')
    cat3.add_home(house)
    cats.append(cat3)

    for day in range(1, days + 1):
        print('=' * 59)
        print('День {}\n'.format(day))
        live_the_day(husband, wife, child, cats, house, life_report)

        print('Информационный блок:')
        print('-' * 20)
        show_info(wife, husband, child)
        print()
        show_info(cat, cat2, cat3, house)

    print('\nИтого зa {days} дней:'.format(days=days))

    for key, value in life_report.items():
        print('{key:<17} {value:>6}'.format(
            key=key,
            value=value
        ))


main()
