from typing import ClassVar


def bestdeal(message: ClassVar, bot: ClassVar) -> None:
    """
    Заглушка для команды /bestdeal

    :param message: данные сообщения
    :type message: telebot.types.Message

    :param bot: для отправки сообщения от бота
    :type bot: class 'telebot.TeleBot
    """
    answer_str = 'Inside bestdeal(): {text}'.format(text=message.text)

    print(answer_str)
    bot.send_message(message.chat.id, answer_str)
