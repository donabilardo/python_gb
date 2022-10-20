""" 5. Реализуйте алгоритм перемешивания списка. """
#заполняем случайными числами список
from random import randint, random, shuffle

n = int(input("Введите длинну списка >> :"))

lst = []
for i in range(n):
    #num = randint(-100,100)
    #lst.append(num)
    lst.append(randint(-1000,1000)) #без переменной, слуйчайное число сразу пишем в список lst

print(f'Изначальный список {lst}')

shuffle(lst)

print(f'Перемешанный список {lst}')