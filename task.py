import random
def proverka_lengt(lenght):
    d = random.randint(1, 1000)
    i=0
    while True:
        if i == len(lenght):
            length.append(d)
            break
        elif length[i] == d:
            d = random.randint(1, 1000)
            i=0
        else: i=i+1
n = int(input())
Massiv = []
length = [] #список с данными о размерах списков
i=0
while i<n:
    proverka_lengt(length) #функция создания случайной длины массива и проверка на наличие такой же длины
    l = []
    j=0
    while j<length[i]:
        l.append(random.randint(1,1000))
        j=j+1
    if (i+1) % 2 == 0: l.sort() #сортировка, так как 0 элемент не является четным и нечетным, то 1ый элемент нечетный
    else: l.sort(reverse=True)
    Massiv.append(l)
    i=i+1
print(Massiv)


