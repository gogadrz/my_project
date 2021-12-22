films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
favorite_films = []

def film_in_list(film_name, film_list):
    for i_film in film_list:
        if i_film == film_name:
            return True
    return False

def add_film(film_name):
    if film_in_list(film_name, favorite_films) or not film_in_list(film_name, films):
        return False
    else:
        favorite_films.append(film_name)
        return True

def remove_film(film_name):
    if film_in_list(film_name, favorite_films):
        favorite_films.remove(film_name)
        return True
    else:
        return False

def insert_film(film_name):
    if film_in_list(film_name, favorite_films) or not film_in_list(film_name, films):
        return False
    else:
        position = int(input('В какую позицию вставить? '))
        favorite_films.insert(position - 1, film_name)
        return True

def print_error():
    print('Ошибка.\nФильм должен быть в базе фильмов и его не должно быть в Вашем топе.')
    print('Доступные команды: добавить, вставить, удалить, выход')

def menu():
    command = ''
    while command != 'выход':
        print('Ваш текущий топ фильмов:', favorite_films)
        film_name = input('Название фильма: ')
        print('Команды: добавить, вставить, удалить, выход')
        command = input('Введите команду: ')

        if command == 'добавить':
            if not add_film(film_name):
                print_error()
        elif command == 'удалить':
            if not remove_film(film_name):
                print_error()
        elif command == 'вставить':
            if not insert_film(film_name):
                print_error()



menu()