# Изменение данных
# Создание нового контакта
# Редактирование существующего контакта

# Фамилия_1*

# *Имя_1*

# *Телефон_1*

# *Описание_1*

def new_data(format):
    print("Создание нового контакта \n")
    if format == 1:

    
        last_name = input("Введите фамилию \n")+","
        first_name = input("Введите имя \n")+","
        number_tel = input("Введите номер телефона \n")+","
        description = input("Введите описание контакта \n")
        new_contact = [last_name, first_name, number_tel, description]

    elif format == 2:

        new_contact = input("Введите фамилию, имя, номер телефона и описание контакта  \n")
        
    return new_contact




