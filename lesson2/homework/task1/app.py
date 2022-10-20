# Урок 2. Знакомство с Python. Продолжение
#1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.




inputData = int(input("Введите число  "))
if inputData < 0:
    inputData = inputData * -1

inputData = str(inputData)
inputDataLenght = len(inputData)
result = 0

for i in range(inputDataLenght):
    result = result + int(inputData[i])


print(result)


"""  print(inputDataLenght)


n = int(input("Введите число"))
 
suma = 0
 
while n > 0:
    digit = n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10

print("Сумма:", suma)  """