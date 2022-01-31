class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    __total_salary = 0

    def salary_calculate(self):
        pass

    def get_total_salary(self):
        return self.__total_salary

    @staticmethod
    def add_total_salary(value):
        Employee.__total_salary += value


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__salary = 13000
        self.add_total_salary(self.__salary)

    def get_salary(self):
        return self.__salary


class Agent(Employee):
    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.__volume_of_sales = volume_of_sales
        self.__salary = 5000
        self.add_total_salary(self.get_salary())

    def get_salary(self):
        if self.__volume_of_sales:
            return self.__salary + self.__volume_of_sales * 0.05
        else:
            return self.__salary


class Worker(Employee):
    def __init__(self, name, surname, age, worked_hours):
        super().__init__(name, surname, age)
        self.__salary = 100
        self.__worked_hours = worked_hours
        self.add_total_salary(self.get_salary())

    def get_salary(self):
        return self.__salary * self.__worked_hours


def main():

    some_employee = Manager('Вадим', 'Сидоров', 35)
    Manager('Василий', 'Буслаев', 55)
    Manager('Антон', 'Духов', 40)

    Agent('Наум','Астафьев', 25, 1000)
    Agent('Полина', 'Телецкая', 23, 2500)
    Agent('Домна', 'Лазурная', 90, 0)

    Worker('Евлампий', 'Пароходов', 45, 1)
    Worker('Макар', 'Паровозов', 55, 10)
    Worker('Иосиф', 'Лошадинный', 97, 22)

    print('Величина заработной платы всех 9 служащих: {salary_all}'.format(
        salary_all=some_employee.get_total_salary()
    ))


main()
