import telebot
from telebot import types

bot = telebot.TeleBot('5942487246:AAGhW_0wFKbZ-GNbweypIxbs3lSXqSaYPT8')

# Open and read the text file containing questions and answers
with open('questions.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    qa_pairs = [line.strip().split(',') for line in lines]


# Define the message handlers
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,)
    location_button = types.KeyboardButton('Lokasiya 📍')
    payment_options_button = types.KeyboardButton('Ödəmə 💰')
    shipment_button = types.KeyboardButton('Çatdırılma 🚚')
    address_button = types.KeyboardButton('Ünvan və Telefon nömrəsi 📞')
    markup.add(location_button, payment_options_button, shipment_button, address_button)

    mess = f'Salam, <b>{message.from_user.first_name} {message.from_user.last_name}.</b> Sizə necə komək edə bilərəm?'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda message: True, regexp='Lokasiya 📍')
def handle_location(message):
    latitude = 40.5891367
    longitude = 49.6756716
    bot.send_venue(message.chat.id, latitude, longitude, 'Adress', 'adresssss',  'https://goo.gl/maps/E4mV8spsCyD1gxxG9')


@bot.message_handler(func=lambda message: True, regexp='Ödəmə 💰')
def handle_payment_options(message):
    bot.send_message(message.chat.id, 'Visa, MasterCard, Bank kartları və ya Nəğd.')


@bot.message_handler(func=lambda message: True, regexp='Çatdırılma 🚚')
def handle_shipment(message):
    bot.send_message(message.chat.id, 'Poçt ilə istənilən kənd və şəhərə. Məbləğin önəmi yoxdur. İstənilən məbləğdə '
                                      'məhsul çatdırılır.')


@bot.message_handler(func=lambda message: True, regexp='Ünvan və Telefon nömrəsi 📞')
def handle_address(message):
    bot.send_message(message.chat.id, 'Sumqayıt 1 mkr. Teıefon 050 000 00 00.')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Search for a matching question and send the corresponding answer
    for qa_pair in qa_pairs:
        if qa_pair[0].lower() in message.text.lower():
            bot.send_message(message.chat.id, qa_pair[1])
            return
    # If no matching question was found, send a default message
    bot.send_message(message.chat.id, "Üzr istəyirəm, bu sualınızı cavablaya bilmirəm.")

 # Save user request to a file
    with open('user_requests.txt', 'a', encoding='utf-8') as f:
        f.write(f"{message.from_user.id}: {message.from_user.username}: {message.text}\n")

# Start the bot
bot.polling()
