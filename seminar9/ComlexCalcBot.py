from email import message
from turtle import update
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from calcul import complex_calc

# bot = Bot("5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Инициализация бота

bot = Bot(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo")
updater = Updater(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Апдэйтер это класс опрашивающий сервер на предмет сообщений
dispatcher = updater.dispatcher # экзэмпляр объекта регистрирует обработчики, 

# context - при регистрации обработчика передается обратно в функцию
START = 0
NUMBERFIRST = 1
NUMBERSECOND = 2
OPERATION = 3
RESULT = 4
numberOne=""
numberTwo=""
operat=""
name = ""
time = ""


def numbers(number):
    pass

def start(update, context):

    name = update.message.from_user.first_name
    data = update.message.date
    file = open('Py_seminars\seminar9\log.txt', "a", encoding='utf-8')
    file.writelines(f"{name} \n {data} \n")
    file.close()
    
    context.bot.send_message(update.effective_chat.id, f'Введите первое число, в формате "5+5i" {name}')
    
    return NUMBERFIRST

def numberFirst(update, context):
    global numberOne
    numberOne += update.message.text
    context.bot.send_message(update.effective_chat.id, "Второе число")
    return NUMBERSECOND

def numberSecond(update, context):
    global numberTwo
    numberTwo += update.message.text
    context.bot.send_message(update.effective_chat.id, "Операция")
    
    plus = InlineKeyboardButton("+", callback_data = "+")
    minus = InlineKeyboardButton("-", callback_data = "-")
    mul = InlineKeyboardButton("*", callback_data = "*")
    div = InlineKeyboardButton("/", callback_data = "/")
    keyboard = [[plus], [minus], [mul], [div]]
    update.message.reply_text("Change: ", reply_markup = InlineKeyboardMarkup(keyboard))
    

    
    return OPERATION


def operation(update, context):

    global res
    # global oper
    que = update.callback_query
    var = que.data
    que.answer()
    res = complex_calc(numberOne, numberTwo, var)
 
    file = open('Py_seminars\seminar9\log.txt', "a", encoding='utf-8')
    file.writelines(f"{res} \n")
    file.close()
    que.edit_message_text(text=f'Результат: {res}')


def cancel(update, context):
    
    context.bot.send_message(update.effective_chat.id, "END")
    return ConversationHandler.END



start_handler = CommandHandler('start', start)
numOne_handler = MessageHandler(Filters.text, numberFirst)
numTwo_handler = MessageHandler(Filters.text, numberSecond)
oper_handler = CallbackQueryHandler(operation)
cancel_handler = CommandHandler("cancel", cancel)
conver_handler = ConversationHandler(entry_points=[start_handler],
                                states = {
                                    NUMBERFIRST: [numOne_handler],
                                    NUMBERSECOND: [numTwo_handler],
                                    OPERATION: [oper_handler]
                                        }, 
                                fallbacks=[cancel_handler] )


dispatcher.add_handler(conver_handler)

updater.start_polling()
updater.idle()
