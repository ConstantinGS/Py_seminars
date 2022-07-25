
from fileinput import close
from msvcrt import kbhit
import random 

# Вычислить число c заданной точностью d

# Пример:

# - при d = 3, π = 3.141


def ex1_pi(d):
    pi = 0
    for k in range(d):
        pi += 1/16**k*(4/(8*k + 1) - 2/(8*k + 4) - 1/(8*k+ 5) - 1/(8*k + 6))
    return pi


# d = int(input())
# print(round(ex1_pi(d), d))




# Задайте натуральное число N. 
# Напишите программу, которая составит список простых делителей числа N. (1 - составное число)



def ex2_div(N):
    list_div = []
    for i in range(2,N//2+1):
        if N%i==0:
            list_div.append(i)

    for j in list_div[:]:
    
        for k in range(2,j):
            if (j%k) == 0:
                list_div.remove(j)
                break
     
    print (list_div)

# ex2_div(98)



# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def ex3_nonrepeat(list_numbers):

    list_number_new = []
    for i in list_numbers:
        if i not in list_number_new:
            list_number_new.append(i)
    print (list_number_new)

# l_num = [3, 5, 16, 789, 5, 35, 1, 5, 10, 789]
# ex3_nonrepeat(l_num)





# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def ex4_degree(k):

    degrees = {2: "\u00B2",
    3: "\u00B3", 4: "\u2074", 5: "\u2075",
    6: "\u2076", 7: "\u2077", 8: "\u2078",
    9: "\u2079" }

    polinom = ""

    if random.randint(0,1)==0:
            polinom += "-"
    polinom += str(random.randint(1,100))
    polinom += f"x{degrees[k]}"
    

    for j in range(k-1,-1,-1):
        rat = random.randint(0,100)
        if rat != 0:
            if random.randint(0,1)==0:
                polinom += "-"
            else: polinom += "+" 
            polinom += str(rat)
            if j in degrees:
                polinom += f"x{degrees[j]}"
            elif j == 1:
                polinom += f"x"

    print(f"{polinom} = 0")

# ex4_degree(2)


# 35(Доп). Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


def ad_ex():

    digits_1st = [""]
    digits_2nd = []
    digits_sum = []




    pol_File1 = open("Py_seminars\HW4_File_1.txt", "r")
    string1 = pol_File1.read()
    pol_File1.close
    pol_File2 = open("Py_seminars\HW4_File_2.txt", "r")
    string2 = pol_File2.read()
    pol_File1.close

    print(string1)
    print(string2)

    merker1 = 0
    count = 0
    for i in range(0,len(string1)):
        if string1[i] == "=" : break
        if string1[i] == "+" or string1[i] == " ":
            digits_1st.append("")
            count += 1
        else:
            digits_1st[count] += string1[i]

    print (digits_1st)

    # for j in digits_1st:
    #     for k in range(len(j)):
            

        


        






ad_ex()






        

