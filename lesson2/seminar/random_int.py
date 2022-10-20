# генерация случайных чисел
from random import randint  # импортируем randint

lenInt = int(input("Длинна списка :  "))
startInt = int(input("Начало диапазона :  "))
endInt = int(input("Конец диапазона :  "))


def randDigit(startInt, endInt, lenInt):
    listRandom = []
    for i in range(lenInt):
        listRandom.append(randint(startInt, endInt))
    return listRandom


aList = randDigit(startInt, endInt, lenInt)
print(aList)
