""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
 """

""" fileTxt = open("ttt.txt","r",encoding="utf-8")

fileTxt.close() """

def readTxt(): #функция для считывания файла с фразами
    spisokSlov = [] #список куда будем писать слова из файла
    try: #если файл найден то выполняем строку ниже
        fileTxt = open("input.txt","r",encoding="utf-8") #открываем файл на чтение указав нужную кодировку
    except FileNotFoundError: #если файл не найден выводим сообщение и прерываем выполнение программы
        print("Нужно проверить путь к файлу")
        exit()
    lines = fileTxt.readlines() 
    for line in lines:
        spisokSlov.append(line.strip())
    fileTxt.close()# закрываем файл
    return spisokSlov#возвращаем список с фразами

def clearABV(spisikInput):
    clearSpisokSlov =[] #список куда будем писать новый список откуда удалили абв
    
    for i in range(len(spisikInput)): #цикл перебора входящего списка
        if not 'абв' in spisikInput[i]: #проверяем если абв нету в элементе списка
          clearSpisokSlov.append(spisikInput[i]) #то добавляем его в другой список
        
    try: #если файл найден то выполняем строку ниже
        fileTxt = open("output.txt","w",encoding="utf-8") #открываем файл на чтение указав нужную кодировку
        for i in range(len(clearSpisokSlov)):
            fileTxt.writelines(clearSpisokSlov[i] + '\n')
    except FileNotFoundError: #если файл не найден выводим сообщение и прерываем выполнение программы
        print("Нужно проверить путь к файлу") #сообщение если файл не найден
        exit() #прерываем работу программы

    fileTxt.close()# закрываем файл
    return clearSpisokSlov#возвращаем список с фразами





slova = readTxt()
clearSlova = clearABV(slova)
print(f'Фразы из файла input.txt   {slova}')
print(f'Удалили из файла фразы где есть "абв"   {clearSlova}')
print('Полученый результат записали в файл output.txt')
