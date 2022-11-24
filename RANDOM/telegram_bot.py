import telebot
bot = telebot.TeleBot('5629960231:AAFnog4cs9MYVbqswwN2KX8HD9tR1wd0lS8')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "С чем пожаловал?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "ПАМАГИТИ!!!")
    elif message.text == "yes":
        bot.send_message(message.from_user.id, "Йес, йес, ОБХСС")
    elif message.text in ['петросян', 'Петросян', '@петросян']:
        bot.send_message(message.from_user.id, "Я те ткну")

bot.polling(none_stop=True, interval=0)