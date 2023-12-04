import random
try:
    m=int(input("Введите кол-во элементов строки:"))
    n=int(input("Введите кол-во строк:"))
    if m<0 or n<0:
        raise ValueError
    new_list = []
    matrix = [[random.randint(0, 10) for i in range(m)] for j in range(n)]
    for i in range(len(matrix)):
        print(matrix[i])
    for i in matrix:
        summa = 1
        for j in i:
            summa *= j
        new_list.append(summa**(1/len(i)))
    print("Список В:",new_list)
except:
    print("Введеное не натуральное число ")






