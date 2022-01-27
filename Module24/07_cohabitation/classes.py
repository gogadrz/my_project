class Icebox:
    def __init__(self, foods=50):
        self.foods = foods

    def foods_is_left(self):
        return self.foods

    def add_remove_foods(self, num):
        self.foods += num


class Nightstand:
    def __init__(self, money=0):
        self.money = money

    def money_is_left(self):
        return self.money

    def add_sub_money(self, num):
        self.money += num


class Home:
    def __init__(self, name='Коттедж'):
        self.name = name
        self.n_stand = Nightstand()
        self.i_box = Icebox()

    def left_money(self):
        return self.n_stand.money_is_left()

    def add_money(self, num):
        self.n_stand.add_sub_money(num)

    def left_foods(self):
        return self.i_box.foods_is_left()

    def add_foods(self, num):
        self.i_box.add_remove_foods(num)

    def home_info(self):
        print('Foods: {}'.format(self.left_foods()))
        print('Money: {}'.format(self.left_money()))


class People:
    delta = 10
    live_status = {
        0: 'Прислонился к березе и дал дуба.',
        1: 'Живее всех живых'
                   }

    def __init__(self, name, ate_state=50, live=True):
        self.name = name
        self.ate_state = ate_state
        self.live = live
        self.home = []

    def add_house(self, house):
        self.home.append(house)

    def to_eat(self):
        self.ate_state += self.delta
        self.home[0].add_foods(-self.delta)

    def to_work(self):
        self.ate_state -= self.delta
        if self.ate_state < 0:
            self.live = False
        self.home[0].add_money(self.delta)

    def to_play(self):
        self.ate_state -= self.delta
        if self.ate_state < 0:
            self.live = False

    def to_go_to_shop(self):
        self.home[0].add_foods(self.delta)
        self.home[0].add_money(-self.delta)

    def info(self):
        print("Имя: {}\nСытность: {}".format(
            self.name,
            self.ate_state
        ))
        self.home[0].home_info()
        print(self.live_status[self.live])

    def is_live(self):
        return self.live

    def what_is_to_eat(self):
        return self.ate_state

    def how_much_foods(self):
        return self.home[0].left_foods()

    def how_much_money(self):
        return self.home[0].left_money()
