import random


class KillError(Exception):
    def __str__(self):
        return 'KillError Exception!'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError Exception!'


class CarCrushError(Exception):
    def __str__(self):
        return 'CarCrushError Exception!'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError Exception!'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError Exception!'


class LifeSimulator:

    def __init__(self):
        self.__karma = 0
        self.__ex_list = list()
        self.__ex_list.append(KillError())
        self.__ex_list.append(DrunkError())
        self.__ex_list.append(CarCrushError())
        self.__ex_list.append(GluttonyError())
        self.__ex_list.append(DepressionError())

    def one_day(self, day):

        if random.randint(1, 10) == 6:
            print('This day was written to the \'karma.log\' file.')

            try:
                raise (self.__ex_list[random.randint(0, 3)])

            except (KillError, DrunkError, CarCrushError, GluttonyError, DepressionError) as ex:
                str_to_file = 'Day {day}, {ex}\n'.format(
                    day=str(day),
                    ex=str(ex)
                )

                with open('karma.log', 'a') as except_file:
                    except_file.write(str_to_file)

        else:
            self.__karma += random.randint(1, 7)
            print('Карма = {}'.format(self.__karma))

    def get_karma(self):
        return self.__karma


def main():

    karma = 500
    day_index = 0

    person = LifeSimulator()

    while person.get_karma() < karma:

        day_index += 1
        print('День {index}, '.format(index=day_index), end='')
        person.one_day(day_index)

    print('\nОткрылась 7-я чакра. Просветленный. :)')


main()
