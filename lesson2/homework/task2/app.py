""" . Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. """
from datetime import datetime  # импортируе5м
startTime = datetime.now()  # начало выполнения скрипта

n = int(input("Введите число N:  "))
temp = 1
listDigit = []

for i in range(1, n+1, 1):  # 1 старт 2 конец 3 шаг
    temp = temp * i  # перемножаем все значения цикла
    listDigit.append(i)  # кидаём всё значения в список


print(f'Произведение чисе{listDigit} =  {temp}')  # Выводим найденый факториал

# выводим время выполнения скрипта
print(f'Время выполнения скрипта : {datetime.now() - startTime}')
