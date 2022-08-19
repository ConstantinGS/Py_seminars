import random
import copy


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
            