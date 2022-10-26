""" Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """
from random import randint  # импортируем randint

lenInt = int(input("Длинна списка :  "))
if lenInt < 0 or lenInt == 0:
    print("Длинна списка должна быть больше 0")
    exit()
startInt = int(input("Начало диапазона :  "))
endInt = int(input("Конец диапазона :  "))
if endInt < startInt or endInt == 0:
    print("Конец диапазона. должен быть больше чем начало диапазона")
    exit()

def randDigitWhile(startInt, endInt, lenInt):
    listRandom = []
    i = 0
    while i < lenInt:
        listRandom.append(randint(startInt, endInt))
        i = i+1
    return listRandom



def countElem (lst):
    newLst = []
    startElement = 0
    endElement = -1

    while startElement < len(lst)/2 and endElement < len(lst)/2:
        newLst.append(lst[startElement] * lst[endElement])
        startElement = startElement+1
        endElement = endElement - 1
    return newLst




aList = randDigitWhile(startInt, endInt, lenInt)
bList = countElem(aList)

print(f'Первоначальный список   {aList}')
print(f'Результирующий список   {bList}') 
