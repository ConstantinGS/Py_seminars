from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler
import random
bot = Bot(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo")
updater = Updater(token = "5453828110:AAG3k4YA1OpkJ9d3yYep38MqRGqth_HAdbo") # Апдэйтер это класс опрашивающий сервер на предмет сообщений
dispatcher = updater.dispatcher # экзэмпляр объекта регистрирует обработчики,


START = 0
STEP1 = 1

ALL_CONTACTS = 2

NEW_CONTACTS_FN = 3
NEW_CONTACTS_SN = 4
NEW_CONTACTS_NB = 5
NEW_CONTACTS_DS = 6
SEARCH_CONTACT = 7
OVER = 4
counter = 0
move = 1
operation = 0
new_contact = ""


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Телефонный справочник"')
    context.bot.send_message(update.effective_chat.id, 'Выберите операцию')
    return STEP1

def help(update, context):
    context.bot.send_message(update.effective_chat.id, '1 - список контактов, 2 добавить новый контакт"')
    return STEP1


#ВЫБОР ОПЕРАЦИИ 
def change_operation(update, context):
    global operation
    operation = int(update.message.text)

    if operation == 1: return ALL_CONTACTS
    elif operation == 2:
        context.bot.send_message(update.effective_chat.id, 'Введите имя')
        return NEW_CONTACTS_FN
    elif operation == 3:
        context.bot.send_message(update.effective_chat.id, 'Введите имя и фамилию')
        return SEARCH_CONTACT 
    

#ПОКАЗАТЬ ВСЕ КОНТАКТЫ
def show_all_contacts(update, context):
    print("here")
    with open(f'Py_seminars\sem10\data.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in data:
            context.bot.send_message(update.effective_chat.id, f'{i}')
    return STEP1


#ДОБАВИТЬ НОВЫЙ КОНТАКТ

def add_fn_contact(update, context):
    global new_contact 
    new_contact += f'*{update.message.text}\n'
    context.bot.send_message(update.effective_chat.id, 'Введите фамилию') 
    return NEW_CONTACTS_SN
def add_sn_contact(update, context):
    global new_contact 
    new_contact += f'{update.message.text}\n'
    context.bot.send_message(update.effective_chat.id, 'Введите номер телефона') 
    return NEW_CONTACTS_NB
def add_nm_contact(update, context):
    global new_contact 
    new_contact += f'{update.message.text}\n'
    context.bot.send_message(update.effective_chat.id, 'Введите описание') 
    return NEW_CONTACTS_DS
def add_ds_contact(update, context):
    global new_contact 
    new_contact += f'{update.message.text}*\n\n'
    file = open('Py_seminars\sem10\data.txt', "a", encoding='utf-8')
    file.write(f"{new_contact}")
    file.close()
    new_contact = ""

    return STEP1



# ПОИСК КОНТАКТА ПО ИМЕНИ И ФАМИЛИИ
def search(update, context):

    context.bot.send_message(update.effective_chat.id, 'ТУт')
    sought_contact = update.message.text
    file = open('Py_seminars\sem10\data.txt', "r", encoding='utf-8')
    data = file.readlines()
    
    first_last =  sought_contact.split(" ")
    if len(first_last) == 2:
        merker = 0
        for i in range(len(data)-3): 
            if  first_last[0] in data[i] and first_last[1] in data[i+1]:
                context.bot.send_message(update.effective_chat.id, f'{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
                merker = 1
            elif (first_last[0] in data[i] or first_last[1] in data[i+1]) and merker == 0:
                context.bot.send_message(update.effective_chat.id,f'{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
            
    elif len(first_last) == 1:
        for i in range(len(data)-2): 
            if  first_last[0] in data[i] :
                context.bot.send_message(update.effective_chat.id,f'{data[i-1]}{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
            
    file.close()




            
# ВЫХОД
def cancel(update, context):
    
    context.bot.send_message(update.effective_chat.id, "END")
    return ConversationHandler.END



start_handler = CommandHandler('start', start)
change_handler = MessageHandler(Filters.text, change_operation)
show_handler = MessageHandler(Filters.text, show_all_contacts)
add_fn_handler = MessageHandler(Filters.text, add_fn_contact)
add_sn_handler = MessageHandler(Filters.text, add_sn_contact)
add_nb_handler = MessageHandler(Filters.text, add_nm_contact)
add_ds_handler = MessageHandler(Filters.text, add_ds_contact)
search_handler = MessageHandler(Filters.text, search)
cancel_handler = CommandHandler("cancel", cancel)
conver_handler = ConversationHandler(entry_points=[start_handler],
                                states = {
                                    STEP1: [change_handler],
                                    ALL_CONTACTS:  [show_handler],

                                    NEW_CONTACTS_FN: [add_fn_handler],
                                    NEW_CONTACTS_SN: [add_sn_handler],
                                    NEW_CONTACTS_NB: [add_nb_handler],
                                    NEW_CONTACTS_DS: [add_ds_handler],

                                    SEARCH_CONTACT: [search_handler],



                                        }, 
                                fallbacks=[cancel_handler] )


dispatcher.add_handler(conver_handler)

updater.start_polling()
updater.idle()


