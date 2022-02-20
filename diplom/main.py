import telebot
import os
from typing import ClassVar
from lowprice import lowprice
from highprice import highprice
from bestdeal import bestdeal
from history import history


def get_full_file_name(file_name: str) -> str:
    """
    Функция возвращает полный путь по имени файла

    :param file_name: имя файла
    :type file_name: str

    :return: полный путь к файлу
    :rtype: str
    """
    return os.path.abspath(os.path.join(os.path.curdir, file_name))


def get_token(file_name: str) -> str:
    """
    Функция возвращает токен бота.
    Токен хранится в текстовом файле 'token'.
    Если файл не существует, возвращается пустая строка.

    :param file_name: имя файла
    :type file_name: str

    :return: токен
    :rtype: str

    """
    full_file_name = get_full_file_name(file_name)

    if not os.path.exists(full_file_name):
        print('Файл {f_name} (содержащий токен) не найден.'.format(f_name=file_name))
        return ''

    with open(full_file_name, 'r') as file:
        return file.read()


def main(file_name: str) -> None:

    token: str = get_token(file_name)

    # Нет токена, нет смысла продолжать.
    if token == '':
        return

    bot: ClassVar = telebot.TeleBot(token, parse_mode=None)

    @bot.message_handler(commands=['hello-world'])
    def hello_world_message(message: ClassVar) -> None:
        """
        Функция-обработчик команды /hello-world
        Просто пишет приветствие со смайликом

        :param message: данные сообщения
        :type message: telebot.types.Message
        """
        answer_str = 'Привет {u_name} {smile}\nОтвет из команды /hello-world'.format(
            u_name=message.from_user.first_name,
            smile=U'\U0001F44C'
        )

        print(answer_str)
        bot.send_message(message.chat.id, answer_str)

    @bot.message_handler(commands=['help'])
    def help(message: ClassVar) -> None:
        """
        Функция-обработчик команды /help
        Выводит список доступных команд и краткое описание.

        :param message: данные сообщения
        :type message: telebot.types.Message
        """
        answer_str = "Здесь будет справка по командам.\n\n" \
                     "/hello-world - приветствие со смайликом\n" \
                     "/lowprice    - заглушка\n" \
                     "/highprice   - заглушка\n" \
                     "/bestdeal    - заглушка\n" \
                     "/history     - заглушка\n\n" \
                     "Если написать в чат 'привет', бот поздоровается в ответ."
        print(answer_str)
        bot.send_message(message.chat.id, answer_str)

    @bot.message_handler(commands=['lowprice'])
    def low_price(message: ClassVar) -> None:
        lowprice(message=message, bot=bot)

    @bot.message_handler(commands=['highprice'])
    def high_price(message: ClassVar) -> None:
        highprice(message=message, bot=bot)

    @bot.message_handler(commands=['bestdeal'])
    def best_deal(message: ClassVar) -> None:
        bestdeal(message=message, bot=bot)

    @bot.message_handler(commands=['history'])
    def hist(message: ClassVar) -> None:
        history(message=message, bot=bot)

    @bot.message_handler(content_types='text')
    def listen_all(message: ClassVar) -> None:
        """
        Функция отвечает на фразу 'привет' в тексте сообщения.
        Если получена фраза 'привет',
        здоровается в ответ, со смайликом.

        :param message: данные сообщения.
        :type message: telebot.types.Message
        """

        if message.text == 'привет':
            answer_str = 'Привет {u_name} {smile}'.format(
                u_name=message.from_user.first_name,
                smile=U'\U0001F600'
            )
        # else:
        #     answer_str = ' - You wrote: ' + message.text

            print(answer_str)
            bot.send_message(message.chat.id, answer_str)

    while True:
        try:
            bot.polling()
        except Exception as exc:
            print(exc)
            break


if __name__ == '__main__':
    main('token')
