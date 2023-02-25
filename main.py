import telebot

bot = telebot.TeleBot('5942487246:AAGhW_0wFKbZ-GNbweypIxbs3lSXqSaYPT8')


@bot.message_handler(command=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Privet</b>', parse_mode='html')


bot.polling(none_stop=True)
