from telegram.ext import Filters
from telegram.ext import Updater #Логиниться
from telegram.ext import CommandHandler #Отвечает на команды
from telegram.ext import MessageHandler #Читает сообщения
from settings import TG_token

from telegram import Update
from telegram.ext import CallbackContext


import telegram
#bot = telegram.Bot(token='5377207149:AAF2h6pTLxrwrf0zqqd6sWrox5zbnnx6qf8')
#print(bot.get_me())
#updates = bot.get_updates()
#print(updates)




def sms(bot,update):
    #print(bot.message) #выдает все данные об отправителе
    bot.message.reply_text('пошел на хуй {}!'.format(bot.message.chat.first_name))
    bot.message.reply_text(bot.message.chat.username)
    print(bot.message.chat.username)

def sms1(bot,update):
    bot.message.reply_text('bye')

def parrot(bot,update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)

def main():
    print('0')
    my_bot = Updater(TG_token)
    print('1')
    my_bot.dispatcher.add_handler(CommandHandler('start',sms))
    my_bot.dispatcher.add_handler(CommandHandler('hi',sms1))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text,parrot))
    print('2')
    my_bot.start_polling()
    print('3')
    my_bot.idle()
    print('4')



main()


print('g')