from typing import ClassVar


def highprice(message: ClassVar, bot: ClassVar, debug: bool) -> None:

    answer_str = 'Inside highrice(): {text}'.format(text=message.text)

    if debug:
        print(answer_str)

    bot.send_message(message.chat.id, answer_str)
