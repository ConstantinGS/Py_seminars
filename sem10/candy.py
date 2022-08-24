# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler
import random
bot = Bot(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo")
updater = Updater(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Апдэйтер это класс опрашивающий сервер на предмет сообщений
dispatcher = updater.dispatcher # экзэмпляр объекта регистрирует обработчики,


START = 0
STEP1 = 1
candy = 221
move = 0

PLAYER = 2
OVER = 3

def start(update, context):
    global move
    global candy
    move = random.randint(0,1)
    context.bot.send_message(update.effective_chat.id, f'На столе {candy} конфет')
    if move == 0:
        context.bot.send_message(update.effective_chat.id, f'Мой ход')
        bot_taking = random.randint(1,29)
        context.bot.send_message(update.effective_chat.id, f'Беру {bot_taking}') 
        candy -= bot_taking
        context.bot.send_message(update.effective_chat.id, f'Конфет на столе {candy}')
        move = 1
    else:
        context.bot.send_message(update.effective_chat.id, f'Твой ход') 
    return PLAYER
    

def move_player(update, context):
    global candy
    global move
    context.bot.send_message(update.effective_chat.id, f'Тут') 
    if move == 1:

        player_taking = int(update.message.text)
        if player_taking > 28:
            context.bot.send_message(update.effective_chat.id, f'Возьми поменьше')
            return PLAYER
        else:
            candy -= player_taking
            move = 0
            context.bot.send_message(update.effective_chat.id, f'Конфет на столе {candy}')
            if candy <=28:
                context.bot.send_message(update.effective_chat.id, f'Ты проиграл')
                return OVER
            

    if move == 0:
        bot_taking = random.randint(1,29) 
        context.bot.send_message(update.effective_chat.id, f'Беру {bot_taking}') 
        candy -= bot_taking
        move = 1
        context.bot.send_message(update.effective_chat.id, f'Конфет на столе {candy}')
        if candy <=28:
            context.bot.send_message(update.effective_chat.id, f'Ты выиграл')
            return OVER
        else: 
            context.bot.send_message(update.effective_chat.id, f'Твой ход')
            return PLAYER
            


def cancel(update, context):
    
    context.bot.send_message(update.effective_chat.id, "END")
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
player_handler = MessageHandler(Filters.text, move_player)
cancel_handler = CommandHandler("cancel", cancel)
conver_handler = ConversationHandler(entry_points=[start_handler],
                                states = {
                                    PLAYER:[player_handler],
                                    OVER:[cancel_handler],
                                        }, 
                                fallbacks=[cancel_handler] )


dispatcher.add_handler(conver_handler)
updater.start_polling()
updater.idle()