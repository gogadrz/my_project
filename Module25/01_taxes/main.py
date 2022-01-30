class Property:
    def __init__(self, worth):
        self.__worth = worth

    def calculate_tax(self):
        pass

    def get_worth(self):
        return self.__worth


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        return 'Квартира. Стоимость {worth} рублей'.format(
            worth=self.get_worth()
        )

    def calculate_tax(self):
        return self.get_worth() / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.get_worth() / 200

    def __str__(self):
        return 'Машина. Стоимость {worth} рублей'.format(
            worth=self.get_worth()
        )


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.get_worth() / 500

    def __str__(self):
        return 'Дача. Стоимость {worth} рублей'.format(
            worth=self.get_worth()
        )


def main():
    money_box = int(input('Сколько у Вас всего денег? '))
    apartment_price = int(input('Сколько стоит Ваша квартира? '))
    car_price = int(input('Сколько стоит Ваша машина? '))
    country_house_price = int(input('Сколько стоит Ваша дача? '))

    your_apartment = Apartment(apartment_price)
    your_car = Car(car_price)
    your_country_house = CountryHouse(country_house_price)

    tax_sum = your_apartment.calculate_tax() + your_car.calculate_tax() + \
              your_country_house.calculate_tax()

    print()

    print('Налог на квартиру составляет: {tax}'.format(
        tax=your_apartment.calculate_tax()
    ))

    print('Налог на машину составляет:   {tax}'.format(
        tax=your_car.calculate_tax()
    ))

    print('Налог на дачу составляет:     {tax}'.format(
        tax=your_country_house.calculate_tax()
    ))

    print('\nДля уплаты всех налогов понадобится {summ} рублей.'.format(
        summ=tax_sum
    ))

    money_box -= tax_sum
    if money_box < 0:
        print('Вам не хватает {summ} рублей.'.format(
            summ=-money_box
        ))


main()
