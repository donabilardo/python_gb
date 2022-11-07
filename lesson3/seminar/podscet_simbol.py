#подсчет количества символов
st = input("Введите фразу :")

a = 0
b = 0
c = 0
for elem in st:
    if elem == "a":
        a = a+1
    elif elem == "b":
        b = b+1
    elif elem == "c":
        c = c+1

count = {'a' : a, 'b':b, 'c':c}

print(count)