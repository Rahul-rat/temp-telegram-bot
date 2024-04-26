import telebot 
from keep_alive import keep_alive
token = "7051931465:AAFyUKX3GnJLHY1EonmI0azYM7i9Y5FzCxw"

bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
