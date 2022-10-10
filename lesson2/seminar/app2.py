""" Для N = 5 1, -3, 5, -27 """

n = int(input("Введите число"))
lst = []

for i in range(n):
    lst.append((-3)**i)

print(lst)
