import telebot

bot = telebot.TeleBot('5942487246:AAGhW_0wFKbZ-GNbweypIxbs3lSXqSaYPT8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello</b>', parse_mode='html')

bot.polling(none_stop=True)
