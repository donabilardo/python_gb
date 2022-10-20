""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """

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

