
#отбираем только чётные числа списка

#Заменим двухзначные числа на 2 ноля

from a_list_сomprehension import getRandomList

myList = getRandomList()

print('Изначально сгенерированный список')
print(myList)

for i, d in enumerate(myList):
    if 10 <= abs(d) <= 99:
        myList[i] = 0


print('___________________________________')
print('Отфильтрованный список')
print(myList)





