import random
from warrior import Warrior


def who_is_hit():
    i_hit = random.randint(1, 2)
    i_offended = 3 - i_hit
    return i_hit, i_offended


unit_1 = Warrior('Брюс Ли')
unit_2 = Warrior('Джеки Чен')

warriors = (None, unit_1, unit_2)
hits = 0
winner = ''
loser = ''

while True:
    hits += 1

    # Камень, ножницы бумага.
    # Кто будет бить, а кто терпеть?
    hit_index, offended_index = who_is_hit()

    # Живы?
    if (not warriors[offended_index].is_alive()) or (not warriors[hit_index].is_alive()):
        winner = warriors[hit_index].get_name()
        loser = warriors[offended_index].get_name()
        break

    # Счастливчик, которому выпало бить.
    print('{} - удар. Бьёт: {}'.format(hits, warriors[hit_index].get_name()))

    # Получите, распишитесь...
    warriors[offended_index].got_hit()
    print('У {} осталось здоровья {} очков\n'.format(warriors[offended_index].get_name(),
                                                     warriors[offended_index].get_health()))

print('Победу одержал {}!\nЭх {}, надо было больше тренироваться...'.format(winner, loser))
