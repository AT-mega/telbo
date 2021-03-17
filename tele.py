import telebot
import pywhatkit 
from datetime import datetime 
bot = telebot.TeleBot("1135186491:AAFaDHnoJhgu7B-5lwDNymZs2BzraL10-9I",parse_mode="MarkdownV2")


@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot!")

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.reply_to(message, message.text)
    print(message.text)
    time = datetime.now()
    pywhatkit.sendwhatmsg("+918526376900",message.text ,time.hour,time.minute+1)


bot.polling()