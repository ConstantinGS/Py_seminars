import time


start = time.time()

transformation = lambda value: value   # Нам ведь по сути нужна лямбда-функция пустышка? Или я наверное как то не так понял задание?

def ex1_mimicry():

    values = [1, 23, 42, "asdfg"]
    transformed_values = list(map(transformation, values))
    if values == transformed_values:
        print("ok")
    else:
        print("fail")

#ex1_mimicry()





# Тут тоже немного не уловил. Зачем в условии приводится формула площади, если сказано круговые не учитывать?
# Если речь идет о планете которая дальше всех может быть в принwипе, то разве не достаточно просто взять самое
# большое значение полуоси? Ну и  пример это подверждает.

def ex_2_find_farthest_orbit_var1():
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    calc = lambda a, b: a*b*3.14
    planet = []
    farthest = 0
    farthest_len = [0, 0]

    for i in orbits:  
        if calc(*list(i))>farthest: 
            farthest = calc(*list(i))
            farthest_len = i
    print(farthest_len)


def ex_2_find_farthest_orbit_var2():
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    farthest_len = [0, 0]
    farthest = 0
    for i in orbits:
       if max(list(i))>farthest:
            farthest = max(list(i))
            farthest_len = i

    print(farthest_len)


#ex_2_find_farthest_orbit_var1()
#ex_2_find_farthest_orbit_var2()



def ex_3_param_pam_pam(poem):
    vowels = ["а", "и", "у", "е", "э", "ы", "о", "ю", "я"]
    phrases = "".join(list(filter(lambda x: x in vowels or x == " ", poem)))
    list_syllables = phrases.split(" ")
    merker = False
    for i in range(len(list_syllables)-1):
        if list_syllables[i] != list_syllables[i+1]:
            merker = True
            break
    if merker:    
        print("Пам парам")
    else:
        print("Парам пам-пам")


#ex_3_param_pam_pam("пара-ра-рам рам-пам-папам па-ра-па-дам")



def ex_4_same_by(characteristic, objects):
    if len(objects)<=1 : return True

    temp = characteristic(objects[0])
    result = True

    for i in objects:
        if temp != characteristic(i):
            result = False
            break
    return result

# values = [2, 4, 6]
# if ex_4_same_by(lambda x: x%2, values):
#     print("same")
# else: print ('different')


def ex5_print_operation_table(operation, num_rows=9, num_colomns=9):
    rows = [i for i in range(1, num_rows+1)]
    for i in range(1, num_colomns+1):
        colomns = [i for y in range(1, num_colomns+1)]
        table = list(map(operation, rows, colomns))
        print(*table)

a = 5
b = 5
ex5_print_operation_table(lambda x,y: x*y, a, b)

end_pr = time.time()
print(end_pr-start)




