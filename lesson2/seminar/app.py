""" Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
 """


def f1():
    n = int(input("Введите количество членов последовательности"))
    lst = [i for i in range(1, n+1)]
    print(lst)


f1()
