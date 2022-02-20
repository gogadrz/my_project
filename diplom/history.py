from typing import ClassVar


def history(message: ClassVar, bot: ClassVar) -> None:
    """
    Заглушка для команды /history

    :param message: данные сообщения
    :type message: telebot.types.Message

    :param bot: для отправки сообщения от бота
    :type bot: class 'telebot.TeleBot
    """
    answer_str = 'Inside history(): {text}'.format(text=message.text)

    print(answer_str)
    bot.send_message(message.chat.id, answer_str)
