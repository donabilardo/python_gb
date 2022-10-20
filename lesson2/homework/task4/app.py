""" 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
 Позиции хранятся в файле file.txt в одной строке одно число. """
from datetime import datetime

startTime = datetime.now()

# проверка на вводимые данные
n = int(input("Введите число N (Не больше 10):  "))
if (n < 0) or (n == 0):
    print("Число должно быть больше 0")
    n = int(input("Введите число N (Не больше 10):  "))
elif (n > 10):
    print("Введите число не больше 10")
    n = int(input("Введите число N (Не больше 10):  "))

# создаем список
listDigit = []
for i in range(-n, n+1, 1):
    listDigit.append(i)


# читаем файл, где хранятся позиции элементов произведение которых необходимо найти
listFileRead = []  # список для прочтенных строках из файла с данными
fileRead = open("lesson2\\homework\\task4\\file.txt",
                "r")  # открываем файл на чтение

# цикл для записи строк в список
for line in fileRead:
    listFileRead.append(int(line))

fileRead.close  # закрываем открытый файл

# получаем произведение элементов на указанных позициях взятых из файла
result = listDigit[listFileRead[0]] * listDigit[listFileRead[1]]

print(listDigit)
print(listFileRead)
print(
    f'{listDigit[listFileRead[0]]} умножить на {listDigit[listFileRead[1]]} будет: {result}')
print(f'Время выполнения скрипта : {datetime.now() - startTime}')
