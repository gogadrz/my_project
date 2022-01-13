countries = []
country_cnt = int(input('Кол-во стран: '))

for i_country in range(1, country_cnt + 1):
    print('{0} страна: '.format(i_country), end='')
    cmd_str = input().split()

    country = {cmd_str[0]: [city for city in cmd_str[1:]]}
    countries.append(country)

for i_search in range(1, 4):
    print('\n{0} город: '.format(i_search), end='')
    city_name = input()

    found = False

    for i_countries in range(len(countries)):
        for city in countries[i_countries].keys():
            if city_name in countries[i_countries][city]:
                city_str = str(countries[i_countries].keys())[12:-3]
                print('Город {0} расположен в стране {1}.'.format(city_name, city_str))
                found = True

    if not found:
        print('По городу {0} данных нет.'.format(city_name))
