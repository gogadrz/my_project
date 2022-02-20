import telebot
import os
from typing import ClassVar
from lowprice import lowprice
from highprice import highprice
from bestdeal import bestdeal
from history import history


class HotelsBot:
    def __init__(self, file_name):
        self.__token = self.__get_token(file_name)

    @classmethod
    def __get_token(cls, file_name: str) -> str:
        full_file_name = os.path.abspath(os.path.join(os.path.curdir, file_name))
        if not os.path.exists(full_file_name):
            print('Файл {f_name} (содержащий токен) не найден.'.format(f_name=file_name))
            return ''

        with open(full_file_name, 'r') as file:
            return file.read()


def main(file_name: str) -> None:

    done: bool = False
    debug: bool = True  # если True, вывод будет дублироваться в консоль

    token: str = get_token(file_name)
    if token == '':
        return

    bot: ClassVar = telebot.TeleBot(token, parse_mode=None)

    @bot.message_handler(commands=['hello-world'])
    def start_message(message: ClassVar) -> None:
        answer_str = 'Привет {u_name} {smile}\nОтвет из команды /hello-world'.format(
            u_name=message.from_user.first_name,
            smile=U'\U0001F44C'
        )

        if debug:
            print(answer_str)

        bot.send_message(message.chat.id, answer_str)

    @bot.message_handler(commands=['exit'])
    def exit_message(message: ClassVar) -> None:

        answer_str = 'Выполнена команда "/exit"\nПока.'

        if debug:
            print(answer_str)

        bot.send_message(message.chat.id, answer_str)

        nonlocal done
        done = True
        bot.stop_polling()

    @bot.message_handler(commands=['lowprice'])
    def low_price(message: ClassVar) -> None:
        lowprice(message=message, bot=bot, debug=debug)

    @bot.message_handler(commands=['highprice'])
    def high_price(message: ClassVar) -> None:
        highprice(message=message, bot=bot, debug=debug)

    @bot.message_handler(commands=['bestdeal'])
    def best_deal(message: ClassVar) -> None:
        bestdeal(message=message, bot=bot, debug=debug)

    @bot.message_handler(commands=['history'])
    def hist(message: ClassVar) -> None:
        history(message=message, bot=bot, debug=debug)

    @bot.message_handler(content_types='text')
    def listen_all(message: ClassVar) -> None:
        # bot.reply_to(message, message.text)

        if message.text == 'привет':
            answer_str = 'Привет {u_name} {smile}'.format(
                u_name=message.from_user.first_name,
                smile=U'\U0001F600'
            )
        else:
            answer_str = ' - You wrote: ' + message.text

        if debug:
            print(answer_str)

        bot.send_message(message.chat.id, answer_str)

    while not done:
        try:
            bot.polling()
        except Exception as exc:
            print(exc)
            break


if __name__ == '__main__':
    main('token')
