# вывод чисел от -N до N

n = int(input("Введите число:  "))
listDigit = []

for i in range(-n, n+1, 1):
    listDigit.append(i)
    print(i, end=" * ")
