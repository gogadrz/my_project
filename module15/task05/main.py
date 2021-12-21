films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []


def search_film(film_name):
    for film in films:
        if film_name == film:
            return True
    return False


def print_film_list(film_list):
    for film in film_list:
        print(film, end='')
        if film != film_list[-1]:
            print(', ', end='')


films_count = int(input('Сколько фильмов хотите добавить? '))

for i in range(films_count):
    film_name = input('Введите название фильма: ')
    if not search_film(film_name):
        print('Ошибка: фильма', film_name, 'у нас нет :(')
    else:
        favorite_films.append(film_name)

print('Ваш список любимых фильмов: ', end='')
print_film_list(favorite_films)
