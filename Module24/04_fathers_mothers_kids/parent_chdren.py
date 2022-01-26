class Parent:
    def __init__(self, name, age, children = None):
        self.name = name
        self.age = age
        self.children = children or list()

        for i_child in self.children:
            if i_child.age > self.age - 16:
                print('\nРазница в возрасте родителя и ребенка должна быть не меньше 16 лет!')
                print('{} не может быть родителем {}.\n'.format(
                    self.name,
                    i_child.name))

                self.children.remove(i_child)

    def soothe_the_child(self, name):
        for child_name in self.children:
            if child_name.name == name:
                child_name.crying = 0

    def feed_the_baby(self, name):
        for child_name in self.children:
            if child_name.name == name:
                child_name.hungry = 0

    def show_info(self):
        print('Имя родителя: {}\nВозраст: {}'.format(
            self.name,
            self.age))

        print('Дети:', len(self.children))
        if self.children:
            for i_child in self.children:
                i_child.show_info()


class Child:
    hungry_states = {0: 'Сыт', 1: 'Голоден'}
    states = {0: 'Спокоен', 1: 'Плачет'}

    def __init__(self, name, age, crying = 0, hungry = 0):
        self.name = name
        self.age = age
        self.crying = crying
        self.hungry = hungry

    def show_info(self):
        print('\tИмя ребенка: {}\n\tВозраст: {}\n\tСостояние спокойствия: {}\n\tСостояние голода: {}\n'.format(
            self.name,
            self.age,
            self.states[self.crying],
            self.hungry_states[self.hungry]
        ))
