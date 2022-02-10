import datetime


class Date:
    """
    Класс Date
    """

    def __init__(self, date_str: str) -> None:
        date = self.from_string(date_str)
        self.__f_date = datetime.date(date.year, date.month, date.day)

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        try:
            datetime.datetime.strptime(date_str, '%d-%m-%Y')

        except ValueError:
            return False

        return True

    @classmethod
    def from_string(cls, date_str: str) -> datetime.date:
        return datetime.datetime.strptime(date_str, '%d-%m-%Y')

    def __str__(self) -> str:
        return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(
            day=self.__f_date.day,
            month=self.__f_date.month,
            year=self.__f_date.year
        )


def main():
    # Александр. Подскажите пожалуйста.
    # Я никак не могу сделать что бы сработала
    # строка из примера:
    #     date = Date.from_string('10-12-2077')
    # У меня работает вариант вызова конструктора,
    # а из него вызывается метод from_string.
    # Я не понимаю эту конструкцию, вызов метода без вызова конструктора...

    # Во 2-ой задаче, с математическим модулем у меня возникла
    # такая же проблема. Пришлось использовать @classmethod.

    # date = Date.from_string('10-12-2077')
    date = Date('10-12-2077')
    print(date)
    print(Date.is_date_valid('10-12-2077'))
    print(Date.is_date_valid('40-12-2077'))


main()
