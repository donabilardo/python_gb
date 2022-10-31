""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
 Играют два игрока делая ход друг после друга. 
 Первый ход определяется жеребьёвкой. 
 За один ход можно забрать не более чем 28 конфет.
  Все конфеты оппонента достаются сделавшему последний ход.
  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
 """


from random import randint
ostalostKonfet = 20 #количество оставшихся конфет
count = 1 #счётчик ходов
lot = randint(1,2) #выбираем рандомно кто будет ходить Игрок1 или Игрок 2

if lot == 1: #если 1 то ходит игрок1
    print("Первым ходит Игрок 1") #вывод кто ходит
elif lot == 2: #если 2 то ходит игрок2
    print("Первым ходит Игрок 2") #вывод кто ходит

flag = lot #тут храним очередность ходов

while True:
    print(f'\n******** Ход номер: {count} ********')
    if flag == 1:
        print(f'Ходит Игрок{flag}')
        beremKonfety = int(input("Сколько возьмем конфет? "))
        if (beremKonfety <= 0) or (beremKonfety > 28):
            print("Допускается брать от 1 до 28 конфет включительно")
            break
        elif ostalostKonfet <= 0:
            print(f"Победил Игрок{flag}, забрал конфеты за {count} ходов")
            break
        else:
            ostalostKonfet = ostalostKonfet - beremKonfety    
            count +=1
            flag += 1
            print(f'Осталось конфет {ostalostKonfet}')
    elif flag == 2:
        print(f'Ходит Игрок{flag}')
        beremKonfety = int(input("Сколько возьмем конфет? "))
        if (beremKonfety <= 0) or (beremKonfety > 28):
            print("Допускается брать от 1 до 28 конфет включительно")
            break
        elif ostalostKonfet <= 0:
            print(f"Победил Игрок{flag}, забрал конфеты за {count} ходов")
            break
        else:
            ostalostKonfet = ostalostKonfet - beremKonfety    
            count +=1
            flag = flag - 1    
            print(f'Осталось конфет {ostalostKonfet}')
