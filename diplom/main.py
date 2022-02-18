import telebot
import json

# def main() -> None:

token = '5235302158:AAFNCdbTixqPCYK9a62GSwox7FsSxqBLufw'

bot = telebot.TeleBot(token, parse_mode = None)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi bro... :)")
    print('start, help', message)


@bot.message_handler(commands=['exit'])
def start_message(message):
    bot.lsend_message(message.chat.id, "Пока")
    print('command = exit. Пока', message)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

    print('echo_all')
    # for key, value in message.items():
    #     print(key, value)
    print(message.from_user.username)
    # print(message['content_type'])


bot.infinity_polling()

# if __name__ == '__main__':
#     main()
