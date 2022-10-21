""" 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. """
""" Для натурального n создать словарь индекс-значение,
 состоящий из элементов последовательности 3n + 1.
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} """


n = int(input("введите число "))
slov = {}
for i in range(1, n, 1):  # 1 начало отсчёта, 2 длинна, 3 шаг отсчёта
    slov[i] = 3 * i + 1
print(slov)


# генерация случайных чисел

""" lenInt = int(input("Длинна списка :  "))
startInt = int(input("Начало диапазона :  "))
endInt = int(input("Конец диапазона :  ")) 

from random import randint  # импортируем randint
def randDigitFor(startInt, endInt, lenInt):
    listRandom = []
    for i in range(lenInt):
        listRandom.append(randint(startInt, endInt))
    return listRandom


lst2 = [4, 7, 10, 13, 16, 19]


def spisok(lst):
    spisokReturn = []
    for i in range(len(lst)):
        tmp = lst[i] + 3
        spisokReturn.append(f"{i+1}:{tmp}")
    return spisokReturn


#lst = randDigitFor(startInt, endInt, lenInt)
print(spisok(lst2)) """
