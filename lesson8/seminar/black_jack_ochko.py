import random

koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(koloda)

print("Поиграем в очко? ")

count1 = 0

while True:
    choice = input("Вы будете брать карту?     Y \ N \n")
    if choice == "Y" or "y" or "д" or "Д":
        current = koloda.pop()
        print(f"Вам попалась карта: %d" %current)
        count1 += current
        if count1 > 21:
            print(f"Вы проиграли, ваш счёт {count1}")
            break
        elif count1 == 21:
            print("ОЧКО")
            break
        else:
            print(f"У вас {current} очков")
    elif choice == "N" or "n" or "н" or "Н":
        print(f"У вас {current} очков и вы заклнчили игру")
        exit()
        break
        



