import telebot


bot = telebot.TeleBot('1748688926:AAGXOJNZLVtHoCGD5okX9FVy__mN06TkRAA')

@bot.message_handler(content_types=['start'])

def start_message(message):
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")

bot.polling()

