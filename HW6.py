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















end_pr = time.time()
print(end_pr-start)
