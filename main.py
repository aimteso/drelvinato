import telebot

bot = telebot.TeleBot('6262495766:AAEjtiuPNbKbAJuNyo6kUS253Lv52WQ7Rdw')


@bot.message_handler(command=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Privet</b>', parse_mode='html')


bot.polling(none_stop=True)
