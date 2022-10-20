# Поиск максимального числа

listDigit = [111, 55, 656, 8, -3]

""" max_ = 0

for elementList in listDigit:
    if elementList > max_:
        max_ = elementList """

# поиск с помощью сортировки

listDigit.sort()
print(listDigit[-1])  # выводим последний осортированный элемент из списка
