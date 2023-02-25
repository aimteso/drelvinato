import telebot

bot = telebot.TeleBot('6262495766:AAGN54gw1NlhwNxrx3jiRM1bZ2NIq2V7skY')

@bot.message_handler(command=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Privet</b>', parse_mode='html')

bot.polling(none_stop=True)