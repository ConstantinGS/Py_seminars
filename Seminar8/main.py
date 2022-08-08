from fileinput import close

database = {}
db_id = {"Parents": 1, "Childrens": 2, "Contacts": 3, "Marks": 4, "Classes": 5}

def reading_file_to_dict(number_file):
    
    
    with open(f'Py_seminars\Seminar8\{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))
        close



 # Найти ребенка родителя по фамилии

def print_childrens(second_name):
    id = [i[0] for i in  database[db_id["Parents"]] if second_name in i][0]
    child = [i for  i in database[db_id["Childrens"]] if id == i[1]]
    print(*[" ".join(i[2:4]) + '\n' for i in child] )

# Найти номер телефона родителя

def print_childrens(second_name):
    id = [i[0] for i in  database[db_id["Parents"]] if second_name in i][0]
    number = [i for  i in database[db_id["Contacts"]] if id == i[0]]
    print(second_name)
    print(*[i[1] + '\n' for i in number] )

# Вывести класс, который учится в кабинете N

def class_spisok(classroom):
  
    name_class = [i[1] for i in database[db_id["Classes"]] if classroom in i][0]
    print(f"В классной комнате {classroom} учится класс {name_class}:")
    students = [i for  i in database[db_id["Childrens"]] if name_class == i[5]]
    print(*[" ".join(i[2:4]) + '\n' for i in students] )
    
# Вывести табель успеваемости класса N

def class_marks(number_class):
    print(number_class)
    print("Ученик           math chemical literature")
    students = [i for  i in database[db_id["Childrens"]] if number_class == i[5]]
    marks = [i for  i in database[db_id["Marks"]] if i[0] in [i[0] for i in students]]
    spisok_students = [" ".join(i[2:4]) for i in students]
    spisok_marks = [" ".join(i[1:4]) for i in marks]

    for i in range(len(spisok_students)):
        print( spisok_students[i] + "      " + "      ".join(spisok_marks[i].split(" ")) + " \n" )

# Средняя оценка класса по предметам

def class_raiting(number_class):
    print(f" Средняя оценка класса {number_class}")
    print("math chemical literature")
    raiting = [1, 1, 1]
    students = [i for  i in database[db_id["Childrens"]] if number_class == i[5]]
    marks = [i for  i in database[db_id["Marks"]] if i[0] in [i[0] for i in students]]
    for i in marks:
        for j in range(1, len(i)):  raiting[j-1] *= float(i[j])
    for i in raiting:
        print(f"  {i}   ", end="")
   
 




reading_file_to_dict(1)
reading_file_to_dict(2)
reading_file_to_dict(3)
reading_file_to_dict(4)
reading_file_to_dict(5)

print_childrens('Ivanov')
class_spisok("42")
class_marks("7b")
class_raiting("7b")


   

 