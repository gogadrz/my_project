from typing import ClassVar


def bestdeal(message: ClassVar, bot: ClassVar, debug: bool) -> None:

    answer_str = 'Inside destdeal(): {text}'.format(text=message.text)

    if debug:
        print(answer_str)

    bot.send_message(message.chat.id, answer_str)
