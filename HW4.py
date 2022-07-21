


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
    for i in range(2,N):
        if N%i==0:
            list_div.append(i)

    print (list_div)

    for n in list_div:
        print(n)
        for x in range(2,n):
            # print(n/x)
            if n/x!=n//x:
                list_div.remove(n)
                break

    print (list_div)

ex2_div(100)








        

