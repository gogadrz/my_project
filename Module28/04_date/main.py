import datetime


class Date:
    """
    Класс Date
    """

    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        try:
            datetime.datetime.strptime(date_str, '%d-%m-%Y')

        except ValueError:
            return False

        return True

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        result = datetime.datetime.strptime(date_str, '%d-%m-%Y')
        return Date(result.day, result.month, result.year)

    def __str__(self) -> str:
        return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(
            day=self.__day,
            month=self.__month,
            year=self.__year
        )


def main():

    date = Date.from_string('10-12-2077')
    # date = Date(10, 12, 2077)
    print(date)
    print(Date.is_date_valid('10-12-2077'))
    print(Date.is_date_valid('40-12-2077'))


main()
