# Блок хранящий данные 



def data_read():
    stroka = ""
    with open('Py_seminars\HW7\data.txt', encoding='utf-8') as file:
        spisok_strok = file.readlines()
        for i in spisok_strok:
            stroka += i
 
        return stroka
            


def data_new_contact(new_data, format):
    new_contact = ""
    if format == 1:
        for i in new_data:
            new_contact += str(i)+" "
        new_contact += ';\n'
    if format == 2:
        new_contact += new_data
        new_contact += ' ;'
    
    
    file = open('Py_seminars\HW7\data.txt', "a", encoding='utf-8')
    file.write(f"{new_contact} \n")
    file.close()




    











    
        
