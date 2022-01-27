import random
from classes import Home, People


def throw_cube():
    return random.randint(1, 6)


my_house = Home()
man = People('Артем')
women = People('Аглафея')

man.add_house(my_house)
women.add_house(my_house)

family = list()
family.append(man)
family.append(women)

day = 0

while day < 365 and man.live:
    day += 1
    print('\n--- День {}-й ---\n'.format(day))

    whats_next = throw_cube()

    for family_member in family:

        if family_member.what_is_to_eat() < 20:
            family_member.to_eat()
            print('{} - нужно поесть'.format(
                family_member.name
            ))

        elif family_member.how_much_foods() < 10 * len(family):
            family_member.to_go_to_shop()
            print('{} - нужно сходить в магазин'.format(
                family_member.name
            ))

        elif family_member.how_much_money() < 50:
            family_member.to_work()
            print('{} - нужно работать'.format(
                family_member.name
            ))

        elif whats_next == 1:
            family_member.to_work()
            print('{} - кубик послал работать'.format(
                family_member.name
            ))

        elif whats_next == 2:
            family_member.to_eat()
            print('{} - кубик послал поесть'.format(
                family_member.name
            ))

        else:
            family_member.to_play()
            print('{} - кубик разрешил поиграть'.format(
                family_member.name
            ))

        # print('live: ', family_member.is_live())
        # print()
        family_member.info()
        print()
