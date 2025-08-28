import telebot

bot = telebot.TeleBot("8497680999:AAHclqnExmf1FsIlptHPalXnEC5zlxFHMTY")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Tesabetcoin oyununa hoş geldin!")
  
    bot.polling()