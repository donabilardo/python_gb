""" Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.
Том 2 тут мы преобразуем список из чисел в строки, список мы получили на предыдущем шаге
 """

import a_list_сomprehension

mySuperList = a_list_сomprehension.getRandomList()

def convertListToString(lst):
    lst = list(map(str,mySuperList))#Применяем функцию str (которая приводит к строке) ко всем элементам списка, полученым с помощью list comprehension
    return lst


myList = convertListToString(mySuperList)

