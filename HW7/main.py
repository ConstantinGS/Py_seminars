#Главный блок
from data import data_new_contact
from change_data import new_data
from enter import action_User
from enter import hello_User
from log import new_log
from data import data_read

format = hello_User()
action = 0

while action!=3:

    action = action_User()

    if action == 1:
        print("Чтение данных ...")
        new_log(data_read(), format)
        print("Данные считаны")

    elif action == 2:
        data_new_contact(new_data(format), format)  
        print("Обновление данных ...")
        new_log(data_read(), format)
        print("Данные обновлены")

    













