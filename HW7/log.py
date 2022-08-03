

def new_log(data_file, type_output):

    output_file = ""
    if data_file == "":
        print("Справочник пуст")
    else:
        if type_output == 1:
            print("Тип вывода данных построчный")
            for i in range(len(data_file)-1):
                if data_file[i] != ",":
                    output_file += data_file[i]
                if data_file[i] == ";" or data_file[i] == ",":
                    output_file += "\n"
            output_file += data_file[len(data_file)-1]


        elif type_output == 2:
            output_file = data_file
            print("Тип вывода данных в одну строку")
        
        file = open('Py_seminars\HW7\logbook.txt', "w", encoding='utf-8')
        file.write(output_file)
        file.close()

