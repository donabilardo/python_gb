""" # Домашнее задание 1 семинара
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

    - 6 -> да
    - 7 -> да
    - 1 -> нет
 """

listDay = ("Понедельник", "Вторник", "Среда",
           "Четверг", "Пятница", "Суббота", "Воскресенье")

dayoff1 = 6
dayoff2 = 7

inputData = int(
    input("Введите день недели, от 1 до 7 (где понедельник = 1, воскресенье = 7 >>>"))-1

if inputData < 0:
    print("Число не может быть меньше 1")
elif inputData >= 8:
    print("Число не может быть больше 7")
elif (inputData == dayoff1) or (inputData == dayoff2):
    print(f'{listDay[inputData]} является выходным днём')
else:
    print(f'{listDay[inputData]} является рабочим днём')
