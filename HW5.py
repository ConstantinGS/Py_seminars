import random
import copy

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) (доп) Подумайте как наделить бота ""интеллектом""


def ex1_candy():

    candies = 2021
    move_player = False
    move_bot = False
   
    difficulty_level = int(input("Выбери уровень сложности (легкий = 1, нормальный = 2, сложный = 3) \n"))

    if random.randint(0,1) == 1: 
        print("Твой ход")
        move_player = True
    else:
        print("Я начинаю") 
        move_bot = True

    while candies>28:
        if move_player == True:
            take_candy_player = int(input("Бери конфеты \n"))
            while take_candy_player>28: 
                take_candy_player = int(input("Возьми поменьше \n"))
            candies = candies - take_candy_player
            move_player = False
            move_bot = True
            print(f"Конфет осталось {candies}")
            
        if move_bot == True:
                
            print("Беру конфеты")
                
            take_candy_bot = random.randint(1,28)
            if difficulty_level != 1:
                if difficulty_level == 2 and random.randint(1,5) != 4:
                    for i in range(1,29):
                        if (candies-i)%29==0:
                            while (candies-take_candy_bot)%29!=0:
                                take_candy_bot = random.randint(1,28)
                            break
            

            print(f"Взял {take_candy_bot}")
            candies = candies - take_candy_bot
            move_player = True
            move_bot = False
            print(f"Конфет осталось {candies}")
    if (move_player and candies>0) or (move_bot and candies == 0): 
        print("Ты выиграл")
    else: 
        print("Ты проиграл")    

# ex1_candy()



# Создайте программу для игры в ""Крестики-нолики"".

def ex2_tic_tac_toe():

    field = [[" * ", " * ", " * " ],    
            [" * ", " * ", " * " ],
            [" * ", " * ", " * " ]]

    for i in field:
        print(*i)

    move_player = False
    move_bot = False
    game_over = False

    if random.randint(0,1) == 1: 
        print("Твой ход")
        move_player = True
    else:
        print("Я начинаю") 
        move_bot = True

    def check(new_field):
        if new_field[1][1] == " 0 " and new_field[0][2] == " 0 " and new_field[2][0] == " 0 ": return 1
        elif new_field[1][1] == " X " and new_field[0][2] == " X " and new_field[2][0] ==  " X ": return 1

        for i in range(0,3):
            counter_bot = 0
            counter_player = 0
            for j in range (0,3):
                if new_field[i][j] == " 0 ": counter_bot+=1
                elif new_field[i][j] == " X ": counter_player+=1
                else: break
                if counter_bot == 3 or counter_player == 3:
                    return 1
            counter_bot = 0
            counter_player = 0
            for k in range (0,3):
                if new_field[k][i] == " 0 ": counter_bot+=1
                elif new_field[k][i] == " X ": counter_player+=1
                else: break
                if counter_bot == 3 or counter_player == 3:
                    return 1

            for z in range (0,3):
                if new_field[z][z] == " 0 ": counter_bot+=1
                elif new_field[z][z] == " X ": counter_player+=1
                else: break
                if counter_bot == 3 or counter_player == 3:
                    return 1
            
             
        



        return 0 
                
    while game_over == 0:      

        if move_player == True:
            row = int(input("Введи номер строки \n"))
            column = int (input("Введи номер столбца \n"))
            while field[row-1][column-1] == " X " or field[row-1][column-1] == " 0 ":
                print("Поле занято")
                row = int(input("Введи номер строки \n"))
                column = int (input("Введи номер столбца \n"))
            field[row-1][column-1] = " X "
            move_bot = True
            move_player = False
            for i in field:
                print(*i)
            if check(field) == 1: 
                print("Ты выиграл")
                break

        if move_bot == True:
            print ("Мой ход")
            row = random.randint(1,3)
            column = random.randint(1,3)
            while field[row-1][column-1] == " 0 " or field[row-1][column-1] == " X ":
                row = random.randint(1,3)
                column = random.randint(1,3)

            field[row-1][column-1] = " 0 "
            move_bot = False
            move_player = True
            for i in field:
                print(*i)
            if check(field) == 1: 
                print("Ты проиграл")
                break            
            

# ex2_tic_tac_toe()




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def ex3_RLE(string_RLE):

    counter = 0
    new_string = ""
    while counter < (len(string_RLE)):

        if (counter < (len(string_RLE))-4 and string_RLE[counter] == string_RLE[counter+1] 
        == string_RLE[counter+2] ==string_RLE[counter+3] ):

            new_string += f"#" 

            asc_count = 0
            replace_string = ""

            while (counter+1 < len(string_RLE) and asc_count < 254 
            and string_RLE[counter] == string_RLE[counter+1]):

                asc_count +=1
                counter +=1

            asc_count +=1
            counter +=1 


            replace_string = str((hex(asc_count))).replace("0x", "")
            new_string += f"{replace_string}{string_RLE[counter-1]}"


        else: 
            new_string += f"{string_RLE[counter]}"
            counter +=1

   
    print(new_string)



ex3_RLE("яяяяяя быыыыыыыыыыыл здесььььььь")


    




 








