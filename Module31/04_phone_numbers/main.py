import re


def check_phone_number(number: str) -> bool:
    if re.search(r'[89]\d{9}', number):
        return True
    else:
        return False


def main() -> None:

    phone_numbers_list: list[str] = ['9999999999',
                                     '999999-999',
                                     '99999x9999',
                                     '8567467563',
                                     '9-234-2345',
                                     'd-082364293',
                                     '8123456789'
                                     ]

    for index, number in enumerate(phone_numbers_list):
        print('{index} номер: '.format(index=index + 1), end='')

        if check_phone_number(number):
            print('всё в порядке')
        else:
            print('не подходит')


if __name__ == '__main__':
    main()
