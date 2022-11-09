#Функция filter возвращает значения true
from random import randint


def getDigitParam():

    digitParam = {}
    
    while True:
        print(f'Введите длину списка:')
        lenDigit = int(input(""))
        if lenDigit < 0 or lenDigit == 0:
            print("Число должно быть положительным и не должно быть равно 0")
            continue
        else:
            lenDigit = int(input(""))

        print("Введите начало диапазона чисел:")
        startDigit = int(input(""))
        if startDigit < 0 or startDigit == 0:
            print("Диапазон числа не может начинаться с отрицательных значений и 0")
            continue
        else:
            startDigit = int(input(""))

        print("Введите конец диапазона чисел:")
        endDigit = int(input(""))
        if endDigit < startDigit or endDigit == startDigit:
            print("Конец диапазона чисел должен быть больше чем начало диапазона и не должен быть равен 0")
            continue
        else:
            endDigit = int(input(""))   


    return digitParam 

def getRandomList():
    pass

getDigitParam()

