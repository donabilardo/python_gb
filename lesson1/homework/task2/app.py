""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


""" def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно") """


diap = [0,1]
flag = True
for X in diap:
    for Y in diap:
        for Z in diap:
            f1 = not(X or Y or Z)
            f2 = not(X) and  not(Y) and not(Z) 
            print(X, Y, Z, f1 == f2)
            if f1 != f2:
                flag == False
if flag:
    answer = "Соотвествует утверждению"
else:
    answer = "Не соотвествует утверждению"


print(answer)
