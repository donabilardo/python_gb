""" Создайте программу для игры в ""Крестики-нолики""."""
#from re import T


board = list(range(1, 10))  # поле игры
wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
        (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]  # кортеж с выйгрышными комбинациями


def drawBoard():  # рисуем доску
    print("-------------")
    for i in range(3):
        print(f"| {0 + i * 3} | {1 + i * 3} | {2 + i * 3} |")
    print("-------------")


def takeInput(playerToken):
    while True:
        # приглашение к вводу, крест или ноль
        value = input("Куда поставить  " + playerToken + "? ")

        if not (value in "123456789"):  # проверяем введенные символы
            # если символы не 123456789 то выводим сообщение об ошибке
            print("Нужно вводить только цифры")
            continue  # возвращаем обратно приглашение на ввод
        value = int(value)  # gthtdjlbv cnhjre r byne

        if str(board[value - 1]) in "XO":  # если в поле стоит либо XO (английские)
            print("Данная клетка уже занята")  # сообщение об ошибке
            continue  # возвращаем обратно приглашение на ввод

        # если ячейка не занята то ставим туда либо  Х либо О и присваиваем "токен"
        board[value - 1] = playerToken
        break  # если все ок то выходим из цикла


def checkWin():
    for i in wins:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[1]-1]
        else:
            return False


def main():
    count = 0
    while True:
        drawBoard()

        if count % 2 == 0:
            takeInput("X")
        else:
            takeInput("O")

        if count > 3:
            winer = checkWin()
            if winer:
                drawBoard()
                print(winer, "выиграл!")
                break

        count += 1
        if count > 8:
            drawBoard()
            print("Ничья")
            break


main()
