import math

# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



def ex1_sumel():

    list_numbers = [6, 5, 10, 78, 42, 2, 30, 10, 20]

    for i in range(len(list_numbers)):
        if i%2!=0:
            print(list_numbers[i])

# ex1_sumel()



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def ex2_mulcouples(list_numbers):

    new_list_numbers = []
    for i in range(math.ceil(len(list_numbers)/2)):
        new_list_numbers.append(list_numbers[i]*list_numbers[-i-1])

    print (new_list_numbers)


# list_num = [2, 3, 5, 6]
# ex2_mulcouples(list_num)




# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def ex3_floatmaxmin_math(list_numbers):
    temp = 0
    min = 1
    max = 0
    for i in range(len(list_numbers)):
        if type(list_numbers[i]) == float:
            temp = list_numbers[i] - int(list_numbers[i])
            if temp > max:
                max = temp
            elif temp < min:
                min = temp

    print (max)
    print (min)
    print (max - min)
        
# list_num = [1.1, 1.2, 3.1, 5, 10.01]
# ex3_floatmaxmin_math(list_num)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def ex4_binary(number, binstr = ""):
    if number<2: return f"{number}" + binstr
    binstr = f"{int(number%2)}" + binstr
    return ex4_binary(number//2, binstr) 

# print(ex4_binary(45))




# *5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]


def ex5_negafib_1(number):

    if number <= 1:
        return number
    return ex5_negafib_1(number-1) + ex5_negafib_1(number-2)

def ex5_negafib_2(number):
    
    if number==1 or number==-1:
        return number
    return ex5_negafib_2(number+2) - ex5_negafib_2(number+1)

# Немного встрял в этой части. Ошибка глубины рекурсии. Не могу понять, она в возвращаемой функции 
# или в базовом условии. 



def ex5_negafib(N):
    spisok = [0]

    count = 1
    while count < N:
        spisok.append(ex5_negafib_1(count))
        spisok.insert(0,ex5_negafib_2(-count)) 
        count+=1

    print(spisok)

ex5_negafib(8)








