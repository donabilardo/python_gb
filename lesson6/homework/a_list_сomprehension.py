""" Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.
Роман в шести томах. Том первый list comprehension тут мы создаем список с помощью
такой конструкции:

 список = [выражение for элемент in ранж] """



from random import randint


def getRandomList():
    lenInt = int(input("Длинна списка :  "))
    startInt = int(input("Начало диапазона :  "))
    endInt = int(input("Конец диапазона :  "))
    myList = [randint(startInt,endInt) for elem in range(lenInt)]
    return myList


#myList = getRandomList()
