# генерация случайных чисел
from random import randint  # импортируем randint

lenInt = int(input("Длинна списка :  "))
startInt = int(input("Начало диапазона :  "))
endInt = int(input("Конец диапазона :  "))


def randDigitFor(startInt, endInt, lenInt):
    listRandom = []
    for i in range(lenInt):
        listRandom.append(randint(startInt, endInt))
    return listRandom


def randDigitWhile(startInt, endInt, lenInt):
    listRandom = []
    i = 0
    while i < lenInt:
        listRandom.append(randint(startInt, endInt))
        i = i+1
    return listRandom


aList = randDigitWhile(startInt, endInt, lenInt)
print(aList)
