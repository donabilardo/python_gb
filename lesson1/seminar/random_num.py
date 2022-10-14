#заполняем случайными числами список
from random import randint

n = int(input("Введите число >> :"))

lst = []
for i in range(n):
    #num = randint(-100,100)
    #lst.append(num)
    lst.append(randint(-1000,1000)) #без переменной, слуйчайное число сразу пишем в список lst

print(lst)
