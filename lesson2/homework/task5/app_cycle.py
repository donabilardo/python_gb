from random import randint

n = int(input("Введите длинну списка >> :"))

lst = []
for i in range(n):
    #num = randint(-100,100)
    # lst.append(num)
    # без переменной, слуйчайное число сразу пишем в список lst
    lst.append(randint(-1000, 1000))

print(f'Изначально заданный список {print(lst)}')


def mixList(lst):
    list = lst[:]
    listLenght = len(lst)

    for i in range(listLenght):
        indexLst = randint(0, listLenght - 1)
        temp = list[i]
        list[i] = list[indexLst]
        list[indexLst] = temp
    return list


print(f'Измененный список {mixList(lst)}')