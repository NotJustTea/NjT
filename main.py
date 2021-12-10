import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])
def message_recieved(message):
    print(message)
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)



