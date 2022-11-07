""" Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

from random import randint

lenInt = int(input("Длинна списка :  "))
startInt = int(input("Начало диапазона :  "))
endInt = int(input("Конец диапазона :  "))


def randDigitWhile(startInt, endInt, lenInt):
    listRandom = []
    i = 0
    while i < lenInt:
        listRandom.append(randint(startInt, endInt))
        i = i+1
    return listRandom


def summNegativeDigit(lst):
    count = 0
    for i in range(len(lst)):  # 1 старт 2 конец 3 шаг
        if i % 2 != 0:
            count += lst[i]
    return count


aList = randDigitWhile(startInt, endInt, lenInt)
result = summNegativeDigit(aList)
print(
    f'Сгенерированный список {aList} Сумма элементов находящихся на нечётной позиции {result}')
