from typing import ClassVar


def lowprice(message: ClassVar, bot: ClassVar) -> None:
    """
    Заглушка для команды /lowprice

    :param message: данные сообщения
    :type message: telebot.types.Message

    :param bot: для отправки сообщения от бота
    :type bot: class 'telebot.TeleBot
    """
    answer_str = 'Inside lowprice(): {text}'.format(text=message.text)

    print(answer_str)
    bot.send_message(message.chat.id, answer_str)
