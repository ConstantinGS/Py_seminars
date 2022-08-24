from traceback import print_exception


def search():

    contact = "Имя2"
    name = "Имя1"
    file = open('Py_seminars\sem10\data.txt', "r", encoding='utf-8')
    data = file.readlines()
    first_last =  contact.split(" ")
    if len(first_last) == 2:
        for i in range(len(data)-3): 
            if  first_last[0] in data[i] and first_last[1] in data[i+1]:
                print(f'{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
            elif first_last[0] in data[i] and first_last[1] not in data[i+1]:
                print(f'{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
            elif first_last[0] not in data[i] and first_last[1] in data[i+1]:
                print(f'{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
    elif len(first_last) == 1:
        for i in range(len(data)-2): 
            if  first_last[0] in data[i] :
                print(f'{data[i-1]}{data[i]}{data[i+1]}{data[i+2]}{data[i+3]} \n')
            
    print(len(first_last))
    file.close()


search()