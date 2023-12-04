import random
matrix = [[random.randint(0, 10) for i in range(5)] for j in range(5)]
for i in range(len(matrix)):
    print(matrix[i])
a=[]
b=[]
for j in range(5):
    list_i=[]
    for i in matrix:
        list_i.append(i[j])
    a.append(list_i)
for i in matrix:
    list_j=[]
    for j in i:
        list_j.append(j)
    b.append(list_j)
flag=False
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            print("строка i :",j,"совпадает с столбцом:",i)
            flag=True
if flag==False:
    print("Совпадающих строк и столбцов не найдено ")

print(a)
print(b)










