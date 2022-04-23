from telegram.ext import Updater
from telegram.ext import CommandHandler

print('d')

#def main():
 #   my_bot = Updater("5377207149:AAF2h6pTLxrwrf0zqqd6sWrox5zbnnx6qf8" , "https://telegg.ru/orig/bot",use_context=True)
  #  my_bot.start_polling()
   # my_bot.idle()

def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")

updater = Updater(token='5377207149:AAF2h6pTLxrwrf0zqqd6sWrox5zbnnx6qf8')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
# только на команду /start

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!


print('d')