from email import message
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


bot = Bot("5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Инициализация бота
updater = Updater("5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo")
dispatcher = updater.dispatcher

def tic_tac_toe():
    pass

message_handler = MessageHandler(Filters.text, message) # Отслеживание. Вид обрабатываемых сообщений (здесь текст)
dispatcher.add_handler(message_handler)




updater.start_polling()
updater.idle(   )