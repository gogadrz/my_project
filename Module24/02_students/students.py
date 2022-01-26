import random


class Student:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.group_num = random.randint(1, 5)
        self.scores = []
        for _ in range(5):
            self.scores.append(random.randint(3, 5))
        self.GPA = sum(self.scores) / len(self.scores)

    def show_info(self, print_gpa=False):
        print('Студент: {:20} группа №: {} успеваемость: '.format(
            self.name,
            self.group_num
        ), end='')

        for index, score in enumerate(self.scores):
            print(score, end = '')

            if index < len(self.scores) - 1:
                print(',', end='')
            print(' ', end='')

        if print_gpa:
            print(' средний балл: {}'.format(self.GPA), end='')

        print()
