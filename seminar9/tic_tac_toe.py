from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler

bot = Bot(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo")
updater = Updater(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Апдэйтер это класс опрашивающий сервер на предмет сообщений
dispatcher = updater.dispatcher # экзэмпляр объекта регистрирует обработчики,


START = 0
STEP1 = 1
STEP2= 2
STEP3 = 3
OVER = 4
counter = 0

field_ttt = [[" * ", " * ", " * " ],    
             [" * ", " * ", " * " ],
             [" * ", " * ", " * " ]]
field = [[InlineKeyboardButton(field_ttt[0][0], callback_data='1'), InlineKeyboardButton(field_ttt[0][1], callback_data=f'2'), InlineKeyboardButton(field_ttt[0][2], callback_data='3')],
         [InlineKeyboardButton(field_ttt[1][0], callback_data= '4'), InlineKeyboardButton(field_ttt[1][1], callback_data='5'), InlineKeyboardButton(field_ttt[1][2], callback_data='6')],
         [InlineKeyboardButton(field_ttt[2][0], callback_data='7'), InlineKeyboardButton(field_ttt[2][1], callback_data='8'), InlineKeyboardButton(field_ttt[2][2], callback_data='9')]]
def counter_field(num, field):
 
    if num == "1": field[0][0] = "X"
    elif num == "2": field[0][1] = "X"
    elif num == "3": field[0][2] = "X"
    elif num == "4": field[1][0] = "X"
    elif num == "5": field[1][1] = "X"
    elif num == "6": field[1][2] = "X"
    elif num == "7": field[2][0] = "X"
    elif num == "8": field[2][1] = "X"
    elif num == "9": field[2][2] = "X"

    return field


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в игру "Крестики и нолики"')
    context.bot.send_message(update.effective_chat.id, "Поле", reply_markup = InlineKeyboardMarkup(field))
    return STEP1

def operation(update, context):
    global field_ttt
    global field
    global counter
    query = update.callback_query
    variant = query.data
    query.answer()
    field_ttt = counter_field(variant, field_ttt)
    field = [[InlineKeyboardButton(field_ttt[0][0], callback_data='1'), InlineKeyboardButton(field_ttt[0][1], callback_data=f'2'), InlineKeyboardButton(field_ttt[0][2], callback_data='3')],
            [InlineKeyboardButton(field_ttt[1][0], callback_data= '4'), InlineKeyboardButton(field_ttt[1][1], callback_data='5'), InlineKeyboardButton(field_ttt[1][2], callback_data='6')],
            [InlineKeyboardButton(field_ttt[2][0], callback_data='7'), InlineKeyboardButton(field_ttt[2][1], callback_data='8'), InlineKeyboardButton(field_ttt[2][2], callback_data='9')]]
    context.bot.send_message(update.effective_chat.id, field_ttt)
    context.bot.send_message(update.effective_chat.id, "Поле", reply_markup = InlineKeyboardMarkup(field))
    counter +=1
    if counter <9:return STEP2
    context.bot.send_message(update.effective_chat.id, "Игра окончена") 
       


def cancel(update, context):
    
    context.bot.send_message(update.effective_chat.id, "END")
    return ConversationHandler.END



start_handler = CommandHandler('start', start)
draw_handler = CallbackQueryHandler(operation)
cancel_handler = CommandHandler("cancel", cancel)
conver_handler = ConversationHandler(entry_points=[start_handler],
                                states = {
                                    STEP1: [draw_handler],
                                    STEP2: [draw_handler]
                                        }, 
                                fallbacks=[cancel_handler] )


dispatcher.add_handler(conver_handler)

updater.start_polling()
updater.idle()








