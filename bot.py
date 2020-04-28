import telebot

bot = telebot.TeleBot("1113715967:AAEf5eBctEv0Oe2SNBMVLEur5-vOAF3r7hE")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
  #bot.reply_to(message, message.text)
  bot.send_message(message.chat.id, message.text + " це круто")
bot.polling( none_stop = True )
