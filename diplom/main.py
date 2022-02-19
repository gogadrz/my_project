import telebot


def main():
    done = False

    with open('token', 'r') as file:
        token = file.read()
    bot = telebot.TeleBot(token, parse_mode = None)

    @bot.message_handler(commands = ['start', 'help'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hi bro... :)")
        print('start, help', message)

    @bot.message_handler(commands = ['exit'])
    def start_message(message):
        bot.send_message(message.chat.id, "Пока")

        print('command = exit. Пока', message.text)
        nonlocal done
        done = True
        bot.stop_polling()
        # bot.infinity_polling(skip_pending = True)
        exit(0)

    # @bot.message_handler(func=lambda m: True)
    @bot.message_handler(content_types = 'text')
    def echo_all(message):
        # bot.reply_to(message, message.text)
        answer_str = 'bot answer: ' + message.text
        bot.send_message(message.chat.id, answer_str)

        print('function: echo_all()')
        # for key, value in message.items():
        #     print(key, value)
        print(message.from_user.username)  # print(message['content_type'])

        # bot.infinity_polling(skip_pending = False)

    while not done:
        try:
            bot.polling()
        except Exception as exc:
            print(exc)
            break


if __name__ == '__main__':
    main()
