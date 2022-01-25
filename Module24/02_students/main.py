import random


class Student:

    def __init__(self, name):
        self.name = name
        self.group_num = random.randint(1, 20)
        self.scores = []
        for _ in range(5):
            self.scores.append(random.randint(3, 5))

    def show_info(self):
        print('ФИ: {}, группа №: {}, успеваемость: {}'.format(self.name, self.group_num, self.scores))
        print('{}'.format(sum(self.scores) / len(self.scores)))


try:
    with open('students.txt', 'r', encoding = 'utf-8') as in_file:
        name_str = in_file.readline()
except FileNotFoundError:
    print('Файл {} не найден.'.format('students.txt'))

unit01 = Student(name_str.strip())
unit01.show_info()
