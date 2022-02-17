from typing import ClassVar
import re


def main() -> None:
    numbers_base: str = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    private_number: ClassVar = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', numbers_base)
    print('Список номеров частных автомобилей:', private_number)

    taxi_number: ClassVar = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', numbers_base)
    print('Список номеров такси:', taxi_number)


if __name__ == '__main__':
    main()
