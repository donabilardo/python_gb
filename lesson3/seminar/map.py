""" . Задайте строку из набора чисел. Напишите программу, 
которая покажет большее и меньшее число. 
В качестве символа-разделителя используйте пробел. """

st = input().split() #получаем числа в виде строки. разделенные split()
print(type(st))
nums = list(map(int, st))# применяем конвертацию каждого элемента из списка
print(type(nums))