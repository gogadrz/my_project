from typing import ClassVar


def highprice(message: ClassVar, bot: ClassVar) -> None:
    """
    Заглушка для команды /highprice

    :param message: данные сообщения
    :type message: telebot.types.Message

    :param bot: для отправки сообщения от бота
    :type bot: class 'telebot.TeleBot
    """
    answer_str = 'Inside highrice(): {text}'.format(text=message.text)

    print(answer_str)
    bot.send_message(message.chat.id, answer_str)
