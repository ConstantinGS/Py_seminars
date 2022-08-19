from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler
import random
bot = Bot(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo")
updater = Updater(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Апдэйтер это класс опрашивающий сервер на предмет сообщений
dispatcher = updater.dispatcher # экзэмпляр объекта регистрирует обработчики,


START = 0
STEP1 = 1
STEP2= 2
STEP3 = 3
OVER = 4
counter = 0
move = 1

field_ttt = [[" * ", " * ", " * " ],    
             [" * ", " * ", " * " ],
             [" * ", " * ", " * " ]]
field = [[InlineKeyboardButton(field_ttt[0][0], callback_data='1'), InlineKeyboardButton(field_ttt[0][1], callback_data=f'2'), InlineKeyboardButton(field_ttt[0][2], callback_data='3')],
         [InlineKeyboardButton(field_ttt[1][0], callback_data= '4'), InlineKeyboardButton(field_ttt[1][1], callback_data='5'), InlineKeyboardButton(field_ttt[1][2], callback_data='6')],
         [InlineKeyboardButton(field_ttt[2][0], callback_data='7'), InlineKeyboardButton(field_ttt[2][1], callback_data='8'), InlineKeyboardButton(field_ttt[2][2], callback_data='9')]]
def counter_field(num, field):
    global counter
    global move

    if move:
        
        if num == "1" and field[0][0] == " * " : field[0][0] = "X"
        elif num == "2" and field[0][1] == " * ": field[0][1] = "X"
        elif num == "3" and field[0][2] == " * ": field[0][2] = "X"
        elif num == "4" and field[1][0] == " * ": field[1][0] = "X"
        elif num == "5" and field[1][1] == " * ": field[1][1] = "X"
        elif num == "6" and field[1][2] == " * ": field[1][2] = "X"
        elif num == "7" and field[2][0] == " * ": field[2][0] = "X"
        elif num == "8" and field[2][1] == " * ": field[2][1] = "X"
        elif num == "9" and field[2][2] == " * ": field[2][2] = "X"

        if ((field[0] == ["X", "X", "X" ] or field[1] == ["X", "X", "X" ] or field[2] == ["X", "X", "X" ]) or
            (field[0][0] == 'X' and field[0][0] == field[1][0] and  field[0][0] == field[2][0]) or
            (field[0][1] == 'X' and field[0][1] == field[1][1] and  field[0][1] == field[2][1]) or
            (field[0][2] == 'X' and field[0][2] == field[1][2] and  field[0][2] == field[2][2]) or
            (field[0][0] == 'X' and field[0][0] == field[1][1] and  field[0][0] == field[2][2]) or
            (field[1][1] == 'X' and field[2][0] == field[1][1] and  field[2][0] == field[0][2])): 
            counter = 9
            return field

        counter +=1
        move = 0

    if move == 0:
        temp1 = random.randint(0,2)
        temp2 = random.randint(0,2)
                
        while field[temp1][temp2] != " * ":
            temp1 = random.randint(0,2)
            temp2 = random.randint(0,2)

        field[temp1][temp2] = "0"
        if ((field[0] == ["0", "0", "0" ] or field[1] == ["0", "0", "0" ] or field[2] == ["0", "0", "0" ]) or
            (field[0][0] == '0' and field[0][0] == field[1][0] and  field[0][0] == field[2][0]) or
            (field[0][1] == '0' and field[0][1] == field[1][1] and  field[0][1] == field[2][1]) or
            (field[0][2] == '0' and field[0][2] == field[1][2] and  field[0][2] == field[2][2]) or
            (field[0][0] == 'X' and field[0][0] == field[1][1] and  field[0][0] == field[2][2]) or
            (field[1][1] == 'X' and field[2][0] == field[1][2] and  field[2][0] == field[0][2])): 
            counter = 9
            return field
        counter +=1
        move = 1

    return field


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в игру "Крестики и нолики"')
    context.bot.send_message(update.effective_chat.id, "Поле", reply_markup = InlineKeyboardMarkup(field))
    return STEP1

def operation(update, context):
    global field_ttt
    global field
    
    query = update.callback_query
    variant = query.data
    query.answer()
    field_ttt = counter_field(variant, field_ttt)
    field = [[InlineKeyboardButton(field_ttt[0][0], callback_data='1'), InlineKeyboardButton(field_ttt[0][1], callback_data=f'2'), InlineKeyboardButton(field_ttt[0][2], callback_data='3')],
            [InlineKeyboardButton(field_ttt[1][0], callback_data= '4'), InlineKeyboardButton(field_ttt[1][1], callback_data='5'), InlineKeyboardButton(field_ttt[1][2], callback_data='6')],
            [InlineKeyboardButton(field_ttt[2][0], callback_data='7'), InlineKeyboardButton(field_ttt[2][1], callback_data='8'), InlineKeyboardButton(field_ttt[2][2], callback_data='9')]]
    context.bot.send_message(update.effective_chat.id, field_ttt)
    context.bot.send_message(update.effective_chat.id, "Поле", reply_markup = InlineKeyboardMarkup(field))
    
    if counter <9:return STEP2
    if move:
        context.bot.send_message(update.effective_chat.id, "Вы выиграли")
    else:
        context.bot.send_message(update.effective_chat.id, "Вы проиграли")  
       


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








